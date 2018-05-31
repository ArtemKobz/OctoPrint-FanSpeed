# coding=utf-8
from __future__ import absolute_import

import re
import octoprint.plugin
from flask.ext.babel import gettext
import logging

class FanSpeedPlugin(octoprint.plugin.StartupPlugin,
                     octoprint.plugin.TemplatePlugin,
                     octoprint.plugin.AssetPlugin):

    def __init__(self):
        self.speed = "N/A"

    def process_gcode_received(self, comm, line, *args, **kwargs):
        if "Fanspeed" not in line:
            return line

        fan_response = re.search("(\d*\.?\d+?)", line)
        if fan_response and fan_response.group(1):
            fan_response = fan_response.group(1)
            if float(fan_response) == 0:
                self.speed = gettext('Off')
            else:
                self.speed = str(int(float(fan_response)*100.0/255.0))+"%"
            self._plugin_manager.send_plugin_message(self._identifier, dict(speed=self.speed))
        return line

    def process_gcode(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
        if gcode and gcode.startswith('M106'):
            s = re.search("S(.+)", cmd)
            if s and s.group(1):
                s = s.group(1)
                if float(s) == 0:
                    self.speed = gettext('Off')
                else:
                    self.speed = str(int(float(s)*100.0/255.0))+"%"
                self._plugin_manager.send_plugin_message(self._identifier, dict(speed=self.speed))
        if gcode and gcode.startswith('M107'):
            self.speed = gettext('Off')
            self._plugin_manager.send_plugin_message(self._identifier, dict(speed=self.speed))
        return None

    def get_assets(self):
        return { 
            "js": ["js/fanspeed.js"],
            "css": ["css/fanspeed.css"],
            "less": ["less/fanspeed.less"]
        }

    def get_update_information(self):
        return dict(
            navbarfanspeed=dict(
                displayName="Fan Speed",
                displayVersion=self._plugin_version,

                type="github_release",
                user="ntoff",
                repo="OctoPrint-FanSpeed",
                current=self._plugin_version,

                pip="https://github.com/ntoff/OctoPrint-FanSpeed/archive/{target_version}.zip"
            )
        )

__plugin_name__ = "Fan Speed (ntoff mod)"
__plugin_description__ = "Displays the print cooling fan speed in OctoPrint's nav bar"
__plugin_url__ = "https://github.com/ntoff/OctoPrint-FanSpeed"
__plugin_author_email__ = "" #unset the email to prevent email about this version going to the wrong author, see "setup.py" for the original author's contact details
__plugin_author__ = "Marcus J. Ertl (modified by ntoff)"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = FanSpeedPlugin()
    
    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.comm.protocol.gcode.sent": __plugin_implementation__.process_gcode,
        "octoprint.comm.protocol.gcode.received": __plugin_implementation__.process_gcode_received,
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }