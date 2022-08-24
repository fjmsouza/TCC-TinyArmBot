import cv2

def status1Led(frame,threshold = 100):
    frame_mean = cv2.blur(frame, (3, 3), borderType=cv2.BORDER_REFLECT)
    ret, frame_thres = cv2.threshold(frame_mean, threshold, 255, cv2.THRESH_BINARY)
    width, height = frame_thres.shape
    width_center = int(width/2)
    height_center = int(height/2)
    if frame_thres[width_center,height_center] == 255:
        return True
    else:
        return False

def execute(cropped_sections):
    STATUS_LED_SEC = status1Led(cropped_sections[0])
    STATUS_LED_BAT = status1Led(cropped_sections[1])
    STATUS_LED_WAIT = status1Led(cropped_sections[2])
    STATUS_LED_FREE = status1Led(cropped_sections[3])
    return STATUS_LED_SEC, STATUS_LED_BAT, STATUS_LED_WAIT, STATUS_LED_FREE