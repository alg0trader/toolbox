
import wx
import wx.aui
import gui_base

import chamfer
import settings
import math as m
from .toolbox import get_path


def menu_dialog(msg, e=None):
    if e: msg = '\n'.join(msg, str(e), traceback.format.exc())
    dlg = wx.MessageDialog(None, msg, '', wx.OK)
    dlg.ShowModal()
    dlg.Destroy()


class CurveTab(gui_base.SettingsDialogBase):
    """
    Class for methods relative to the curve-tab in the settings dialog window.
    """

    def __init__(self):
        # Load Curve-Tab Settings
        gui_base.SettingsDialogBase.__init__(self, None)
        # super(CurveTab, self).__init__()

        # Default to bottom vector direction for 'From' pad (for now)
        self.fromBottomRadioBtn.SetValue(True)
        self.fromPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/bottom.png'))

        # Default to top vector direction for 'To' pad (for now)
        self.toBottomRadioBtn.SetValue(True)
        self.toPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/bottom.png'))
    
    def GetMaxArcCheck(self):
        if self.maxArcRadiusCheck.GetValue(): return '1'
        else: return '0'
    
    def SetMaxArcCheck(self, value):
        if value == '1': self.maxArcRadiusCheck.SetValue(True)
        else: self.maxArcRadiusCheck.SetValue(False)
    
    def GetFromPad(self):
        if self.fromRightRadioBtn.GetValue(): return '0'
        elif self.fromTopRightRadioBtn.GetValue(): return '1'
        elif self.fromTopRadioBtn.GetValue(): return '2'
        elif self.fromTopLeftRadioBtn.GetValue(): return '3'
        elif self.fromLeftRadioBtn.GetValue(): return '4'
        elif self.fromBottomLeftRadioBtn.GetValue(): return '5'
        elif self.fromBottomRadioBtn.GetValue(): return '6'
        elif self.fromBottomRightRadioBtn.GetValue(): return '7'
        else: return '-1'
    
    def SetFromPad(self, value):
        if value == '0':
            self.fromRightRadioBtn.SetValue(True)
            self.OnFromRightRadioBtn(None)
        elif value == '1':
            self.fromTopRightRadioBtn.SetValue(True)
            self.OnFromTopRightRadioBtn(None)
        elif value == '2':
            self.fromTopRadioBtn.SetValue(True)
            self.OnFromTopRadioBtn(None)
        elif value == '3':
            self.fromTopLeftRadioBtn.SetValue(True)
            self.OnFromTopLeftRadioBtn(None)
        elif value == '4':
            self.fromLeftRadioBtn.SetValue(True)
            self.OnFromLeftRadioBtn(None)
        elif value == '5':
            self.fromBottomLeftRadioBtn.SetValue(True)
            self.OnFromBottomLeftRadioBtn(None)
        elif value == '6':
            self.fromBottomRadioBtn.SetValue(True)
            self.OnFromBottomRadioBtn(None)
        elif value == '7':
            self.fromBottomRightRadioBtn.SetValue(True)
            self.OnFromBottomRightRadioBtn(None)
    
    def GetToPad(self):
        if self.toRightRadioBtn.GetValue(): return 0
        elif self.toTopRightRadioBtn.GetValue(): return 1
        elif self.toTopRadioBtn.GetValue(): return 2
        elif self.toTopLeftRadioBtn.GetValue(): return 3
        elif self.toLeftRadioBtn.GetValue(): return 4
        elif self.toBottomLeftRadioBtn.GetValue(): return 5
        elif self.toBottomRadioBtn.GetValue(): return 6
        elif self.toBottomRightRadioBtn.GetValue(): return 7
        else: return -1
    
    def SetToPad(self, value):
        if value == '0':
            self.toRightRadioBtn.SetValue(True)
            self.OnToRightRadioBtn(None)
        elif value == '1':
            self.toTopRightRadioBtn.SetValue(True)
            self.OnToTopRightRadioBtn(None)
        elif value == '2':
            self.toTopRadioBtn.SetValue(True)
            self.OnToTopRadioBtn(None)
        elif value == '3':
            self.toTopLeftRadioBtn.SetValue(True)
            self.OnToTopLeftRadioBtn(None)
        elif value == '4':
            self.toLeftRadioBtn.SetValue(True)
            self.OnToLeftRadioBtn(None)
        elif value == '5':
            self.toBottomLeftRadioBtn.SetValue(True)
            self.OnToBottomLeftRadioBtn(None)
        elif value == '6':
            self.toBottomRadioBtn.SetValue(True)
            self.OnToBottomRadioBtn(None)
        elif value == '7':
            self.toBottomRightRadioBtn.SetValue(True)
            self.OnToBottomRightRadioBtn(None)
    
    def OnFromTopLeftRadioBtn(self, event):
        self.fromPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/top_left.png'))
    
    def OnFromTopRadioBtn(self, event):
        self.fromPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/top.png'))
    
    def OnFromTopRightRadioBtn(self, event):
        self.fromPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/top_right.png'))
    
    def OnFromLeftRadioBtn(self, event):
        self.fromPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/left.png'))
    
    def OnFromRightRadioBtn(self, event):
        self.fromPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/right.png'))
    
    def OnFromBottomLeftRadioBtn(self, event):
        self.fromPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/bottom_left.png'))
    
    def OnFromBottomRadioBtn(self, event):
        self.fromPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/bottom.png'))
    
    def OnFromBottomRightRadioBtn(self, event):
        self.fromPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/bottom_right.png'))
    
    def OnToTopLeftRadioBtn(self, event):
        self.toPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/top_left.png'))
    
    def OnToTopRadioBtn(self, event):
        self.toPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/top.png'))
    
    def OnToTopRightRadioBtn(self, event):
        self.toPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/top_right.png'))
    
    def OnToLeftRadioBtn(self, event):
        self.toPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/left.png'))
    
    def OnToRightRadioBtn(self, event):
        self.toPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/right.png'))
    
    def OnToBottomLeftRadioBtn(self, event):
        self.toPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/bottom_left.png'))
    
    def OnToBottomRadioBtn(self, event):
        self.toPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/bottom.png'))
    
    def OnToBottomRightRadioBtn(self, event):
        self.toPadImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/bottom_right.png'))

