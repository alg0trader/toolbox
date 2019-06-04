
import wx
import wx.aui
import gui_base
import settings
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
        # gui_base.SettingsDialogBase.__init__(self, None)
        # super(ChamferTab, self).__init__()
        CurveTab.__init__(self)

        # Load arbitrary chamfer guide image
        self.chamferImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/arbitrary_chamfer.png'))


class SettingsDialog(ChamferTab):
    """
    Class for inheriting dialog base class.
    """
    def __init__(self):
        ChamferTab.__init__(self)

        self.Centre()

        # Load settings
        self.cfgSettings = settings.CurveSettings()
        self.cfgSettings.Load()

        self.curveTypeRadioBox.SetSelection(int(self.cfgSettings.curveType))
        self.padVectorRadioBox.SetSelection(int(self.cfgSettings.padVectorCfg))
        self.arcRadius_spinCtrlDouble.SetValue(float(self.cfgSettings.arcRadius))
        self.arcRadiusUnitsChoice.SetSelection(int(self.cfgSettings.arcRadiusUnit))
        self.SetMaxArcCheck(self.cfgSettings.maxArcCheck)
        self.SetFromPad(self.cfgSettings.fromPad)
        self.SetToPad(self.cfgSettings.toPad)
    
    # Hack for new wxFormBuilder generating code incompatible with old wxPython
    # no inspection PyMethodOverriding
    def SetSizeHints(self, sz1, sz2):
        self.SetSizeHintsSz(sz1, sz2)
    
    def OnOKSettingsButtonClick(self, event):
        # Save settings from user
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
        finally:
            self.Destroy()
