# Import packages
import cv2
from easygui import fileopenbox
import Crop
import Rectify

#selecionar figura/ logo vai ser substituído por snapshot da camera
path_open = fileopenbox(title="choose a picture", multiple=False)
frame = cv2.imread(path_open)

frame_display_cropped, frame_led_sec_cropped, frame_led_bat_cropped, frame_led_wait_cropped, frame_led_free_cropped, frame_lcd_cropped = Crop.croppingSections(frame)

frame_display_rectified = Rectify.rectify(frame_display_cropped,600, 200)
frame_led_sec_rectified = Rectify.rectify(frame_led_sec_cropped,50, 50)
frame_led_bat_rectified = Rectify.rectify(frame_led_bat_cropped,50, 50)
frame_led_wait_rectified = Rectify.rectify(frame_led_wait_cropped,50, 50)
frame_led_free_rectified = Rectify.rectify(frame_led_free_cropped,50, 50)
frame_lcd_rectified = Rectify.rectify(frame_lcd_cropped,100, 300)

cv2.imwrite('Resources\Output\display.jpg', frame_display_rectified)
cv2.imwrite('Resources\Output\led1.jpg', frame_led_sec_rectified)
cv2.imwrite('Resources\Output\led2.jpg', frame_led_bat_rectified)
cv2.imwrite('Resources\Output\led3.jpg', frame_led_wait_rectified)
cv2.imwrite('Resources\Output\led4.jpg', frame_led_free_rectified)
cv2.imwrite('Resources\Output\lcd.jpg', frame_lcd_rectified)



print("pronto! ")
