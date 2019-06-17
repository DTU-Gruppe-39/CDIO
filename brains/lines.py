from shapely.geometry import LineString
from model.point import Point
from model import obstacle


def getPointFromTwoLines(l1, l2):
    line1 = l1
    line2 = l2

    p = line1.intersection(line2)

    intersection = Point(p.x, p.y)

    return intersection


def areLineTouchingObstacleSquare(line):
    if areLinesTouching(line, obstacle.right_line) or \
    areLinesTouching(line, obstacle.left_line) or \
    areLinesTouching(line, obstacle.top_line) or \
    areLinesTouching(line, obstacle.bottom_line):
        return True
    else:
        return False


def areLinesTouching(l1, l2):

    line1 = l1
    line2 = l2

    bool = line1.touches(line2)

    return bool


#------ Old methods that take points instead of lines ------#

# def getPointFromTwoLines(p1, p2, p3, p4):
#     line1 = LineString([(p1[0], p1[1]), (p2[0],  p2[1])])
#     line2 = LineString([(p3[0], p3[1]), (p4[0],  p4[1])])
#
#     p = line1.intersection(line2)
#
#     intersection = Point(p.x, p.y)
#
#     return intersection


# def areLinesTouching(p1, p2, p3, p4):
#
#     line1 = LineString([(p1[0], p1[1]), (p2[0], p2[1])])
#     line2 = LineString([(p3[0], p3[1]), (p4[0], p4[1])])
#
#     bool = line1.touches(line2)
#
#     return bool