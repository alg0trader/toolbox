
# TODO: Fetch active layer instead of defaulting to F_Cu (obtain from selected pads, that way you can obtain nets)


import pcbnew
import math as m
from layout import Layout


class Chamfer:
    """
    Class for creating arbitrary angled chamfers.
    """
    def __init__(self, width, height, angle, net, layer):
        self.width = pcbnew.FromMM(width)       # mm
        self.height = pcbnew.FromMM(height)     # mm
        self.angle_deg = angle                  # deg
        self.net = net
        self.layer = layer
    
    def bilinear_interpolation(self, x, y, points):
        '''
        http://stackoverflow.com/questions/8661537/how-to-perform-bilinear-interpolation-in-python
        Interpolate (x,y) from values associated with four points.

        The four points are a list of four triplets:  (x, y, value).
        The four points can be in any order.  They should form a rectangle.

            >>> bilinear_interpolation(12, 5.5,
            ...                        [(10, 4, 100),
            ...                         (20, 4, 200),
            ...                         (10, 6, 150),
            ...                         (20, 6, 300)])
            165.0
        '''
        # See formula at:  http://en.wikipedia.org/wiki/Bilinear_interpolation

        points = sorted(points)               # Order points by x, then by y
        (x1, y1, q11), (_x1, y2, q12), (x2, _y1, q21), (_x2, _y2, q22) = points

        return (q11 * (x2 - x) * (y2 - y) +
                q21 * (x - x1) * (y2 - y) +
                q12 * (x2 - x) * (y - y1) +
                q22 * (x - x1) * (y - y1)
                ) / ((x2 - x1) * (y2 - y1) + 0.0)
    
    def OptimalMiter(self):
        '''
        Calculate optimal miter by interpolating from table.
        https://awrcorp.com/download/faq/english/docs/Elements/MBENDA.htm
        "Transmission Line Design Handbook", by Brian C. Wadell (pg. 292-293)
        '''
        w, h, angle = self.width, self.height, self.angle_deg

        wh = w/h
        whs = [0.5, 1.0, 2.0]
        angles = [0, 30, 60, 90, 120]
        table = [
            [0, 12, 45, 75, 98],
            [0, 19, 41, 63, 92],
            [0, 7, 31, 56, 79]
        ]
        
        for i, x in enumerate(whs):
            if x > wh: break
        for j, y in enumerate(angles):
            if y > angle: break
        i = min(i-1, 1)
        j = min(j-1, 3)
        px = lambda ii,jj: (whs[ii],angles[jj],table[ii][jj])
        x1 = px(i,j)
        x2 = px(i+1,j)
        y1 = px(i,j+1)
        y2 = px(i+1,j+1)
        
        return self.bilinear_interpolation(wh, angle, [x1,x2,y1,y2])/100.0
    
    @staticmethod
    def CheckParameters(w, h, angle):
        errors = list()
        if w < 0: errors.append('Width < 0')
        if w/h < 0.25: errors.append('Width/Height < 0.25')
        if angle > 90: errors.append('Angle > 90 deg')
        if angle < 0: errors.append('Angle < 0 deg')
        
        if len(errors) >= 1: return '\n'.join(errors)
        else: return ''        
    
    def ChamferFootprint(self, center=pcbnew.wxPoint(0,0)):
        self.module = pcbnew.MODULE(None)   # Create new module
        self.angle = m.radians(self.angle_deg)

        # Calculate the miter
        w = self.width

        # Width of the corner from edge of the corner to inside corner
        corner_width = pcbnew.ToMM(w)/m.cos(self.angle/2)

        # Get proportion of width to cut
        cut = self.OptimalMiter()
        print("Cut: {0:.2f}%".format(cut*100))

        # Distance from uncut outside corner point to point 7
        cut = pcbnew.FromMM(cut*corner_width/m.cos((m.pi - self.angle)/2))

        # Distance between points 2 and 3 and points 3 and 4
        # Minimum of w/2 to satisfy DRC, otherwise pads are too close
        # and track connected to other pad overlaps the other one.
        # Rounded trace end can also stick out of the cut area
        # if a is too small.
        a = max(cut-self.width*m.tan(self.angle/2), w/2)

        # Distance between points 3 and 4
        x34 = a*m.sin(self.angle)
        y34 = a*m.cos(self.angle)

        # Distance between points 4 and 5
        x45 = self.width*m.cos(self.angle)
        y45 = self.width*m.sin(self.angle)

        # Distance from point 7 to 1 (no x-component)
        d71 = a + self.width*m.tan(self.angle/2)-cut

        #   1  2
        #   +--+
        #   |  |3
        # 7 \  --+ 4
        #    \   |
        #     \--+ 5
        #     6
        dW = w/55       # To prevent tracks from over-extending
        points = [
                (-w/2, -d71/2),
                (w/2, -d71/2),
                (w/2, a - d71/2 + dW),
                (w/2+x34-(d71/2-d71/1e5-dW)*m.sin(self.angle), a+y34-d71/2-(d71/2-d71/1e5-dW)*m.cos(self.angle) + dW),
                (w/2+x34-x45-(d71/2-d71/1e5-dW)*m.sin(self.angle), a+y34+y45-d71/2-(d71/2-d71/1e5-dW)*m.cos(self.angle)+dW),
                (cut*m.sin(self.angle) - w/2, a+self.width*m.tan(self.angle/2)+cut*m.cos(self.angle)-d71/2+dW),
                (-w/2, a+self.width*m.tan(self.angle/2)-cut-d71/2+dW)
                ]

        # Last two points can be equal
        if points[-2] == points[-1]:
            points = points[:-1]

        points = [pcbnew.wxPoint(*point) for point in points]

        # Custom pad
        cs_pad = pcbnew.D_PAD(self.module)
        cs_pad.SetSize(pcbnew.wxSize(w, d71))
        cs_pad.SetShape(pcbnew.PAD_SHAPE_CUSTOM)
        cs_pad.SetAnchorPadShape(pcbnew.PAD_SHAPE_RECT)
        cs_pad.SetAttribute(pcbnew.PAD_ATTRIB_SMD)
        cs_pad.SetLayerSet(pcbnew.LSET(pcbnew.F_Cu))
        cs_pad.AddPrimitive(points, 0)
        cs_pad.SetLocalClearance(1)
        cs_pad.SetNet(self.net)
        cs_pad.SetPadName("1")

        self.module.Add(cs_pad)

        # Halfway between points 4 and 5
        posx = ((w/2+x34) + (w/2+x34-x45))/2
        posy = ((a+y34-d71/2) + (a+y34+y45-d71/2))/2

        # Position pad so that pad edge touches polygon edge
        posx -= (d71/2 - dW)*m.sin(self.angle)
        posy -= (d71/2 - dW)*m.cos(self.angle)-dW
        size_pad = pcbnew.wxSize(d71, w)
        self.module.Add(Layout.smdRectPad(self.module, pcbnew.wxSize(w, d71), pcbnew.wxPoint(0, 0), "1", 0, self.net))      # Alignment pad
        self.module.Add(Layout.smdRectPad(self.module, size_pad, pcbnew.wxPoint(posx, posy), "1", (self.angle_deg-90)*10, self.net))
        
        self.module.Rotate(self.module.GetPosition(), (90 + self.angle_deg)*100)

        # self.module.MoveAnchorPosition(pcbnew.wxPoint((d71/2 - a - w/2)*m.sin(self.angle), \
        #                                (d71/2 - a - w/2)*m.cos(self.angle)))
        self.module.SetPosition(center)

        if self.layer == pcbnew.B_Cu: self.module.Flip(self.module.GetCenter())
        elif self.layer == pcbnew.F_Cu: self.module.Rotate(self.module.GetPosition(), (90 + self.angle_deg)*100)

        # Find center of bounding box for placement
        
        # Add to Pcbnew
        pcbnew.GetBoard().Add(self.module)
        pcbnew.Refresh()
