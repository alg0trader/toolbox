
import wx
import wx.aui
from . import gui_base

import math as m
from . import chamfer
from .toolbox import get_path


def menu_dialog(msg, e=None):
    if e: msg = '\n'.join(msg, str(e), traceback.format.exc())
    dlg = wx.MessageDialog(None, msg, '', wx.OK)
    dlg.ShowModal()
    dlg.Destroy()


class CurveTab(gui_base.SettingsDialogBase):
    """
    Class for methods associated with the curve-tab in the settings dialog window.
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
    Class for methods associated with the curve-tab in the settings dialog window.
    """
    def __init__(self):
        # Load Chamfer-Tab Settings
        CurveTab.__init__(self)

        # Load arbitrary chamfer guide image
        self.chamferImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/arbitrary_chamfer.png'))
    
    # Override chamfer methods

class TaperTab(ChamferTab):
    """
    Class for methods associated with the taper-tab in the settings dialog window.
    """
    def __init__(self):
        # Load Taper-Tab Settings
        ChamferTab.__init__(self)

        # Load arbitrary taper guide image
        self.taperImg.SetBitmap(wx.Bitmap(get_path() + '/toolbox_icons/arbitrary_taper.png'))
    

class SettingsDialog(TaperTab):
    """
    Class for inheriting dialog base class.
    """
    def __init__(self):
        TaperTab.__init__(self)

        self.Centre()

        # Set max ranges
        # get current units -> set max

    
    # hack for new wxFormBuilder generating code incompatible with old wxPython
    # noinspection PyMethodOverriding
    def SetSizeHints(self, sz1, sz2):
        try:
            # wxPython 3
            self.SetSizeHintsSz(sz1, sz2)
        except TypeError:
            # wxPython 4
            super(SettingsDialog, self).SetSizeHints(sz1, sz2)
    
    # def GetChamferAutorouteCheck(self):
    #     if self.chamferRouteTracksCheckBox.GetValue(): return '1'
    #     else: return '0'

    # def SetChamferAutoCheck(self, value):
    #     if value == '1': self.chamferRouteTracksCheckBox.SetValue(True)
    #     else: self.chamferRouteTracksCheckBox.SetValue(False)
    
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
        pass
    
    def OnChamferWidthAuto( self, event ):
        if self.chamferAutoLineWidthCheckBox.IsChecked():
            self.chamferLineWidthStaticText.Enable(False)
            self.chamferLineWidthSpinCtrlDouble.Enable(False)
            self.chamferLineWidthUnitwxChoice.Enable(False)
        else:
            self.chamferLineWidthStaticText.Enable(True)
            self.chamferLineWidthSpinCtrlDouble.Enable(True)
            self.chamferLineWidthUnitwxChoice.Enable(True)

    def OnChamferBoardHeightUnit(self, event):
        pass
    
    def OnChamferHeightAuto(self, event):
        if self.chamferAutoBoardHeightCheckBox.IsChecked():
            self.chamferBoardHeightStaticText.Enable(False)
            self.chamferHeightSpinCtrlDouble.Enable(False)
            self.chamferBoardHeightUnitwxChoice.Enable(False)
        else:
            self.chamferBoardHeightStaticText.Enable(True)
            self.chamferHeightSpinCtrlDouble.Enable(True)
            self.chamferBoardHeightUnitwxChoice.Enable(True)

    def OnChamferAngleUnit(self, event):
        pass
    
    def OnChamferAngleAuto(self, event):
        if self.chamferAutoAngleCheckBox.IsChecked():
            self.chamferAngleStaticText.Enable(False)
            self.chamferAngleSpinCtrlDouble.Enable(False)
            self.chamferUnitwxChoice.Enable(False)
        else:
            self.chamferAngleStaticText.Enable(True)
            self.chamferAngleSpinCtrlDouble.Enable(True)
            self.chamferUnitwxChoice.Enable(True)

    def OnTaperW1SpinCtrlDouble(self, event):
        w1 = self.taperWidth1SpinCtrlDouble.GetValue()
        if str(self.taperW1UnitwxChoice.GetSelection()) == '1': w1 = w1 * 0.0254
        elif str(self.taperW1UnitwxChoice.GetSelection()) == '2': w1 = w1 * 25.4

        # errors = chamfer.Taper.CheckParameters(lw, bh, ca)
        # if len(errors) >= 1: menu_dialog('Errors:\n%s' % errors
    
    def OnTaperW1Unit(self, event):
        pass

    def OnTaperW1Auto(self, event):
        if self.taperW1CheckBox.IsChecked():
            self.taperW1StaticText.Enable(False)
            self.taperWidth1SpinCtrlDouble.Enable(False)
            self.taperW1UnitwxChoice.Enable(False)
        else:
            self.taperW1StaticText.Enable(True)
            self.taperWidth1SpinCtrlDouble.Enable(True)
            self.taperW1UnitwxChoice.Enable(True)

    def OnTaperW2SpinCtrlDouble(self, event):
        w2 = self.taperWidth2SpinCtrlDouble.GetValue()
        if str(self.taperW2UnitwxChoice.GetSelection()) == '1': w2 = w2 * 0.0254
        elif str(self.taperW2UnitwxChoice.GetSelection()) == '2': w2 = w2 * 25.4

        # errors = chamfer.Taper.CheckParameters(lw, bh, ca)
        # if len(errors) >= 1: menu_dialog('Errors:\n%s' % errors

    def OnTaperW2Unit(self, event):
        pass
    
    def OnTaperW2Auto(self, event):
        if self.taperW2CheckBox.IsChecked():
            self.taperW2StaticText.Enable(False)
            self.taperWidth2SpinCtrlDouble.Enable(False)
            self.taperW2UnitwxChoice.Enable(False)
        else:
            self.taperW2StaticText.Enable(True)
            self.taperWidth2SpinCtrlDouble.Enable(True)
            self.taperW2UnitwxChoice.Enable(True)
    
    def OnTaperLengthSpinCtrlDouble(self, event):
        length = self.taperLengthSpinCtrlDouble.GetValue()
        if str(self.taperLengthUnitwxChoice.GetSelection()) == '1': length = length * 0.0254
        elif str(self.taperLengthUnitwxChoice.GetSelection()) == '2': length = length * 25.4

        # errors = chamfer.Taper.CheckParameters(lw, bh, ca)
        # if len(errors) >= 1: menu_dialog('Errors:\n%s' % errors

    def OnTaperLengthUnit(self, event):
        pass

    def OnTaperLengthAuto(self, event):
        if self.taperLCheckBox.IsChecked():
            self.taperLStaticText.Enable(False)
            self.taperLengthSpinCtrlDouble.Enable(False)
            self.taperLengthUnitwxChoice.Enable(False)
        else:
            self.taperLStaticText.Enable(True)
            self.taperLengthSpinCtrlDouble.Enable(True)
            self.taperLengthUnitwxChoice.Enable(True)

    def OnOKSettingsButtonClick(self, event):
        # Save settings from user
        # TODO check if input settings are valid
        pass
