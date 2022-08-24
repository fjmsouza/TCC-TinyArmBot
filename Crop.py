import cv2

def croppingSections(frame):
    # 6 CROPS
    # [height0 : height1, width0 : width1]
    frame_led_sec_cropped = frame[245:250, 548:555]
    frame_led_bat_cropped = frame[296:303, 555:565]
    frame_led_wait_cropped = frame[328:334, 560:569]
    frame_led_free_cropped = frame[362:369, 566:575]
    frame_display_cropped = frame[110:210, 110:535]
    frame_lcd_cropped = frame[385:435, 42:142]
    return [frame_led_sec_cropped, frame_led_bat_cropped, frame_led_wait_cropped, frame_led_free_cropped, frame_display_cropped, frame_lcd_cropped]