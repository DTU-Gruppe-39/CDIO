class Obstacle:
    center_x = None
    center_y = None
    right_line = None
    left_line = None
    top_line = None
    bottom_line = None
    square_top_left_corner = None
    square_top_right_corner = None
    square_bottom_left_corner = None
    square_bottom_right_corner = None

    def __init__(self, center_x, center_y, right_line, left_line, top_line, bottom_line, square_top_left_corner, square_top_right_corner, square_bottom_left_corner, square_bottom_right_corner):
        self.center_x = center_x
        self.center_y = center_y
        self.right_line = right_line
        self.left_line = left_line
        self.top_line = top_line
        self.bottom_line = bottom_line
        self.square_top_left_corner = square_top_left_corner
        self.square_top_right_corner = square_top_right_corner
        self.square_bottom_left_corner = square_bottom_left_corner
        self.square_bottom_right_corner = square_bottom_right_corner
