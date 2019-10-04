
import numbers
import math as m
import collections
from fractions import Fraction


import numbers
import math as m
import collections
from fractions import Fraction


def spread(start, end, count, mode=1):
    """
    spread(start, end, count [, mode]) -> generator

    Yield a sequence of evenly-spaced numbers between start and end.

    The range start...end is divided into count evenly-spaced (or as close to
    evenly-spaced as possible) intervals. The end-points of each interval are
    then yielded, optionally including or excluding start and end themselves.
    By default, start is included and end is excluded.

    For example, with start=0, end=2.1 and count=3, the range is divided into
    three intervals:

        (0.0)-----(0.7)-----(1.4)-----(2.1)

    resulting in:

        >>> list(spread(0.0, 2.1, 3))
        [0.0, 0.7, 1.4]

    Optional argument mode controls whether spread() includes the start and
    end values. mode must be an int. Bit zero of mode controls whether start
    is included (on) or excluded (off); bit one does the same for end. Hence:

        0 -> open interval (start and end both excluded)
        1 -> half-open (start included, end excluded)
        2 -> half open (start excluded, end included)
        3 -> closed (start and end both included)

    By default, mode=1 and only start is included in the output.

    (Note: depending on mode, the number of values returned can be count,
    count-1 or count+1).
    """
    if not isinstance(mode, int):
        raise TypeError('mode must be an int')
    if count != int(count):
        raise ValueError('count must be an integer')
    if count <= 0:
        raise ValueError('count must be positive')
    if mode & 1:
        yield start
    width = Fraction(end-start)
    start = Fraction(start)
    for i in range(1, count):
        yield float(start + i*width/count)
    if mode & 2:
        yield end


class Linear:
    """
    Class for common linear algebra functions.
    """
    @staticmethod
    def multiplyConstant(v, c):
        return [x * c for x in v]
    
    @staticmethod
    def multiplyFloat(v, f):
        return [float(x) * f for x in v]

    @staticmethod
    def addMatrix(v, w):
        # return [[v[i][j]+w[i][j] for j in range(len(w[0]))] for i in range(len(v))]
        return [x + y for x, y in zip(v, w)]

    @staticmethod
    def multiplyMatrix(v, w):
        return [sum(v[i][j]*w[j] for j in range(len(w))) for i in range(len(v))]
    
    @staticmethod
    def dot(v, w):
        if len(v) != len(w): return 0
        return sum(i[0] * i[1] for i in zip(v, w))

    @staticmethod
    def transposeMatrix(m):
        return map(list,zip(*m))
    
    @staticmethod
    def getMatrixMinor(m,i,j):
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

    @staticmethod
    def getMatrixDeterminant(m):
        # Base case for 2x2 matrix
        if len(m) == 2:
            return m[0][0]*m[1][1]-m[0][1]*m[1][0]

        determinant = 0
        for c in range(len(m)):
            determinant += ((-1)**c)*m[0][c]*getMatrixDeterminant(getMatrixMinor(m,0,c))
        return determinant

    @staticmethod
    def getMatrixInverse(m):
        determinant = getMatrixDeterminant(m)
        # Special case for 2x2 matrix:
        if len(m) == 2:
            return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                    [-1*m[1][0]/determinant, m[0][0]/determinant]]

        # Find matrix of cofactors
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = getMatrixMinor(m,r,c)
                cofactorRow.append(((-1)**(r+c)) * getMatrixDeterminant(minor))
            cofactors.append(cofactorRow)
        cofactors = transposeMatrix(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c]/determinant
        return cofactors

class Vector:
    """
    Class for common mathematical vector operations.
    """
    @staticmethod
    def vector_intersect(v, w, v0, w0):
        '''
        Return the intersection point, i.e. wxPoint, of two line vectors, v and w,
        that have starting positions v0 and w0, respectively.
        '''
        A = [Linear.multiplyFloat([v.x, v.y], 1e-6), Linear.multiplyFloat([-w.x, -w.y], 1e-6)]
        B = Linear.multiplyFloat([(w0.x - v0.x), (w0.y - v0.y)], 1e-6)
        AT = Linear.getMatrixInverse(A)
        x = Linear.multiplyMatrix(AT, B)
        vt = Linear.multiplyFloat(Linear.multiplyFloat(A[0], x[0]), 1e6)
        return pcbnew.wxPoint(vt[0], vt[1]) + v0

    @staticmethod
    def get_vector(p0, p1):
        '''Constructs a vector from p0 to p1, both wxPoints.'''
        return pcbnew.wxPoint((p1.x - p0.x), (p1.y - p0.y))

    @staticmethod
    def get_vector_magnitude(v):
        '''Returns the magnitude of a given wxPoint vector.'''
        return m.sqrt(v.x**2 + v.y**2)
    
    @staticmethod
    def get_vector_angle(v):
        '''Returns the angle of a given wxPoint vector in radians.'''
        return m.acos(v.x/v.y)
    
    @staticmethod
    def get_vectors_angle(v, w):
        '''Returns the angle between two wxPoint-defined vectors in radions.'''
        return m.acos((Linear.dot(v, w))/(Vector.get_vector_magnitude(v) * Vector.get_vector_magnitude(w)))

    @staticmethod
    def get_point_on_vline(v, v0, d):
        '''Returns the point along a vector line defined by distance d from v0.'''
        return pcbnew.wxPoint(v.x * d, v.y * d) + v0
