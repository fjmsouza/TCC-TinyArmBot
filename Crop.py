
def croppingThreeSections(frame):
    frame_display = frame[266:472, 440:1360]
    frame_led_sec = frame[500:615, 1180:1480]
    frame_led_remainder = frame[620:867, 1200:1515]
    frame_lcd = frame[678:1019, 271:539]
    return frame_display, frame_led_sec, frame_led_remainder, frame_lcd

