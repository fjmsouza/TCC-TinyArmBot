
def croppingSections(frame):
    # 6 CROPS
    # [height0 : height1, width0 : width1]
    frame_led_sec_cropped = frame[290:294, 587:591]
    frame_led_bat_cropped = frame[360:364, 601:605]
    frame_led_wait_cropped = frame[406:410, 612:616]
    frame_led_free_cropped = frame[456:460, 620:624]
    frame_lcd_cropped = frame[378:382, 6:10]
    frame_display_cropped = frame[138:218, 315:538]
    return [frame_led_sec_cropped, frame_led_bat_cropped, frame_led_wait_cropped, frame_led_free_cropped, frame_lcd_cropped, frame_display_cropped]