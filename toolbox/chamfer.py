
# TODO: Fetch active layer instead of defaulting to F_Cu (obtain from selected pads, that way you can obtain nets)


import pcbnew
import math as m


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
    
    def smdRectPad(self, module, size, pos, name, angle):
        '''Build a rectangular pad.'''
        pad = pcbnew.D_PAD(module)
        pad.SetSize(size)
        pad.SetShape(pcbnew.PAD_SHAPE_RECT)
        pad.SetAttribute(pcbnew.PAD_ATTRIB_SMD)
        # Set only the copper layer without mask
        # since nothing is mounted on these pads
        pad.SetLayerSet(pcbnew.LSET(pcbnew.F_Cu))       # Get active layer
        pad.SetPos0(pos)
        pad.SetPosition(pos)
        pad.SetPadName(name)
        pad.Rotate(pos, angle)
        # Set clearance to small value, because
        # pads can be very close together.
        # If distance is smaller than clearance
        # DRC doesn't allow routing the pads
        pad.SetLocalClearance(1)
        pad.SetNet(self.net)

        return pad
    
    def Polygon(self, points, layer):
        '''Draw a polygon through specified points.'''

        polygon = pcbnew.EDGE_MODULE(self.module)
        polygon.SetWidth(0)         # Disables outline
        polygon.SetLayer(layer)
        polygon.SetShape(pcbnew.S_POLYGON)
        polygon.SetPolyPoints(points)

        self.module.Add(polygon)
    
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
            if x > wh:
                break
        for j, y in enumerate(angles):
            if y > angle:
                break
        i = min(i-1,1)
        j = min(j-1,3)
        px = lambda ii,jj: (whs[ii],angles[jj],table[ii][jj])
        x1 = px(i,j)
        x2 = px(i+1,j)
        y1 = px(i,j+1)
        y2 = px(i+1,j+1)
        
        return self.bilinear_interpolation(wh, angle, [x1,x2,y1,y2])/100.0
    
    def ChamferFootprint(self):
        self.module = pcbnew.MODULE(None)   # Create new module
        # TODO self.module.SetPosition()

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
        a = max(cut-self.width*m.tan(self.angle/2),w/2)

        # Distance between points 3 and 4
        x34 = a*m.sin(self.angle)
        y34 = a*m.cos(self.angle)

        # Distance between points 4 and 5
        x45 = self.width*m.cos(self.angle)
        y45 = self.width*m.sin(self.angle)

        #   1  2
        # 8 +--+
        #   |  |3
        # 7 \  --+ 4
        #    \   |
        #     \--+ 5
        #     6

        points = [
                (0,0),
                (w,0),
                (w,a),
                (w+x34,a+y34),
                (w+x34-x45,a+y34+y45),
                (cut*m.sin(self.angle),a+self.width*m.tan(self.angle/2)+cut*m.cos(self.angle)),
                (0,a+self.width*m.tan(self.angle/2)-cut),
                (0,0)]

        # Last two points can be equal
        if points[-2] == points[-1]:
            points = points[:-1]

        points = [pcbnew.wxPoint(*point) for point in points]

        self.Polygon(points, pcbnew.F_Cu)       # TODO get active layer

        # Create pads
        pad_l = self.width/10
        size_pad = pcbnew.wxSize(self.width,pad_l)
        self.module.Add(self.smdRectPad(self.module, size_pad, pcbnew.wxPoint(self.width/2, -pad_l/2), "1", 0))
        size_pad = pcbnew.wxSize(pad_l,self.width)

        # Halfway between points 4 and 5
        posx = ((w+x34) + (w+x34-x45))/2
        posy = ((a+y34) + (a+y34+y45))/2

        # Position pad so that pad edge touches polygon edge
        posx += (pad_l/2)*m.sin(self.angle)
        posy += (pad_l/2)*m.cos(self.angle)
        size_pad = pcbnew.wxSize(pad_l, self.width)
        self.module.Add(self.smdRectPad(self.module, size_pad, pcbnew.wxPoint(posx, posy), "2", (self.angle_deg-90)*10))

        if self.layer == 31: self.module.Flip(self.module.GetCenter())

        # Add to Pcbnew
        pcbnew.GetBoard().Add(self.module)
        pcbnew.Refresh()
