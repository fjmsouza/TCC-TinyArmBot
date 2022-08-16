import cv2
import numpy as np

def execute(frame):

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)
    # frame = cv2.bilateralFilter(frame, 20, 50, 50)

    return frame
