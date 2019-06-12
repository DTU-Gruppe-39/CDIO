class Robot:
    centrumX = None
    centrumY = None
    blSquareX = None
    blSquareY = None
    box = None

    def __init__(self, x, y,conX,conY, box):
        self.centrumX = x
        self.centrumY = y
        self.blSquareX = conX
        self.blSquareY = conY
        self.box = box
