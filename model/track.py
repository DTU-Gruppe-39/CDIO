from model import corner
from model import goal
from model import boundary


class Track:
    topRightCorner = corner.Corner
    topLeftCorner = corner.Corner
    bottomRightCorner = corner.Corner
    bottomLeftCorner = corner.Corner
    bigGoal = goal.Goal
    smallGoal = goal.Goal
    boundary = boundary.Boundary

    def __init__(self, topRightCorner, topLeftCorner, bottomRightCorner, bottomLeftCorner, bigGoal, smallGoal, boundary):
        self.topRightCorner = topRightCorner
        self.topLeftCorner = topLeftCorner
        self.bottomRightCorner = bottomRightCorner
        self.bottomLeftCorner = bottomLeftCorner
        self.bigGoal = bigGoal
        self.smallGoal = smallGoal
        self.boundary = boundary