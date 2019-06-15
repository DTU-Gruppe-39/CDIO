class Robot:
    centrumX = None
    centrumY = None
    blSquareX = None
    blSquareY = None
    box = None
    numberOfTries = None

    def __init__(self, x, y,conX,conY, box, numberOfTries):
        self.centrumX = x
        self.centrumY = y
        self.blSquareX = conX
        self.blSquareY = conY
        self.box = box
        self.numberOfTries = numberOfTries
