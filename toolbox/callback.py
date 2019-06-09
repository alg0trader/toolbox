import wx
import wx.aui

import gui
import pcbnew
import chamfer
import settings
from layout import Layout

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

    # Check if two pads or two tracks are selected
    net = None
    layer = None
    center = pcbnew.wxPoint(0, 0)
    spads = Layout.get_selected_pads()
    stracks = Layout.get_selected_tracks()
    
    if len(spads) == 2:
        if spads[0].GetNetname() != spads[1].GetNetname():
            gui.menu_dialog('Pads must be assigned\nto the same net.')
            return
        
        net = spads[0].GetNet()
        layer = spads[0].GetParent().GetLayer()

        p0 = spads[0].GetPosition()
        p1 = spads[1].GetPosition()

        center = pcbnew.wxPoint((p0.x + p1.x)/2, (p0.y + p1.y)/2)
    elif len(stracks) == 2:
        if stracks[0].GetNetname() != stracks[1].GetNetname():
            gui.menu_dialog('Tracks must be assigned\nto the same net.')
            return
        
        net = stracks[0].GetNet()
        layer = stracks[0].GetLayer()

        p0 = stracks[0].GetPosition()
        p1 = stracks[1].GetPosition()

        center = pcbnew.wxPoint((p0.x + p1.x)/2, (p0.y + p1.y)/2)
    else:
        gui.menu_dialog('Select two or more tracks, or two pads.')
        return

    cfgSettings = settings.ChamferSettings()
    cfgSettings.Load()
    
    lw = float(cfgSettings.lineWidth)
    bh = float(cfgSettings.boardHeight)
    ca = float(cfgSettings.chamferAngle)
    
    if cfgSettings.lineUnit == '1': lw = lw * 0.0254
    elif cfgSettings.lineUnit == '2': lw = lw * 25.4
    
    if cfgSettings.heightUnit == '1': bh = bh * 0.0254
    elif cfgSettings.heightUnit == '2': bh = bh * 25.4
    
    if cfgSettings.angleUnit == '1': ca = ca * 57.2958

    c = chamfer.Chamfer(lw, bh, ca, net, layer)
    c.ChamferFootprint(center)

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
