
import gui
import pcbnew
import math as m
from linear import Linear as ln

class Layout:
    """
    Class for common Pcbnew layout operations.
    """
    @staticmethod
    def get_selected_pads(board=None):
        if board is None:
            board = pcbnew.GetBoard()
        
        return list(filter(lambda p: p.IsSelected(), board.GetPads()))
    
    @staticmethod
    def get_pad_coord(pads):
        '''Obtain wxPoint(x,y) coordinates of pads.'''
        return list(filter(lambda p: p.GetPosition(), pads))
    
    @staticmethod
    def get_track_width():
        '''Returns current track width dimension that the user has set.'''
        return pcbnew.GetBoard().GetDesignSettings().GetCurrentTrackWidth()
    
    @staticmethod
    def get_selected_pad_centers():
        '''Returns the center coordinates of any module with a selected pad.'''
        board = pcbnew.GetBoard()
        modules = pcbnew.board.GetModules()
        spads = [p for p in board.GetPads() if p.IsSelected()]
        pcoords = [p.GetPosition() for p in spads]
        return [modules.GetPad(p).GetCenter() for p in pcoords]
    
    @staticmethod
    def draw_track_segment(board, start, end, net, layer=0):
        '''Returns a new pcbnew board with an added track.'''
        tseg = pcbnew.TRACK(board)
        tseg.SetStart(start)
        tseg.SetEnd(end)
        tseg.SetWidth(Layout.get_track_width())
        tseg.SetLayer(layer)
        board.Add(tseg)
        return board
    
    @staticmethod
    def get_selected_tracks(board=None):
        if board is None:
            board = pcbnew.GetBoard()
        
        return list(filter(lambda t: t.IsSelected(), board.GetTracks()))