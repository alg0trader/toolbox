
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

    