class Obstacle:
    center_x = None
    center_y = None
    right_line = None
    left_line = None
    top_line = None
    bottom_line = None

    def __init__(self, center_x, center_y, right_line, left_line, top_line, bottom_line):
        self.center_x = center_x
        self.center_y = center_y
        self.right_line = right_line
        self.left_line = left_line
        self.top_line = top_line
        self.bottom_line = bottom_line
