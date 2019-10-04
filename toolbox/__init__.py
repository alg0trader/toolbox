import os
import time
import inspect
import threading

import wx
import wx.aui
import pcbnew

from  . import callback
from .toolbox import *


# Register curve plugin
curvePlugin = CurvePlugin()
curvePlugin.defaults()
curvePlugin.register()

# Register chamfer plugin
chamferPlugin = ChamferPlugin()
chamferPlugin.defaults()
chamferPlugin.register()

# Register taper plugin
taperPlugin = TaperPlugin()
taperPlugin.defaults()
taperPlugin.register()

# Register settings plugin
settingsPlugin = SettingsPlugin()
settingsPlugin.defaults()
settingsPlugin.register()
