
from re import match

def Vent(ventStr):
    m = match('(\d+),(\d+) -> (\d+),(\d+)', ventStr)
    if m :
        start = (int(m.group(1)), int(m.group(2)))
        end = (int(m.group(3)), int(m.group(4)))
        
        axisAligned = start[0] == end[0] or start[1] == end[1]
        
        if axisAligned:
            return AxisAlignedVent(start, end)
        else:
            return EvenDiagonalVent(start, end)
    else:
        raise ValueError

class AxisAlignedVent:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.alignedAxis = 0 if start[0] == end[0] else 1
        
    def GetPoints(self):
        if self.alignedAxis == 0:
            step = 1 if self.end[1] > self.start[1] else -1
            return ((self.start[0] , i) for i in range(self.start[1], self.end[1] + step, step))
        else:
            step = 1 if self.end[0] > self.start[0] else -1
            return ((i, self.start[1]) for i in range(self.start[0], self.end[0] + step, step))
    
class EvenDiagonalVent:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def GetPoints(self):
        xStep = 1 if self.end[0] > self.start[0] else -1
        yStep = 1 if self.end[1] > self.start[1] else -1
        return ((self.start[0] + xStep * i, self.start[1] + yStep * i) for i in range(0, abs(self.end[0] - self.start[0]) + 1))