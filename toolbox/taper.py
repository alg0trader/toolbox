
import pcbnew
import math as m
from layout import Layout


class Taper:
    """
    Class for creating tapers.
    """
    def __init__(self, w1, w2, tlen, net, layer):
        self.w1 = pcbnew.FromMM(w1)         # mm
        self.w2 = pcbnew.FromMM(w2)         # mm
        self.tlen = pcbnew.FromMM(tlen)     # mm
        self.net = net
        self.layer = layer

    @staticmethod
    def CheckParameters():
        pass

    def TaperFootprint(self, center=pcbnew.wxPoint(0,0), orientation=0):
        self.module = pcbnew.MODULE(None)

        # Create polygon points
        #                6
        # 5 +------------+
        #   |            |\
        #   |            | \ 7
        #   |            |  +---+ 0
        #   |            |  |   |
        #   |            |  +---+ 1
        #   |            | / 2
        #   |            |/
        # 4 +------------+
        #                3
        points = [(self.w2/2, -self.w2/2), (self.w2/2, self.w2/2), (-self.w2/2, self.w2/2), \
                  (-self.w2/2 - self.tlen, self.w1/2), (-(self.w1 + self.tlen + self.w2/2), self.w1/2), \
                  (-(self.w1 + self.tlen + self.w2/2), -self.w1/2), (-self.w2/2 - self.tlen, -self.w1/2), \
                  (-self.w2/2, -self.w2/2)]

        points = [pcbnew.wxPoint(*point) for point in points]
        self.module = Layout.Polygon(self.module, points, pcbnew.F_Cu)

        # Create pads
        angle = 0
        self.module.Add(Layout.smdRectPad(self.module, pcbnew.wxSize(self.w2, self.w2), pcbnew.wxPoint(0,0), "1", angle, self.net))
        self.module.Add(Layout.smdRectPad(self.module, pcbnew.wxSize(self.w1, self.w1), pcbnew.wxPoint(-(self.w1/2 + self.tlen + self.w2/2), 0), "2", angle, self.net))

        self.module.SetPosition(center)

        # Add to pcbnew
        pcbnew.GetBoard().Add(self.module)
        pcbnew.Refresh()
