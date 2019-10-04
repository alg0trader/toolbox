
import pcbnew
import math as m
from layout import Layout

class Junction:
    """
    Class for creating RF/Microwave junctions.
    """
    def __init__(self, w1, w2, w3, net, layer):
        self.w1 = pcbnew.FromMM(w1)     # mm
        self.w2 = pcbnew.FromMM(w2)     # mm
        self.w3 = pcbnew.FromMM(w3)     # mm
        self.net = net
        self.layer = layer

    def JunctionFootprint(self, center=pcbnew.wxPoint(0,0), angle_deg=0):

        self.module = pcbnew.MODULE(None)

        # cs_pad = pcbnew.D_PAD(self.module)
        # cs_pad.SetSize(pcbnew.wxSize(self.w1, self.w1))
        # cs_pad.SetShape(pcbnew.PAD_SHAPE_CUSTOM)
        # cs_pad.SetAnchorPadShape(pcbnew.PAD_SHAPE_RECT)
        # cs_pad.SetAttribute(pcbnew.PAD_ATTRIB_SMD)
        # cs_pad.SetLayerSet(pcbnew.LSET(pcbnew.F_Cu))
        # cs_pad.SetLocalClearance(1)
        # cs_pad.SetNet(self.net)
        # cs_pad.SetPadName("1")

        # self.module.Add(cs_pad)

        self.module.Add(Layout.smdRectPad(self.module, pcbnew.wxSize(self.w1, self.w1), pcbnew.wxPoint(0,0), "1", angle_deg, self.net))
        self.module.SetPosition(center)

        pcbnew.GetBoard().Add(self.module)
        pcbnew.Refresh()
