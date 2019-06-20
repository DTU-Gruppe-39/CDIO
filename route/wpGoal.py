import dao.singleton as singleton
from model import point

# if True: move to right goal
# if False: move to left goal
def getWpGoal(direction):
    track = singleton.Singleton.track

    #False is left goal
    if direction == False:
        if track.bigGoal.x > track.smallGoal.x:
            wpGoal = point.Point(track.bigGoal.x - round(track.pixelConversion*35), track.bigGoal.y)
        elif track.bigGoal.x < track.smallGoal.x:
            wpGoal = (track.bigGoal.x + round(track.pixelConversion*35), track.bigGoal.y)
    # True is right goal
    elif direction == True:
        if track.bigGoal.x > track.smallGoal.x:
            wpGoal = point.Point(track.smallGoal.x + round(track.pixelConversion*35), track.smallGoal.y)
        elif track.bigGoal.x < track.smallGoal.x:
            wpGoal = point.Point(track.smallGoal.x - round(track.pixelConversion*35), track.smallGoal.y)

    return wpGoal
