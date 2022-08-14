# Import packages
import cv2
from easygui import fileopenbox
import Crop
import Rectify

path_open = fileopenbox(title="choose a picture", multiple=False)
frame = cv2.imread(path_open)

frame_display_cropped, frame_led_sec_cropped, frame_led_remainder_cropped, frame_lcd_cropped = Crop.croppingThreeSections(frame)

frame_display_rectified = Rectify.rectify(frame_display_cropped,1350, 300)
frame_led_sec_rectified = Rectify.rectify(frame_led_sec_cropped,1350, 300)
frame_led_remainder_rectified = Rectify.rectify(frame_led_remainder_cropped,300, 500)
frame_lcd_rectified = Rectify.rectify(frame_lcd_cropped,300, 500)

cv2.imwrite('display.jpg', frame_display_rectified)
cv2.imwrite('ledSec.jpg', frame_led_sec_rectified)
cv2.imwrite('ledRem.jpg', frame_led_remainder_rectified)
cv2.imwrite('lcd.jpg', frame_lcd_rectified)

print("pronto! ")
