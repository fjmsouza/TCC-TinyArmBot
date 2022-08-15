import cv2

def statusLeds(frame,threshold = 100):

    frame_mean = cv2.blur(frame, (3, 3), borderType=cv2.BORDER_REFLECT)
    ret, frame_thres = cv2.threshold(frame_mean, threshold, 255, cv2.THRESH_BINARY)
    width, height = frame_thres.shape
    width_center = int(width/2)
    height_center = int(height/2)
    if frame_thres[width_center,height_center] == 255:
        return True
    else:
        return False
