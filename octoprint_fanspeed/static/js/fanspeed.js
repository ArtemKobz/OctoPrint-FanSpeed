$(function() {
    function FanspeedViewModel(parameters) {
        var self = this;

        self.fanspeedModel = parameters[0];

        self.speed = ko.observable();
        self.speed("N/A")

        self.onDataUpdaterPluginMessage = function(plugin, data) {
            if (plugin != "fanspeed") {
                return;
            }
            self.speed(data.speed)
        };
    }


    ADDITIONAL_VIEWMODELS.push([
        FanspeedViewModel,
        ["printerStateViewModel"],
        ["#navbar_plugin_fanspeed"]
    ]);

});
