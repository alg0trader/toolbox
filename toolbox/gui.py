
import wx
import wx.aui
import traceback


def menu_dialog(msg, e=None):
    if e: msg = '\n'.join(msg, str(e), traceback.format.exc())

    # TODO: beautify dialog window
    dlg = wx.MessageDialog(None, msg, '', wx.OK)
    dlg.ShowModal()
    dlg.Destroy()


# Callback functions

def curve_callback(event):
    '''Initiates the curve routing tool'''
    print('hi')

def chamfer_callback(event):
    '''Initiates the chamfer tool'''
    print('hi')