# Import packages
import cv2

img = cv2.imread('5.jpg')
print(img.shape) # Print image shape
cv2.imshow("ui",img)
#
# # Cropping an image
# frame_display = img[466:286, 1329:468]
# frame_leds = img[1202:530, 1502:853]
# frame_lcd = img[539:678, 271:1019]
#
#
# # Display cropped image
# cv2.imshow("display", frame_display)
# cv2.imshow("leds", frame_leds)
# cv2.imshow("lcd", frame_lcd)
#
# # Save the cropped image
# cv2.imwrite("display.jpg", frame_display)
# cv2.imwrite("leds.jpg", frame_leds)
# cv2.imwrite("lcd.jpg", frame_lcd)
#
cv2.waitKey(0)
cv2.destroyAllWindows()