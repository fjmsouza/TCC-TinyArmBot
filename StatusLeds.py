import cv2

def statusSecLed(frame,threshold = 130):

    frame_mean = cv2.blur(frame, (3, 3), borderType=cv2.BORDER_REFLECT)
    # print(frame_mean[2,2])
    _, frame_thres = cv2.threshold(frame_mean, threshold, 255, cv2.THRESH_BINARY)
    width, height = frame_thres.shape
    width_center = int(width/2)
    height_center = int(height/2)

    if frame_thres[width_center,height_center] == 255:
        return True
    else:
        return False
def statusBatLed(frame,threshold = 108):

    frame_mean = cv2.blur(frame, (3, 3), borderType=cv2.BORDER_REFLECT)
    # print(frame_mean[2,2])
    _, frame_thres = cv2.threshold(frame_mean, threshold, 255, cv2.THRESH_BINARY)
    width, height = frame_thres.shape
    width_center = int(width/2)
    height_center = int(height/2)

    if frame_thres[width_center,height_center] == 255:
        return True
    else:
        return False

def statusWaitLed(frame,threshold = 120):

    frame_mean = cv2.blur(frame, (3, 3), borderType=cv2.BORDER_REFLECT)
    # print(frame_mean[2,2])
    _, frame_thres = cv2.threshold(frame_mean, threshold, 255, cv2.THRESH_BINARY)
    width, height = frame_thres.shape
    width_center = int(width/2)
    height_center = int(height/2)

    if frame_thres[width_center,height_center] == 255:
        return True
    else:
        return False

def statusFreeLed(frame,threshold = 120):

    frame_mean = cv2.blur(frame, (3, 3), borderType=cv2.BORDER_REFLECT)
    # print(frame_mean[2,2])
    _, frame_thres = cv2.threshold(frame_mean, threshold, 255, cv2.THRESH_BINARY)
    width, height = frame_thres.shape
    width_center = int(width/2)
    height_center = int(height/2)

    if frame_thres[width_center,height_center] == 255:
        return True
    else:
        return False

def execute(cropped_sections):

    # cv2.imwrite("ledsec.jpg", cropped_sections[0])
    # cv2.imwrite("ledbat.jpg", cropped_sections[1])
    # cv2.imwrite("ledwait.jpg", cropped_sections[2])
    # cv2.imwrite("ledfree.jpg", cropped_sections[3])
    STATUS_LED_SEC = statusSecLed(cropped_sections[0])
    STATUS_LED_BAT = statusBatLed(cropped_sections[1])
    STATUS_LED_WAIT = statusWaitLed(cropped_sections[2])
    STATUS_LED_FREE = statusFreeLed(cropped_sections[3])
    # print(STATUS_LED_SEC, STATUS_LED_BAT, STATUS_LED_WAIT, STATUS_LED_FREE)
    return STATUS_LED_SEC, STATUS_LED_BAT, STATUS_LED_WAIT, STATUS_LED_FREE