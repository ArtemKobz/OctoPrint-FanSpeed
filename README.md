# OctoPrint-Fanspeed

Displays the print cooling fan speed in OctoPrint's nav bar.

![screenshot](./extras/assets/img/plugins/fanspeed/navbar.png)

Originally by: https://github.com/larp-welt/OctoPrint-FanSpeed

## Notes

* Numbers may differ from those displayed elsewhere due to different methods of rounding (i.e. round up, round down, ceiling or floor based rounding)
* Doesn't work with SD prints because the gcode doesn't pass through OctoPrint\*

\*May work on SD prints if your printer runs Repetier firmware as that sends feedback back to the host in the form of "Fanspeed:nnn" which this plugin can now look for.

## Setup

Install ~~via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or~~ manually using this URL:

    https://github.com/ntoff/OctoPrint-Fanspeed/archive/master.zip

