import wx
import wx.aui

import gui


# Callback functions

def curve_callback(event):
    '''Initiates the curve routing tool based on existing settings.'''
    # TODO read from settings

    pass

def chamfer_callback(event):
    '''Initiates the chamfer tool based on existing settings.'''
    pass

def settings_callback(event):
    '''Initiates the settings panel for edit.'''
    dlg = False
    
    try:
        dlg = gui.SettingsDialog()
        if dlg.ShowModal() == wx.ID_OK:
            # update settings
            pass
        else:
            # dialog cancelled
            pass
    finally:
        if dlg: dlg.Destroy()
