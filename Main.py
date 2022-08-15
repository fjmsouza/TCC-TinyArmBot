# Import packages
import cv2
from easygui import fileopenbox
import Rectify
import StatusLeds

# selecionar figura(luz_artificial2 opencv_frame_23.png... logo vai ser substituído por snapshot da camera
path_open = fileopenbox(title="choose a picture", multiple=False)
frame = cv2.imread(path_open)

# 6 CROPS
# [height0 : height1, width0 : width1]
frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
frame_display_cropped = frame_gray[110:210, 110:535]
frame_led_sec_cropped = frame_gray[245:250, 548:555]
frame_led_bat_cropped = frame_gray[296:303, 555:565]
frame_led_wait_cropped = frame_gray[328:334, 560:569]
frame_led_free_cropped = frame_gray[362:369, 566:575]
frame_lcd_cropped = frame_gray[385:435, 42:142]

# 2 RECTIFIES
frame_display_rectified = Rectify.rectify(frame_display_cropped, 600, 200)
frame_lcd_rectified = Rectify.rectify(frame_lcd_cropped, 100, 300)

cv2.imwrite('Resources\Output\display.jpg', frame_display_rectified)
cv2.imwrite('Resources\Output\led1.jpg', frame_led_sec_cropped)
cv2.imwrite('Resources\Output\led2.jpg', frame_led_bat_cropped)
cv2.imwrite('Resources\Output\led3.jpg', frame_led_wait_cropped)
cv2.imwrite('Resources\Output\led4.jpg', frame_led_free_cropped)
cv2.imwrite('Resources\Output\lcd.jpg', frame_lcd_rectified)


# STATUS LEDS:
STATUS_LED_SEC = StatusLeds.statusLeds(frame_led_sec_cropped)
STATUS_LED_BAT = StatusLeds.statusLeds(frame_led_bat_cropped)
STATUS_LED_WAIT = StatusLeds.statusLeds(frame_led_wait_cropped)
STATUS_LED_FREE = StatusLeds.statusLeds(frame_led_free_cropped)

print(STATUS_LED_SEC, STATUS_LED_BAT, STATUS_LED_WAIT, STATUS_LED_FREE)

print("pronto! ")
