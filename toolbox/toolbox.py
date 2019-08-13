import os
import wx
import pcbnew
import inspect

import callback


def get_path():
    # Get the script directory in order to locate icons.
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    return os.path.dirname(os.path.abspath(filename))


class CurvePlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Curve"
        self.category = "Layout"
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        self.icon_file_name = get_path() + '/toolbox_icons/curve.png'
        self.description = "Route curved tracks in Pcbnew."
    
    def Run(self):
        callback.curve_callback(None)

class ChamferPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Chamfer"
        self.category = "Layout"
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        self.icon_file_name = get_path() + '/toolbox_icons/chamfer.png'
        self.description = "Route chamfered tracks in Pcbnew."
    
    def Run(self):
        callback.chamfer_callback(None)

class TaperPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Taper"
        self.category = "Layout"
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        self.icon_file_name = get_path() + '/toolbox_icons/taper.png'
        self.description = "Route tapered tracks in Pcbnew."
    
    def Run(self):
        callback.taper_callback(None)

class SettingsPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Settings"
        self.category = "Layout"
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        self.icon_file_name = get_path() + '/toolbox_icons/settings.png'
        self.description = "Adjust Toolbox settings."
    
    def Run(self):
        callback.settings_callback(None)


if __name__ == "__main__":
    app = wx.App()
