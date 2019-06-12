class Robot:
    x = None
    y = None
    conX = None
    conY = None
    box = None

    def __init__(self, x, y,conX,conY, box):
        self.x = x
        self.y = y
        self.conX = conX
        self.conY = conY
        self.box = box