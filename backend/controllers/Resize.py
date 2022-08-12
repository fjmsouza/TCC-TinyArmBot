import cv2


class Resize:
    def __init__(self, frame):
        self.frame = frame

    def resize(self, resize):
        image_height, image_width, channels = self.frame.shape

        new_width = int(image_width * (int(resize) / 100))
        new_height = int(image_height * (int(resize) / 100))
        new_size = (new_width, new_height)
        resized = cv2.resize(self.frame, new_size)

        return resized
