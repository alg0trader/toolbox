import wx
import wx.aui

import gui
import chamfer
import settings


# Callback functions

def curve_callback(event):
    '''Initiates the curve routing tool based on existing settings.'''
    cfgSettings = settings.CurveSettings()
    cfgSettings.Load()

    if cfgSettings.curveType == cfgSettings._CURVE_TYPE_CFG['Value']['Circular']:
        # Route a circular curve
        pass
    elif cfgSettings.curveType == cfgSettings._CURVE_TYPE_CFG['Value']['Hermite']:
        # Route a hermite curve
        pass

def chamfer_callback(event):
    '''Initiates the chamfer tool based on existing settings.'''
    cfgSettings = settings.ChamferSettings()
    cfgSettings.Load()
    
    # TODO Convert mm, mil, or in depending on setting
    

    c = chamfer.Chamfer(float(cfgSettings.lineWidth), float(cfgSettings.boardHeight), float(cfgSettings.chamferAngle))
    c.ChamferFootprint()

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
