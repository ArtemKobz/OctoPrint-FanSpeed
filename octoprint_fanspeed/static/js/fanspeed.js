$(function() {
    function FanspeedViewModel(parameters) {
        var self = this;

        self.fanspeedModel = parameters[0];
        self.loginState = parameters[1];
        self.access = parameters[2];

        self.speed = ko.observable();
        self.speed("N/A")

        self.onDataUpdaterPluginMessage = function(plugin, data) {
            if (plugin != "fanspeed") {
                return;
            }
            if (data.speed) {
                self.speed(gettext(data.speed))
            }
        };
    }


    OCTOPRINT_VIEWMODELS.push({
        construct: FanspeedViewModel,
        
        dependencies: ["printerStateViewModel", "loginStateViewModel", "accessViewModel"],
        elements: ["#navbar_plugin_fanspeed"]
    });

});
