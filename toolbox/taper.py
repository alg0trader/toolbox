
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

    def TaperFootprint(self, center=pcbnew.wxPoint(0,0), angle_deg=0):
        self.module = pcbnew.MODULE(None)

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
                  (-self.w2/2 - self.tlen, self.w1/2), (-(self.w1/2 + self.tlen + self.w2/2), self.w1/2), \
                  (-(self.w1/2 + self.tlen + self.w2/2), -self.w1/2), (-self.w2/2 - self.tlen, -self.w1/2), \
                  (-self.w2/2, -self.w2/2)]

        points = [pcbnew.wxPoint(*point) for point in points]

        # Custom pad for smaller W2 x W2 pad
        cs_pad = pcbnew.D_PAD(self.module)
        cs_pad.SetSize(pcbnew.wxSize(self.w2, self.w2))
        cs_pad.SetShape(pcbnew.PAD_SHAPE_CUSTOM)
        cs_pad.SetAnchorPadShape(pcbnew.PAD_SHAPE_RECT)
        cs_pad.SetAttribute(pcbnew.PAD_ATTRIB_SMD)
        cs_pad.SetLayerSet(pcbnew.LSET(pcbnew.F_Cu))
        cs_pad.AddPrimitive(points, 0)
        cs_pad.SetLocalClearance(1)
        cs_pad.SetNet(self.net)
        cs_pad.SetPadName("1")

        self.module.Add(cs_pad)
        self.module.Add(Layout.smdRectPad(self.module, pcbnew.wxSize(self.w1, self.w1), pcbnew.wxPoint(-(self.w1/2 + self.tlen + self.w2/2), 0), "1", angle_deg, self.net))

        # TODO: Address other layers...

        self.module.SetPosition(center)

        # Add to pcbnew
        pcbnew.GetBoard().Add(self.module)
        pcbnew.Refresh()
