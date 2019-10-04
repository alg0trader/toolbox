import wx
import wx.aui

import pcbnew
from . import gui
from . import taper
from . import chamfer
from .layout import Layout

# Callback functions

def curve_callback(event):
    '''Initiates the curve routing tool based on existing settings.'''
    pass

def chamfer_callback(event):
    '''Initiates the chamfer tool based on existing settings.'''
    pass

def taper_callback(event):
    pass

def settings_callback(event):
    '''Initiates the settings panel for edit.'''
    dlg = False
    
    try:
        dlg = gui.SettingsDialog()
        if dlg.ShowModal() == wx.ID_OK:
            # Check for active window
            pass
        else:
            # Dialog cancelled
            pass
    finally:
        if dlg: dlg.Destroy()
