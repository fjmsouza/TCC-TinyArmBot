import cv2
import numpy as np


class Morphology:
    def __init__(self, frame):
        self.frame = frame

    def erode(self, c, d, iterations):
        kernel = np.ones((int(c), int(d)), np.uint8)
        erode = cv2.erode(self.frame, kernel, iterations)

        return erode

    def dilate(self, c, d, iterations):
        kernel = np.ones((int(c), int(d)), np.uint8)
        dilate = cv2.dilate(self.frame, kernel, iterations)

        return dilate

    def gradient(self, c, d):
        kernel = np.ones((int(c), int(d)), np.uint8)
        gradient = cv2.morphologyEx(self.frame, cv2.MORPH_GRADIENT, kernel)

        return gradient

    def open(self, c, d):
        kernel = np.ones((int(c), int(d)), np.uint8)
        opened = cv2.morphologyEx(self.frame, cv2.MORPH_OPEN, kernel)

        return opened

    def close(self, c, d):
        kernel = np.ones((int(c), int(d)), np.uint8)
        close = cv2.morphologyEx(self.frame, cv2.MORPH_CLOSE, kernel)

        return close
