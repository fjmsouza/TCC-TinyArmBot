# Import packages
import Crop
import MoveTinyArm
import StatusLeds
import FingerPrints
import TakePicture
import time


class DeskTerminalTest:

    def __init__(self):
        self.frame = TakePicture.takeGrayPicture()
        self.frame_led_sec_cropped = None
        self.frame_led_bat_cropped = None
        self.frame_led_wait_cropped = None
        self.frame_led_free_cropped = None
        self.frame_display_cropped = None
        self.frame_lcd_cropped = None
        self.frame_fp = None

        self.cropped_sections = (self.frame_led_sec_cropped, self.frame_led_bat_cropped, self.frame_led_wait_cropped,
                                 self.frame_led_free_cropped, self.frame_display_cropped, self.frame_lcd_cropped)
        self.status_leds = False, False, False, False
        self.status_display = None
        self.status_lcd = None

    def crop(self):
        self.cropped_sections = Crop.croppingSections(self.frame)
        return self.cropped_sections

    def statusLeds(self):
        self.status_leds = StatusLeds.status4Leds(self.cropped_sections)
        return self.status_leds

    def fingerPrint(self, frame):
        self.frame_fp = FingerPrints.execute(frame)
        return self.frame_fp

    def terminalInstantState(self):
        # GENERATE 6 CROPS
        self.cropped_sections = self.crop()

        # STATE OF 4 LEDS:
        self.status_leds = self.statusLeds()

        # STATE OF SCREEN ("FINGERPRINT")
        self.status_lcd = self.fingerPrint(self.frame_lcd_cropped)
        self.status_display = self.fingerPrint(self.frame_display_cropped)


estado1 = True, True, True, True
estado2 = True, False, False, False
estado3 = True, False, False, False
cropped_sections = [None, None, None, None, None, None, ]
frame_display_cropped = cropped_sections[4]
frame_lcd_cropped = cropped_sections[5]

while True:
    start = input("type 's' to start the test:")
    start = start.lower()
    if start == 's':

        general_status = "1"

        if general_status == '1':
            status_x = DeskTerminalTest()
            status_x.terminalInstantState()
            if status_x.status_leds == estado1:
                MoveTinyArm.moveTo("C")
                time.sleep(2)
                general_status = '2'
            else:
                general_status = 'error'
                print("Test leds Fail!")
        elif general_status == '2':
            status_x = DeskTerminalTest()
            status_x.terminalInstantState()
            if status_x.status_leds == estado2:
                MoveTinyArm.moveTo("C")
                time.sleep(2)
                general_status = '3'
            else:
                general_status = 'error'
                print("Test leds Fail!")
        elif general_status == '3':
            status_x = DeskTerminalTest()
            status_x.terminalInstantState()
            if status_x.status_leds == estado3:
                MoveTinyArm.moveTo("C")
                time.sleep(2)
                general_status = '4'
            else:
                general_status = 'error'
                print("Test leds Fail!")
        elif general_status == '4':
            status_y = DeskTerminalTest()
            status_y.terminalInstantState()
            if status_x.status_lcd != status_y.status_lcd:
                MoveTinyArm.moveTo("C")
                time.sleep(2)
                status_x = DeskTerminalTest()
                status_x.terminalInstantState()
                MoveTinyArm.moveTo("1")
                time.sleep(2)
                general_status = '5'
            else:
                general_status = 'error'
                print("Test LCD Fail!")
        elif general_status == '5':
            status_y = DeskTerminalTest()
            status_y.terminalInstantState()
            if status_x.status_display != status_y.status_display:
                MoveTinyArm.moveTo("2")
                time.sleep(2)
                general_status = '6'
            else:
                general_status = 'error'
                print("Test key 1 Fail!")
        elif general_status == '6':
            status_x = DeskTerminalTest()
            status_x.terminalInstantState()
            if status_x.status_display != status_y.status_display:
                MoveTinyArm.moveTo("3")
                time.sleep(2)
                general_status = '7'
            else:
                general_status = 'error'
                print("Test key 2 Fail!")
        elif general_status == '7':
            status_y = DeskTerminalTest()
            status_y.terminalInstantState()
            if status_x.status_display != status_y.status_display:
                MoveTinyArm.moveTo("4")
                time.sleep(2)
                general_status = '8'
            else:
                general_status = 'error'
                print("Test key 3 Fail!")

        elif general_status == '8':
            status_x = DeskTerminalTest()
            status_x.terminalInstantState()
            if status_x.status_display != status_y.status_display:
                MoveTinyArm.moveTo("5")
                time.sleep(2)
                general_status = '9'
            else:
                general_status = 'error'
                print("Test key 5 Fail!")
        elif general_status == '9':
            status_y = DeskTerminalTest()
            status_y.terminalInstantState()
            if status_x.status_display != status_y.status_display:
                MoveTinyArm.moveTo("6")
                time.sleep(2)
                general_status = '10'
            else:
                general_status = 'error'
                print("Test key 6 Fail!")
        elif general_status == '10':
            status_x = DeskTerminalTest()
            status_x.terminalInstantState()
            if status_x.status_display != status_y.status_display:
                MoveTinyArm.moveTo("7")
                time.sleep(2)
                general_status = '11'
            else:
                general_status = 'error'
                print("Test key 7 Fail!")
        elif general_status == '11':
            status_y = DeskTerminalTest()
            status_y.terminalInstantState()
            if status_x.status_display != status_y.status_display:
                MoveTinyArm.moveTo("8")
                time.sleep(2)
                general_status = '12'
            else:
                general_status = 'error'
                print("Test key 8 Fail!")
        elif general_status == '12':
            status_x = DeskTerminalTest()
            status_x.terminalInstantState()
            if status_x.status_display != status_y.status_display:
                MoveTinyArm.moveTo("9")
                time.sleep(2)
                general_status = '13'
            else:
                general_status = 'error'
                print("Test key 1 Fail!")
        elif general_status == '13':
            status_y = DeskTerminalTest()
            status_y.terminalInstantState()
            if status_x.status_display != status_y.status_display:
                MoveTinyArm.moveTo("G")
                time.sleep(2)
                general_status = '14'
            else:
                general_status = 'error'
                print("Test key 1 Fail!")
        elif general_status == '14':
            status_x = DeskTerminalTest()
            status_x.terminalInstantState()
            if status_x.status_display != status_y.status_display:
                MoveTinyArm.moveTo("0")
                time.sleep(2)
                general_status = '15'
            else:
                general_status = 'error'
                print("Test key 1 Fail!")
        elif general_status == '15':
            status_y = DeskTerminalTest()
            status_y.terminalInstantState()
            if status_x.status_display != status_y.status_display:
                MoveTinyArm.moveTo("C")
                time.sleep(2)
            else:
                general_status = 'error'
                print("Test key 1 Fail!")
        elif general_status == 'error':
            print("Final Result: Test Fail!")

        else:
            print("Successful Test!")
