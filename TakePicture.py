import cv2
from easygui import fileopenbox

def takeGrayPicture():
    # selecionar figura(luz_artificial2 opencv_frame_23.png... logo vai ser substituído por snapshot da camera
    path_open = fileopenbox(title="choose a picture", multiple=False)
    frame = cv2.imread(path_open)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return frame