class ChamferTab(CurveTab):
    """
    Class for methods relative to the curve-tab in the settings dialog window.
    """
    def __init__(self):
        # Load Chamfer-Tab Settings
        CurveTab.__init__(self)

        # Load arbitrary chamfer guide image
        self.chamferImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/arbitrary_chamfer.png'))
    
    # Override chamfer methods
    

class SettingsDialog(ChamferTab):
    """
    Class for inheriting dialog base class.
    """
    def __init__(self):
        ChamferTab.__init__(self)

        self.Centre()

        # Load Curve-Tab settings
        self.cfgSettings = settings.CurveSettings()
        self.cfgSettings.Load()

        self.curveTypeRadioBox.SetSelection(int(self.cfgSettings.curveType))
        self.padVectorRadioBox.SetSelection(int(self.cfgSettings.padVectorCfg))
        self.arcRadius_spinCtrlDouble.SetValue(float(self.cfgSettings.arcRadius))
        self.arcRadiusUnitsChoice.SetSelection(int(self.cfgSettings.arcRadiusUnit))
        self.SetMaxArcCheck(self.cfgSettings.maxArcCheck)
        self.SetFromPad(self.cfgSettings.fromPad)
        self.SetToPad(self.cfgSettings.toPad)

        # Load Chamfer-Tab settings
        self.cfgSettings = settings.ChamferSettings()
        self.cfgSettings.Load()

        self.chamferLineWidthSpinCtrlDouble.SetValue(float(self.cfgSettings.lineWidth))
        self.chamferLineWidthUnitwxChoice.SetSelection(int(self.cfgSettings.lineUnit))
        self.chamferHeightSpinCtrlDouble.SetValue(float(self.cfgSettings.boardHeight))
        self.chamferBoardHeightUnitwxChoice.SetSelection(int(self.cfgSettings.heightUnit))
        self.chamferAngleSpinCtrlDouble.SetValue(float(self.cfgSettings.chamferAngle))
        self.chamferUnitwxChoice.SetSelection(int(self.cfgSettings.angleUnit))
        self.SetChamferAutorouteCheck(self.cfgSettings.chamferAutoroute)
        self.OnChamferSpinCtrlDouble(None)
    
    # Hack for new wxFormBuilder generating code incompatible with old wxPython
    # no inspection PyMethodOverriding
    def SetSizeHints(self, sz1, sz2):
        self.SetSizeHintsSz(sz1, sz2)
    
    def GetChamferAutorouteCheck(self):
        if self.chamferRouteTracksCheckBox.GetValue(): return '1'
        else: return '0'

    def SetChamferAutorouteCheck(self, value):
        if value == '1': self.chamferRouteTracksCheckBox.SetValue(True)
        else: self.chamferRouteTracksCheckBox.SetValue(False)
    
    def OnChamferSpinCtrlDouble(self, event):
        lw = self.chamferLineWidthSpinCtrlDouble.GetValue()
        bh = self.chamferHeightSpinCtrlDouble.GetValue()
        ca = self.chamferAngleSpinCtrlDouble.GetValue()
        
        if str(self.chamferLineWidthUnitwxChoice.GetSelection()) == '1': lw = lw * 0.0254
        elif str(self.chamferLineWidthUnitwxChoice.GetSelection()) == '2': lw = lw * 25.4
        
        if str(self.chamferBoardHeightUnitwxChoice.GetSelection()) == '1': bh = bh * 0.0254
        elif str(self.chamferBoardHeightUnitwxChoice.GetSelection()) == '2': bh = bh * 25.4
        
        if str(self.chamferUnitwxChoice.GetSelection()) == '1': ca = round(ca * 57.2958, 3)

        errors = chamfer.Chamfer.CheckParameters(lw, bh, ca)
        if len(errors) >= 1: menu_dialog('Errors:\n%s' % errors)

        cut = chamfer.Chamfer(lw, bh, ca, None, None).OptimalMiter()
        self.chamferCutStaticText.SetLabel(' '*63 + 'Cut: {0:.2f}%'.format(cut*100))
        
    
    def OnChamferLineWidthUnit(self, event):
        oldUnit = self.cfgSettings.lineUnit
        newUnit = str(self.chamferLineWidthUnitwxChoice.GetSelection())

        if oldUnit == '0' and newUnit == '1':
            self.chamferLineWidthSpinCtrlDouble.SetValue(self.chamferLineWidthSpinCtrlDouble.GetValue()*39.3701)
            self.cfgSettings.lineUnit = '1'
            self.chamferLineWidthSpinCtrlDouble.SetIncrement(1)
        elif oldUnit == '0' and newUnit == '2':
            self.chamferLineWidthSpinCtrlDouble.SetValue(self.chamferLineWidthSpinCtrlDouble.GetValue()*0.0393701)
            self.cfgSettings.lineUnit = '2'
            self.chamferLineWidthSpinCtrlDouble.SetIncrement(0.001)
        elif oldUnit == '1' and newUnit == '0':
            self.chamferLineWidthSpinCtrlDouble.SetValue(self.chamferLineWidthSpinCtrlDouble.GetValue()*0.0254)
            self.cfgSettings.lineUnit = '0'
            self.chamferLineWidthSpinCtrlDouble.SetIncrement(0.01)
        elif oldUnit == '1' and newUnit == '2':
            self.chamferLineWidthSpinCtrlDouble.SetValue(self.chamferLineWidthSpinCtrlDouble.GetValue()*0.001)
            self.cfgSettings.lineUnit = '2'
            self.chamferLineWidthSpinCtrlDouble.SetIncrement(0.001)
        elif oldUnit == '2' and newUnit == '0':
            self.chamferLineWidthSpinCtrlDouble.SetValue(self.chamferLineWidthSpinCtrlDouble.GetValue()*25.4)
            self.cfgSettings.lineUnit = '0'
            self.chamferLineWidthSpinCtrlDouble.SetIncrement(0.01)
        elif oldUnit == '2' and newUnit == '1':
            self.chamferLineWidthSpinCtrlDouble.SetValue(self.chamferLineWidthSpinCtrlDouble.GetValue()*1000.0)
            self.cfgSettings.lineUnit = '1'
            self.chamferLineWidthSpinCtrlDouble.SetIncrement(1)
        
        self.OnChamferSpinCtrlDouble(None)

    def OnChamferBoardHeightUnit(self, event):
        oldUnit = self.cfgSettings.heightUnit
        newUnit = str(self.chamferBoardHeightUnitwxChoice.GetSelection())

        if oldUnit == '0' and newUnit == '1':
            # mm to mils
            self.chamferHeightSpinCtrlDouble.SetValue(self.chamferHeightSpinCtrlDouble.GetValue()*39.3701)
            self.cfgSettings.heightUnit = '1'
            self.chamferHeightSpinCtrlDouble.SetIncrement(1)
        elif oldUnit == '0' and newUnit == '2':
            # mm to in
            self.chamferHeightSpinCtrlDouble.SetValue(self.chamferHeightSpinCtrlDouble.GetValue()*0.0393701)
            self.cfgSettings.heightUnit = '2'
            self.chamferHeightSpinCtrlDouble.SetIncrement(0.001)
        elif oldUnit == '1' and newUnit == '0':
            # mils to mm
            self.chamferHeightSpinCtrlDouble.SetValue(self.chamferHeightSpinCtrlDouble.GetValue()*0.0254)
            self.cfgSettings.heightUnit = '0'
            self.chamferHeightSpinCtrlDouble.SetIncrement(0.01)
        elif oldUnit == '1' and newUnit == '2':
            # mils to in
            self.chamferHeightSpinCtrlDouble.SetValue(self.chamferHeightSpinCtrlDouble.GetValue()*0.001)
            self.cfgSettings.heightUnit = '2'
            self.chamferHeightSpinCtrlDouble.SetIncrement(0.001)
        elif oldUnit == '2' and newUnit == '0':
            # in to mm
            self.chamferHeightSpinCtrlDouble.SetValue(self.chamferHeightSpinCtrlDouble.GetValue()*25.4)
            self.cfgSettings.heightUnit = '0'
            self.chamferHeightSpinCtrlDouble.SetIncrement(0.01)
        elif oldUnit == '2' and newUnit == '1':
            # in to mils
            self.chamferHeightSpinCtrlDouble.SetValue(self.chamferHeightSpinCtrlDouble.GetValue()*1000.0)
            self.cfgSettings.heightUnit = '1'
            self.chamferHeightSpinCtrlDouble.SetIncrement(1)
        
        self.OnChamferSpinCtrlDouble(None)

    def OnChamferAngleUnit(self, event):
        oldUnit = self.cfgSettings.angleUnit
        newUnit = str(self.chamferUnitwxChoice.GetSelection())

        if oldUnit == '0' and newUnit == '1':
            # deg to rad
            self.chamferAngleSpinCtrlDouble.SetValue(m.radians(self.chamferAngleSpinCtrlDouble.GetValue()))
            self.cfgSettings.angleUnit = '1'
            self.chamferAngleSpinCtrlDouble.SetIncrement(0.01)
        elif oldUnit == '1' and newUnit == '0':
            # rad to deg
            self.chamferAngleSpinCtrlDouble.SetValue(round(m.degrees(self.chamferAngleSpinCtrlDouble.GetValue()), 2))
            self.cfgSettings.angleUnit = '0'
            self.chamferAngleSpinCtrlDouble.SetIncrement(1)

        self.OnChamferSpinCtrlDouble(None)
    
    def OnOKSettingsButtonClick(self, event):
        # Save settings from user
        # TODO check if input settings are valid
        try:
            # Curve-Tab settings
            cfgSettings = settings.CurveSettings()
            self.cfgSettings.curveType = self.curveTypeRadioBox.GetSelection()
            self.cfgSettings.padVectorCfg = self.padVectorRadioBox.GetSelection()
            self.cfgSettings.arcRadius = self.arcRadius_spinCtrlDouble.GetValue()
            self.cfgSettings.arcRadiusUnit = self.arcRadiusUnitsChoice.GetSelection()
            self.cfgSettings.maxArcCheck = self.GetMaxArcCheck()
            self.cfgSettings.fromPad = self.GetFromPad()
            self.cfgSettings.toPad = self.GetToPad()
            self.cfgSettings.Save()

            # Chamfer-Tab settings
            cfgSettings = settings.ChamferSettings()
            self.cfgSettings.lineWidth = self.chamferLineWidthSpinCtrlDouble.GetValue()
            self.cfgSettings.lineUnit = self.chamferLineWidthUnitwxChoice.GetSelection()
            self.cfgSettings.boardHeight = self.chamferHeightSpinCtrlDouble.GetValue()
            self.cfgSettings.heightunit = self.chamferBoardHeightUnitwxChoice.GetSelection()
            self.cfgSettings.chamferAngle = self.chamferAngleSpinCtrlDouble.GetValue()
            self.cfgSettings.angleUnit = self.chamferUnitwxChoice.GetSelection()
            self.cfgSettings.chamferAutoroute = self.GetChamferAutorouteCheck()
            self.cfgSettings.Save()
        finally:
            self.Destroy()
