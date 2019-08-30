# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class SettingsDialogBase
###########################################################################

class SettingsDialogBase ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Toolbox Settings", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		mainbSizer = wx.BoxSizer( wx.VERTICAL )

		self.settingsNotebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.curveTrackPanel = wx.Panel( self.settingsNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_curvebSizer = wx.BoxSizer( wx.VERTICAL )

		_curveTopSettingsfgSizer = wx.FlexGridSizer( 0, 3, 0, 0 )
		_curveTopSettingsfgSizer.SetFlexibleDirection( wx.BOTH )
		_curveTopSettingsfgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		_curveTopSettingsbSizer = wx.BoxSizer( wx.HORIZONTAL )

		curveTypeRadioBoxChoices = [ u"Circular", u"Hermite" ]
		self.curveTypeRadioBox = wx.RadioBox( self.curveTrackPanel, wx.ID_ANY, u"Curve Type", wx.DefaultPosition, wx.DefaultSize, curveTypeRadioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.curveTypeRadioBox.SetSelection( 0 )
		_curveTopSettingsbSizer.Add( self.curveTypeRadioBox, 0, wx.ALL, 5 )

		padVectorRadioBoxChoices = [ u"Auto", u"Manual" ]
		self.padVectorRadioBox = wx.RadioBox( self.curveTrackPanel, wx.ID_ANY, u"Pad Vectors", wx.DefaultPosition, wx.DefaultSize, padVectorRadioBoxChoices, 1, wx.RA_SPECIFY_COLS )
		self.padVectorRadioBox.SetSelection( 0 )
		_curveTopSettingsbSizer.Add( self.padVectorRadioBox, 0, wx.ALL, 5 )

		_arcRadiusStaticSizer = wx.StaticBoxSizer( wx.StaticBox( self.curveTrackPanel, wx.ID_ANY, u"Arc Radius" ), wx.HORIZONTAL )

		self.arcRadius_spinCtrlDouble = wx.SpinCtrlDouble( _arcRadiusStaticSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.SP_ARROW_KEYS, 0, 100, 0, 1 )
		self.arcRadius_spinCtrlDouble.SetDigits( 0 )
		_arcRadiusStaticSizer.Add( self.arcRadius_spinCtrlDouble, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		arcRadiusUnitsChoiceChoices = [ u"mm", u"mil", u"in" ]
		self.arcRadiusUnitsChoice = wx.Choice( _arcRadiusStaticSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, arcRadiusUnitsChoiceChoices, 0 )
		self.arcRadiusUnitsChoice.SetSelection( 0 )
		_arcRadiusStaticSizer.Add( self.arcRadiusUnitsChoice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.maxArcRadiusCheck = wx.CheckBox( _arcRadiusStaticSizer.GetStaticBox(), wx.ID_ANY, u"Max", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.maxArcRadiusCheck.SetValue(True)
		_arcRadiusStaticSizer.Add( self.maxArcRadiusCheck, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		_curveTopSettingsbSizer.Add( _arcRadiusStaticSizer, 0, wx.ALL|wx.EXPAND, 5 )


		_curveTopSettingsfgSizer.Add( _curveTopSettingsbSizer, 0, 0, 5 )


		_curvebSizer.Add( _curveTopSettingsfgSizer, 0, wx.EXPAND, 5 )

		_botPadVectorbSizer = wx.BoxSizer( wx.HORIZONTAL )

		_fromPadsbSizer = wx.StaticBoxSizer( wx.StaticBox( self.curveTrackPanel, wx.ID_ANY, u"From" ), wx.VERTICAL )

		_fromVectorsbSizer = wx.BoxSizer( wx.VERTICAL )

		_fromVectorsfgSizer = wx.FlexGridSizer( 3, 3, 0, 0 )
		_fromVectorsfgSizer.SetFlexibleDirection( wx.BOTH )
		_fromVectorsfgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.fromTopLeftRadioBtn = wx.RadioButton( _fromPadsbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		_fromVectorsfgSizer.Add( self.fromTopLeftRadioBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.fromTopRadioBtn = wx.RadioButton( _fromPadsbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		_fromVectorsfgSizer.Add( self.fromTopRadioBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.fromTopRightRadioBtn = wx.RadioButton( _fromPadsbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		_fromVectorsfgSizer.Add( self.fromTopRightRadioBtn, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.fromLeftRadioBtn = wx.RadioButton( _fromPadsbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		_fromVectorsfgSizer.Add( self.fromLeftRadioBtn, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		_fromPadImgbSizer = wx.BoxSizer( wx.VERTICAL )

		self.fromPadImg = wx.StaticBitmap( _fromPadsbSizer.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 75,75 ), 0 )
		_fromPadImgbSizer.Add( self.fromPadImg, 0, wx.ALL, 5 )


		_fromVectorsfgSizer.Add( _fromPadImgbSizer, 1, wx.EXPAND, 5 )

		self.fromRightRadioBtn = wx.RadioButton( _fromPadsbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		_fromVectorsfgSizer.Add( self.fromRightRadioBtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fromBottomLeftRadioBtn = wx.RadioButton( _fromPadsbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		_fromVectorsfgSizer.Add( self.fromBottomLeftRadioBtn, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.fromBottomRadioBtn = wx.RadioButton( _fromPadsbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		_fromVectorsfgSizer.Add( self.fromBottomRadioBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.fromBottomRightRadioBtn = wx.RadioButton( _fromPadsbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		_fromVectorsfgSizer.Add( self.fromBottomRightRadioBtn, 0, wx.ALL, 5 )


		_fromVectorsbSizer.Add( _fromVectorsfgSizer, 1, 0, 5 )


		_fromPadsbSizer.Add( _fromVectorsbSizer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		_botPadVectorbSizer.Add( _fromPadsbSizer, 1, wx.ALL, 5 )

		_toPadVectorbSizer = wx.StaticBoxSizer( wx.StaticBox( self.curveTrackPanel, wx.ID_ANY, u"To" ), wx.VERTICAL )

		_toVectorsbSizer = wx.BoxSizer( wx.VERTICAL )

		_toVectorsfgSizer = wx.FlexGridSizer( 3, 3, 0, 0 )
		_toVectorsfgSizer.SetFlexibleDirection( wx.BOTH )
		_toVectorsfgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.toTopLeftRadioBtn = wx.RadioButton( _toPadVectorbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		_toVectorsfgSizer.Add( self.toTopLeftRadioBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.toTopRadioBtn = wx.RadioButton( _toPadVectorbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		_toVectorsfgSizer.Add( self.toTopRadioBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.toTopRightRadioBtn = wx.RadioButton( _toPadVectorbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		_toVectorsfgSizer.Add( self.toTopRightRadioBtn, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.toLeftRadioBtn = wx.RadioButton( _toPadVectorbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		_toVectorsfgSizer.Add( self.toLeftRadioBtn, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		_toPadImgbSizer = wx.BoxSizer( wx.VERTICAL )

		self.toPadImg = wx.StaticBitmap( _toPadVectorbSizer.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 75,75 ), 0 )
		_toPadImgbSizer.Add( self.toPadImg, 0, wx.ALL, 5 )


		_toVectorsfgSizer.Add( _toPadImgbSizer, 1, wx.EXPAND, 5 )

		self.toRightRadioBtn = wx.RadioButton( _toPadVectorbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		_toVectorsfgSizer.Add( self.toRightRadioBtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.toBottomLeftRadioBtn = wx.RadioButton( _toPadVectorbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		_toVectorsfgSizer.Add( self.toBottomLeftRadioBtn, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.toBottomRadioBtn = wx.RadioButton( _toPadVectorbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		_toVectorsfgSizer.Add( self.toBottomRadioBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.toBottomRightRadioBtn = wx.RadioButton( _toPadVectorbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		_toVectorsfgSizer.Add( self.toBottomRightRadioBtn, 0, wx.ALL, 5 )


		_toVectorsbSizer.Add( _toVectorsfgSizer, 1, 0, 5 )


		_toPadVectorbSizer.Add( _toVectorsbSizer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		_botPadVectorbSizer.Add( _toPadVectorbSizer, 1, wx.EXPAND|wx.ALL, 5 )


		_curvebSizer.Add( _botPadVectorbSizer, 0, wx.EXPAND, 5 )


		self.curveTrackPanel.SetSizer( _curvebSizer )
		self.curveTrackPanel.Layout()
		_curvebSizer.Fit( self.curveTrackPanel )
		self.settingsNotebook.AddPage( self.curveTrackPanel, u"Curve", True )
		self.chamferTrackPanel = wx.Panel( self.settingsNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_chamferbSizer = wx.BoxSizer( wx.VERTICAL )

		self.chamferPanelwxNotebook = wx.Notebook( self.chamferTrackPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chamfer90DegPanel = wx.Panel( self.chamferPanelwxNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_chamfer90bSizer = wx.BoxSizer( wx.VERTICAL )

		_chamferfgSizer = wx.FlexGridSizer( 0, 4, 0, 0 )
		_chamferfgSizer.SetFlexibleDirection( wx.BOTH )
		_chamferfgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.chamferLineWidthStaticText = wx.StaticText( self.chamfer90DegPanel, wx.ID_ANY, u"Line Width", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chamferLineWidthStaticText.Wrap( -1 )

		_chamferfgSizer.Add( self.chamferLineWidthStaticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.chamferLineWidthSpinCtrlDouble = wx.SpinCtrlDouble( self.chamfer90DegPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 254, 0, 1 )
		self.chamferLineWidthSpinCtrlDouble.SetDigits( 0 )
		_chamferfgSizer.Add( self.chamferLineWidthSpinCtrlDouble, 0, wx.ALL, 5 )

		chamferLineWidthUnitwxChoiceChoices = [ u"mm", u"mil", u"in" ]
		self.chamferLineWidthUnitwxChoice = wx.Choice( self.chamfer90DegPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chamferLineWidthUnitwxChoiceChoices, 0 )
		self.chamferLineWidthUnitwxChoice.SetSelection( 0 )
		_chamferfgSizer.Add( self.chamferLineWidthUnitwxChoice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.chamferAutoLineWidthCheckBox = wx.CheckBox( self.chamfer90DegPanel, wx.ID_ANY, u"Auto", wx.DefaultPosition, wx.DefaultSize, 0 )
		_chamferfgSizer.Add( self.chamferAutoLineWidthCheckBox, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT, 5 )

		self.chamferBoardHeightStaticText = wx.StaticText( self.chamfer90DegPanel, wx.ID_ANY, u"Board Height", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chamferBoardHeightStaticText.Wrap( -1 )

		_chamferfgSizer.Add( self.chamferBoardHeightStaticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.chamferHeightSpinCtrlDouble = wx.SpinCtrlDouble( self.chamfer90DegPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 254, 0, 1 )
		self.chamferHeightSpinCtrlDouble.SetDigits( 0 )
		_chamferfgSizer.Add( self.chamferHeightSpinCtrlDouble, 0, wx.ALL, 5 )

		chamferBoardHeightUnitwxChoiceChoices = [ u"mm", u"mil", u"in" ]
		self.chamferBoardHeightUnitwxChoice = wx.Choice( self.chamfer90DegPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chamferBoardHeightUnitwxChoiceChoices, 0 )
		self.chamferBoardHeightUnitwxChoice.SetSelection( 0 )
		_chamferfgSizer.Add( self.chamferBoardHeightUnitwxChoice, 0, wx.ALL, 5 )

		self.chamferAutoBoardHeightCheckBox = wx.CheckBox( self.chamfer90DegPanel, wx.ID_ANY, u"Auto", wx.DefaultPosition, wx.DefaultSize, 0 )
		_chamferfgSizer.Add( self.chamferAutoBoardHeightCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.chamferAngleStaticText = wx.StaticText( self.chamfer90DegPanel, wx.ID_ANY, u"Angle", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chamferAngleStaticText.Wrap( -1 )

		_chamferfgSizer.Add( self.chamferAngleStaticText, 0, wx.ALL, 5 )

		self.chamferAngleSpinCtrlDouble = wx.SpinCtrlDouble( self.chamfer90DegPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 90, 0, 1 )
		self.chamferAngleSpinCtrlDouble.SetDigits( 0 )
		_chamferfgSizer.Add( self.chamferAngleSpinCtrlDouble, 0, wx.ALL, 5 )

		chamferUnitwxChoiceChoices = [ u"Deg", u"Rad" ]
		self.chamferUnitwxChoice = wx.Choice( self.chamfer90DegPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chamferUnitwxChoiceChoices, 0 )
		self.chamferUnitwxChoice.SetSelection( 0 )
		_chamferfgSizer.Add( self.chamferUnitwxChoice, 0, wx.ALL, 5 )

		self.chamferAutoAngleCheckBox = wx.CheckBox( self.chamfer90DegPanel, wx.ID_ANY, u"Auto", wx.DefaultPosition, wx.DefaultSize, 0 )
		_chamferfgSizer.Add( self.chamferAutoAngleCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		_chamfer90bSizer.Add( _chamferfgSizer, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		_chamferImgbSizer = wx.BoxSizer( wx.VERTICAL )

		self.chamferImg = wx.StaticBitmap( self.chamfer90DegPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 295,150 ), 0 )
		_chamferImgbSizer.Add( self.chamferImg, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		_chamfer90bSizer.Add( _chamferImgbSizer, 1, wx.EXPAND, 5 )

		self.chamferCutStaticText = wx.StaticText( self.chamfer90DegPanel, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.chamferCutStaticText.Wrap( -1 )

		_chamfer90bSizer.Add( self.chamferCutStaticText, 0, wx.ALL|wx.EXPAND, 5 )


		self.chamfer90DegPanel.SetSizer( _chamfer90bSizer )
		self.chamfer90DegPanel.Layout()
		_chamfer90bSizer.Fit( self.chamfer90DegPanel )
		self.chamferPanelwxNotebook.AddPage( self.chamfer90DegPanel, u"90", True )
		self.chamfer180DegPanel = wx.Panel( self.chamferPanelwxNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_chamfer180bSizer = wx.BoxSizer( wx.VERTICAL )


		self.chamfer180DegPanel.SetSizer( _chamfer180bSizer )
		self.chamfer180DegPanel.Layout()
		_chamfer180bSizer.Fit( self.chamfer180DegPanel )
		self.chamferPanelwxNotebook.AddPage( self.chamfer180DegPanel, u"180", False )

		_chamferbSizer.Add( self.chamferPanelwxNotebook, 1, wx.EXPAND|wx.ALL, 5 )


		self.chamferTrackPanel.SetSizer( _chamferbSizer )
		self.chamferTrackPanel.Layout()
		_chamferbSizer.Fit( self.chamferTrackPanel )
		self.settingsNotebook.AddPage( self.chamferTrackPanel, u"Chamfer", False )
		self.taperTrackPanel = wx.Panel( self.settingsNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_taperbSizer = wx.BoxSizer( wx.VERTICAL )

		self.taperPanelwxNotebook = wx.Notebook( self.taperTrackPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.linearTaperPanel = wx.Panel( self.taperPanelwxNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_linearTaperbSizer = wx.BoxSizer( wx.VERTICAL )

		_linearTaperSettingsbSizer = wx.FlexGridSizer( 0, 4, 0, 0 )
		_linearTaperSettingsbSizer.SetFlexibleDirection( wx.BOTH )
		_linearTaperSettingsbSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.taperW1StaticText = wx.StaticText( self.linearTaperPanel, wx.ID_ANY, u"W1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.taperW1StaticText.Wrap( -1 )

		_linearTaperSettingsbSizer.Add( self.taperW1StaticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.taperWidth1SpinCtrlDouble = wx.SpinCtrlDouble( self.linearTaperPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 254, 0, 1 )
		self.taperWidth1SpinCtrlDouble.SetDigits( 0 )
		_linearTaperSettingsbSizer.Add( self.taperWidth1SpinCtrlDouble, 0, wx.ALL, 5 )

		taperW1UnitwxChoiceChoices = [ u"mm", u"mil", u"in" ]
		self.taperW1UnitwxChoice = wx.Choice( self.linearTaperPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, taperW1UnitwxChoiceChoices, 0 )
		self.taperW1UnitwxChoice.SetSelection( 0 )
		_linearTaperSettingsbSizer.Add( self.taperW1UnitwxChoice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.taperW1CheckBox = wx.CheckBox( self.linearTaperPanel, wx.ID_ANY, u"Auto", wx.DefaultPosition, wx.DefaultSize, 0 )
		_linearTaperSettingsbSizer.Add( self.taperW1CheckBox, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

		self.taperW2StaticText = wx.StaticText( self.linearTaperPanel, wx.ID_ANY, u"W2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.taperW2StaticText.Wrap( -1 )

		_linearTaperSettingsbSizer.Add( self.taperW2StaticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.taperWidth2SpinCtrlDouble = wx.SpinCtrlDouble( self.linearTaperPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 254, 0, 1 )
		self.taperWidth2SpinCtrlDouble.SetDigits( 0 )
		_linearTaperSettingsbSizer.Add( self.taperWidth2SpinCtrlDouble, 0, wx.ALL, 5 )

		taperW2UnitwxChoiceChoices = [ u"mm", u"mil", u"in" ]
		self.taperW2UnitwxChoice = wx.Choice( self.linearTaperPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, taperW2UnitwxChoiceChoices, 0 )
		self.taperW2UnitwxChoice.SetSelection( 0 )
		_linearTaperSettingsbSizer.Add( self.taperW2UnitwxChoice, 0, wx.ALL, 5 )

		self.taperW2CheckBox = wx.CheckBox( self.linearTaperPanel, wx.ID_ANY, u"Auto", wx.DefaultPosition, wx.DefaultSize, 0 )
		_linearTaperSettingsbSizer.Add( self.taperW2CheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.taperLStaticText = wx.StaticText( self.linearTaperPanel, wx.ID_ANY, u"L", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.taperLStaticText.Wrap( -1 )

		_linearTaperSettingsbSizer.Add( self.taperLStaticText, 0, wx.ALL, 5 )

		self.taperLengthSpinCtrlDouble = wx.SpinCtrlDouble( self.linearTaperPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 254, 0, 1 )
		self.taperLengthSpinCtrlDouble.SetDigits( 0 )
		_linearTaperSettingsbSizer.Add( self.taperLengthSpinCtrlDouble, 0, wx.ALL, 5 )

		taperLengthUnitwxChoiceChoices = [ u"mm", u"mil", u"in" ]
		self.taperLengthUnitwxChoice = wx.Choice( self.linearTaperPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, taperLengthUnitwxChoiceChoices, 0 )
		self.taperLengthUnitwxChoice.SetSelection( 0 )
		_linearTaperSettingsbSizer.Add( self.taperLengthUnitwxChoice, 0, wx.ALL, 5 )

		self.taperLCheckBox = wx.CheckBox( self.linearTaperPanel, wx.ID_ANY, u"Auto", wx.DefaultPosition, wx.DefaultSize, 0 )
		_linearTaperSettingsbSizer.Add( self.taperLCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		_linearTaperbSizer.Add( _linearTaperSettingsbSizer, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		_linearTaperImgbSizer = wx.BoxSizer( wx.VERTICAL )

		self.taperImg = wx.StaticBitmap( self.linearTaperPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 295,150 ), 0 )
		_linearTaperImgbSizer.Add( self.taperImg, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		_linearTaperbSizer.Add( _linearTaperImgbSizer, 1, wx.EXPAND|wx.ALL, 5 )


		self.linearTaperPanel.SetSizer( _linearTaperbSizer )
		self.linearTaperPanel.Layout()
		_linearTaperbSizer.Fit( self.linearTaperPanel )
		self.taperPanelwxNotebook.AddPage( self.linearTaperPanel, u"Linear", True )
		self.exponentialTaperPanel = wx.Panel( self.taperPanelwxNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_exponentialTaperbSizer = wx.BoxSizer( wx.VERTICAL )


		self.exponentialTaperPanel.SetSizer( _exponentialTaperbSizer )
		self.exponentialTaperPanel.Layout()
		_exponentialTaperbSizer.Fit( self.exponentialTaperPanel )
		self.taperPanelwxNotebook.AddPage( self.exponentialTaperPanel, u"Exponential", False )
		self.klopfensteinTaperPanel = wx.Panel( self.taperPanelwxNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_klopfensteinTaperbSizer = wx.BoxSizer( wx.VERTICAL )


		self.klopfensteinTaperPanel.SetSizer( _klopfensteinTaperbSizer )
		self.klopfensteinTaperPanel.Layout()
		_klopfensteinTaperbSizer.Fit( self.klopfensteinTaperPanel )
		self.taperPanelwxNotebook.AddPage( self.klopfensteinTaperPanel, u"Klopfenstein", False )

		_taperbSizer.Add( self.taperPanelwxNotebook, 1, wx.EXPAND |wx.ALL, 5 )


		self.taperTrackPanel.SetSizer( _taperbSizer )
		self.taperTrackPanel.Layout()
		_taperbSizer.Fit( self.taperTrackPanel )
		self.settingsNotebook.AddPage( self.taperTrackPanel, u"Taper", False )
		self.junctionTrackPanel = wx.Panel( self.settingsNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_junctionbSizer = wx.BoxSizer( wx.VERTICAL )

		self.junctionPanelwxNotebook = wx.Notebook( self.junctionTrackPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.teeJunctionPanel = wx.Panel( self.junctionPanelwxNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_teeJunctionbSizer = wx.BoxSizer( wx.VERTICAL )


		self.teeJunctionPanel.SetSizer( _teeJunctionbSizer )
		self.teeJunctionPanel.Layout()
		_teeJunctionbSizer.Fit( self.teeJunctionPanel )
		self.junctionPanelwxNotebook.AddPage( self.teeJunctionPanel, u"Tee", True )
		self.stepJunctionPanel = wx.Panel( self.junctionPanelwxNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_stepJunctionbSizer = wx.BoxSizer( wx.VERTICAL )


		self.stepJunctionPanel.SetSizer( _stepJunctionbSizer )
		self.stepJunctionPanel.Layout()
		_stepJunctionbSizer.Fit( self.stepJunctionPanel )
		self.junctionPanelwxNotebook.AddPage( self.stepJunctionPanel, u"Step", False )
		self.crossJunctionPanel = wx.Panel( self.junctionPanelwxNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		_crossJunctionbSizer = wx.BoxSizer( wx.VERTICAL )


		self.crossJunctionPanel.SetSizer( _crossJunctionbSizer )
		self.crossJunctionPanel.Layout()
		_crossJunctionbSizer.Fit( self.crossJunctionPanel )
		self.junctionPanelwxNotebook.AddPage( self.crossJunctionPanel, u"Cross", False )

		_junctionbSizer.Add( self.junctionPanelwxNotebook, 1, wx.EXPAND |wx.ALL, 5 )


		self.junctionTrackPanel.SetSizer( _junctionbSizer )
		self.junctionTrackPanel.Layout()
		_junctionbSizer.Fit( self.junctionTrackPanel )
		self.settingsNotebook.AddPage( self.junctionTrackPanel, u"Junction", False )

		mainbSizer.Add( self.settingsNotebook, 1, wx.EXPAND |wx.ALL, 5 )

		settingsButtonSizer = wx.StdDialogButtonSizer()
		self.settingsButtonSizerOK = wx.Button( self, wx.ID_OK )
		settingsButtonSizer.AddButton( self.settingsButtonSizerOK )
		self.settingsButtonSizerCancel = wx.Button( self, wx.ID_CANCEL )
		settingsButtonSizer.AddButton( self.settingsButtonSizerCancel )
		settingsButtonSizer.Realize();

		mainbSizer.Add( settingsButtonSizer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )


		self.SetSizer( mainbSizer )
		self.Layout()
		mainbSizer.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.arcRadius_spinCtrlDouble.Bind( wx.EVT_TEXT_ENTER, self.OnArcRadiusTextEnter )
		self.maxArcRadiusCheck.Bind( wx.EVT_CHECKBOX, self.OnMaxArcRadiusCheck )
		self.fromTopLeftRadioBtn.Bind( wx.EVT_RADIOBUTTON, self.OnFromTopLeftRadioBtn )
		self.fromTopRadioBtn.Bind( wx.EVT_RADIOBUTTON, self.OnFromTopRadioBtn )
		self.fromTopRightRadioBtn.Bind( wx.EVT_RADIOBUTTON, self.OnFromTopRightRadioBtn )
		self.fromLeftRadioBtn.Bind( wx.EVT_RADIOBUTTON, self.OnFromLeftRadioBtn )
		self.fromRightRadioBtn.Bind( wx.EVT_RADIOBUTTON, self.OnFromRightRadioBtn )
		self.fromBottomLeftRadioBtn.Bind( wx.EVT_RADIOBUTTON, self.OnFromBottomLeftRadioBtn )
		self.fromBottomRadioBtn.Bind( wx.EVT_RADIOBUTTON, self.OnFromBottomRadioBtn )
		self.fromBottomRightRadioBtn.Bind( wx.EVT_RADIOBUTTON, self.OnFromBottomRightRadioBtn )
		self.toTopLeftRadioBtn.Bind( wx.EVT_RADIOBUTTON, self.OnToTopLeftRadioBtn )
		self.toTopRadioBtn.Bind( wx.EVT_RADIOBUTTON, self.OnToTopRadioBtn )
		self.toTopRightRadioBtn.Bind( wx.EVT_RADIOBUTTON, self.OnToTopRightRadioBtn )
		self.toLeftRadioBtn.Bind( wx.EVT_RADIOBUTTON, self.OnToLeftRadioBtn )
		self.toRightRadioBtn.Bind( wx.EVT_RADIOBUTTON, self.OnToRightRadioBtn )
		self.toBottomLeftRadioBtn.Bind( wx.EVT_RADIOBUTTON, self.OnToBottomLeftRadioBtn )
		self.toBottomRadioBtn.Bind( wx.EVT_RADIOBUTTON, self.OnToBottomRadioBtn )
		self.toBottomRightRadioBtn.Bind( wx.EVT_RADIOBUTTON, self.OnToBottomRightRadioBtn )
		self.chamferLineWidthSpinCtrlDouble.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnChamferSpinCtrlDouble )
		self.chamferLineWidthUnitwxChoice.Bind( wx.EVT_CHOICE, self.OnChamferLineWidthUnit )
		self.chamferAutoLineWidthCheckBox.Bind( wx.EVT_CHECKBOX, self.OnChamferWidthAuto )
		self.chamferHeightSpinCtrlDouble.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnChamferSpinCtrlDouble )
		self.chamferBoardHeightUnitwxChoice.Bind( wx.EVT_CHOICE, self.OnChamferBoardHeightUnit )
		self.chamferAutoBoardHeightCheckBox.Bind( wx.EVT_CHECKBOX, self.OnChamferHeightAuto )
		self.chamferAngleSpinCtrlDouble.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnChamferSpinCtrlDouble )
		self.chamferUnitwxChoice.Bind( wx.EVT_CHOICE, self.OnChamferAngleUnit )
		self.chamferAutoAngleCheckBox.Bind( wx.EVT_CHECKBOX, self.OnChamferAngleAuto )
		self.taperWidth1SpinCtrlDouble.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnTaperW1SpinCtrlDouble )
		self.taperW1UnitwxChoice.Bind( wx.EVT_CHOICE, self.OnTaperW1Unit )
		self.taperW1CheckBox.Bind( wx.EVT_CHECKBOX, self.OnTaperW1Auto )
		self.taperWidth2SpinCtrlDouble.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnTaperW2SpinCtrlDouble )
		self.taperW2UnitwxChoice.Bind( wx.EVT_CHOICE, self.OnTaperW2Unit )
		self.taperW2CheckBox.Bind( wx.EVT_CHECKBOX, self.OnTaperW2Auto )
		self.taperLengthSpinCtrlDouble.Bind( wx.EVT_SPINCTRLDOUBLE, self.OnTaperLengthSpinCtrlDouble )
		self.taperLengthUnitwxChoice.Bind( wx.EVT_CHOICE, self.OnTaperLengthUnit )
		self.taperLCheckBox.Bind( wx.EVT_CHECKBOX, self.OnTaperLengthAuto )
		self.settingsButtonSizerOK.Bind( wx.EVT_BUTTON, self.OnOKSettingsButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnArcRadiusTextEnter( self, event ):
		event.Skip()

	def OnMaxArcRadiusCheck( self, event ):
		event.Skip()

	def OnFromTopLeftRadioBtn( self, event ):
		event.Skip()

	def OnFromTopRadioBtn( self, event ):
		event.Skip()

	def OnFromTopRightRadioBtn( self, event ):
		event.Skip()

	def OnFromLeftRadioBtn( self, event ):
		event.Skip()

	def OnFromRightRadioBtn( self, event ):
		event.Skip()

	def OnFromBottomLeftRadioBtn( self, event ):
		event.Skip()

	def OnFromBottomRadioBtn( self, event ):
		event.Skip()

	def OnFromBottomRightRadioBtn( self, event ):
		event.Skip()

	def OnToTopLeftRadioBtn( self, event ):
		event.Skip()

	def OnToTopRadioBtn( self, event ):
		event.Skip()

	def OnToTopRightRadioBtn( self, event ):
		event.Skip()

	def OnToLeftRadioBtn( self, event ):
		event.Skip()

	def OnToRightRadioBtn( self, event ):
		event.Skip()

	def OnToBottomLeftRadioBtn( self, event ):
		event.Skip()

	def OnToBottomRadioBtn( self, event ):
		event.Skip()

	def OnToBottomRightRadioBtn( self, event ):
		event.Skip()

	def OnChamferSpinCtrlDouble( self, event ):
		event.Skip()

	def OnChamferLineWidthUnit( self, event ):
		event.Skip()

	def OnChamferWidthAuto( self, event ):
		event.Skip()


	def OnChamferBoardHeightUnit( self, event ):
		event.Skip()

	def OnChamferHeightAuto( self, event ):
		event.Skip()


	def OnChamferAngleUnit( self, event ):
		event.Skip()

	def OnChamferAngleAuto( self, event ):
		event.Skip()

	def OnTaperW1SpinCtrlDouble( self, event ):
		event.Skip()

	def OnTaperW1Unit( self, event ):
		event.Skip()

	def OnTaperW1Auto( self, event ):
		event.Skip()

	def OnTaperW2SpinCtrlDouble( self, event ):
		event.Skip()

	def OnTaperW2Unit( self, event ):
		event.Skip()

	def OnTaperW2Auto( self, event ):
		event.Skip()

	def OnTaperLengthSpinCtrlDouble( self, event ):
		event.Skip()

	def OnTaperLengthUnit( self, event ):
		event.Skip()

	def OnTaperLengthAuto( self, event ):
		event.Skip()

	def OnOKSettingsButtonClick( self, event ):
		event.Skip()


