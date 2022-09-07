import cv2
import numpy as np


def checkSum(frame):
    accumulator = np.matrix(frame).sum()
    return accumulator


def preprocess(frame1,frame2):
    blur1 = cv2.GaussianBlur(src=frame1, ksize=(5, 5), sigmaX=0)
    blur2 = cv2.GaussianBlur(src=frame2, ksize=(5, 5), sigmaX=0)
    # calculate difference and update previous frame
    diff_frame = cv2.absdiff(src1=blur1, src2=blur2)
    # cv2.imshow("diff ", diff_frame)

    # 4. Dilute the image a bit to make differences more seeable; more suitable for contour detection
    kernel = np.ones((5, 5))
    diff_frame = cv2.dilate(diff_frame, kernel, 3)
    # cv2.imshow("diff + dilate ", diff_frame)

    # 5. Only take different areas that are different enough (>20 / 255)
    thresh_diff_frame = cv2.threshold(src=diff_frame, thresh=5, maxval=255, type=cv2.THRESH_BINARY)[1]

    return thresh_diff_frame


def changed(frame1, frame2):
    thresh_diff_frame = preprocess(frame1,frame2)
    cv2.imwrite("thresh_diff_frame.jpg",thresh_diff_frame)
    checksum = checkSum(thresh_diff_frame)

    if checksum > 1000:
        print("algo mudou ...checksum:", checksum)
        return True

    else:
        print("nada mudou ...checksum:", checksum)
        return False
