import cv2

def statusLeds(frame,threshold = 0):

    frame_mean = cv2.GaussianBlur(frame_gray, (7, 7), -1)
    # frame_thres = cv2.adaptiveThreshold(frame_mean, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 5)
    ret, frame_thres = cv2.threshold(frame_mean, threshold, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    if frame_thres[3,3] == 255:
        return True
    else:
        return False
