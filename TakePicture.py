import cv2
from easygui import fileopenbox

class ImageInit:
    def __init__(self, via_cam=True):
        self.via_cam = via_cam
        self.frame = None
        if self.via_cam:
            self.cam = cv2.VideoCapture(1 + cv2.CAP_DSHOW)
            self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.cam.set(cv2.CAP_PROP_FPS, 30)
            self.cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
            self.cam.set(cv2.CAP_PROP_BUFFERSIZE, 1);


    def flushLoadCamera(self):
        ret, self.frame = self.cam.read()
        if not ret:
            print("failed to grab frame")

        ret, self.frame = self.cam.read()
        if not ret:
            print("failed to grab frame")

    def takeGrayPicture(self):

        if self.via_cam:
            self.flushLoadCamera()
        else:
            path_open = fileopenbox(title="choose a picture", default=r"\Resources\LUZ_ARTIFICIAL4_JPG(COM SUPORTE)")
            self.frame = cv2.imread(path_open)

        try:
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        except:
            print("Please check the camera!")
            return None
        return self.frame
