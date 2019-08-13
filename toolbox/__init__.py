import os
import time
import inspect
import threading

import wx
import wx.aui
import pcbnew

import callback
from .toolbox import *


# def init_toolbar():
#     # From Miles McCoo's blog
#     # https://kicad.mmccoo.com/2017/03/05/adding-your-own-command-buttons-to-the-pcbnew-gui/
#     def find_pcbnew_window():
#         windows = wx.GetTopLevelWindows()
#         pcbneww = [w for w in windows if "pcbnew" in w.GetTitle().lower()]
#         if len(pcbneww) != 1:
#             return None
#         return pcbneww[0]

#     while not wx.GetApp():
#         time.sleep(1)
    
#     # Add curve routing tool button.
#     curves_button_id = 0
#     curves_button_bm = wx.Bitmap(get_path() + '/toolbox_icons/curves.png', wx.BITMAP_TYPE_PNG)

#     # Add chamfer tool button.
#     chamfer_button_id = 1
#     chamfer_button_bm = wx.Bitmap(get_path() + '/toolbox_icons/chamfer.png', wx.BITMAP_TYPE_PNG)

#     # Add settings tool button.
#     settings_button_id = 2
#     settings_button_bm = wx.Bitmap(get_path() + '/toolbox_icons/settings.png', wx.BITMAP_TYPE_PNG)

#     while True:
#         time.sleep(1)
#         pcbwin = find_pcbnew_window()
#         if not pcbwin:
#             continue

#         top_tb = pcbwin.FindWindowById(pcbnew.ID_V_TOOLBAR)     # Former: pcbnew.ID_H_TOOLBAR
#         if not curves_button_id == 0 or not top_tb.FindTool(curves_button_id):
#             top_tb.AddSeparator()
#             curves_button_id = wx.NewId()
#             top_tb.AddTool(curves_button_id, "Curve", curves_button_bm, "Route a curved trace", wx.ITEM_NORMAL)
#             top_tb.Bind(wx.EVT_TOOL, callback.curve_callback, id=curves_button_id)
#             top_tb.Realize()
#         if not chamfer_button_id == 0 or not top_tb.FindTool(chamfer_button_id):
#             top_tb.AddSeparator()
#             chamfer_button_id = wx.NewId()
#             top_tb.AddTool(chamfer_button_id, "Chamfer", chamfer_button_bm, "Create a chamfer", wx.ITEM_NORMAL)
#             top_tb.Bind(wx.EVT_TOOL, callback.chamfer_callback, id=chamfer_button_id)
#             top_tb.Realize()
#     if not settings_button_id == 0 or not top_tb.FindTool(settings_button_id):
#             top_tb.AddSeparator()
#             settings_button_id = wx.NewId()
#             top_tb.AddTool(settings_button_id, "Chamfer", chamfer_button_bm, "Adjust Toolbox settings", wx.ITEM_NORMAL)
#             top_tb.Bind(wx.EVT_TOOL, callback.chamfer_callback, id=settings_button_id)
#             top_tb.Realize()

# TODO: Figure out why the taper button, while registered before settings, is last in the menu...

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

# # Add a button the hacky way if plugin button is not supported
# # in pcbnew, unless this is linux.
# # TODO: Figure out a cleaner way to do this
# if not curvePlugin.pcbnew_icon_support and not sys.platform.startswith('linux'):
#     t = threading.Thread(target=init_toolbar)
#     t.daemon = True
#     t.start()

# if not chamferPlugin.pcbnew_icon_support and not sys.platform.startswith('linux'):
#     t = threading.Thread(target=init_toolbar)
#     t.daemon = True
#     t.start()

# if not settingsPlugin.pcbnew_icon_support and not sys.platform.startswith('linux'):
#     t = threading.Thread(target=init_toolbar)
#     t.daemon = True
#     t.start()
