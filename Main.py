# Import packages
import Crop
import MoveTinyArm
import StatusLeds
import StatusScreen
import TakePicture
import time


def startDeskTerminalTest(general_status):
    if general_status == '1':
        status_x = DeskTerminalTest()
        status_x.terminalInstantState()
        if status_x.status_leds == estado1:
            # MoveTinyArm.moveTo("C")
            time.sleep(2)
            general_status = '2'
            print("Test leds ok!")
        else:
            general_status = 'error'
            print("Test leds Fail!")
    if general_status == '2':
        status_x = DeskTerminalTest()
        status_x.terminalInstantState()
        if status_x.status_leds == estado2:
            # MoveTinyArm.moveTo("C")
            time.sleep(2)
            general_status = '3'
            print("Test leds ok!")
        else:
            general_status = 'error'
            print("Test leds Fail!")
    if general_status == '3':
        status_x = DeskTerminalTest()
        status_x.terminalInstantState()
        if status_x.status_leds == estado3:
            # MoveTinyArm.moveTo("C")
            time.sleep(2)
            general_status = '4'
            print("Test leds ok!")
        else:
            general_status = 'error'
            print("Test leds Fail!")
    if general_status == '4':
        status_y = DeskTerminalTest()
        status_y.terminalInstantState()
        if status_x.status_lcd != status_y.status_lcd:
            # MoveTinyArm.moveTo("C")
            time.sleep(2)
            # MoveTinyArm.moveTo("1")
            time.sleep(2)
            general_status = '5'
            print("Test lcd ok!")
        else:
            general_status = 'error'
            print("Test LCD Fail!")
    if general_status == '5':
        status_y = DeskTerminalTest()
        status_y.terminalInstantState()
        if status_x.status_display != status_y.status_display:
            # MoveTinyArm.moveTo("2")
            time.sleep(2)
            general_status = '6'
            print("Test key 1 ok!")
        else:
            general_status = 'error'
            print("Test key 1 Fail!")
    if general_status == '6':
        status_x = DeskTerminalTest()
        status_x.terminalInstantState()
        if status_x.status_display != status_y.status_display:
            # MoveTinyArm.moveTo("3")
            time.sleep(2)
            general_status = '7'
            print("Test key 2 ok!")
        else:
            general_status = 'error'
            print("Test key 2 Fail!")
    if general_status == '7':
        status_y = DeskTerminalTest()
        status_y.terminalInstantState()
        if status_x.status_display != status_y.status_display:
            # MoveTinyArm.moveTo("4")
            time.sleep(2)
            general_status = '8'
            print("Test key 3 ok!")
        else:
            general_status = 'error'
            print("Test key 3 Fail!")

    if general_status == '8':
        status_x = DeskTerminalTest()
        status_x.terminalInstantState()
        if status_x.status_display != status_y.status_display:
            # MoveTinyArm.moveTo("5")
            time.sleep(2)
            general_status = '9'
            print("Test key 4 ok!")
        else:
            general_status = 'error'
            print("Test key 4 Fail!")
    if general_status == '9':
        status_y = DeskTerminalTest()
        status_y.terminalInstantState()
        if status_x.status_display != status_y.status_display:
            # MoveTinyArm.moveTo("6")
            time.sleep(2)
            general_status = '10'
            print("Test key 5 ok!")
        else:
            general_status = 'error'
            print("Test key 5 Fail!")
    if general_status == '10':
        status_x = DeskTerminalTest()
        status_x.terminalInstantState()
        if status_x.status_display != status_y.status_display:
            # MoveTinyArm.moveTo("7")
            time.sleep(2)
            general_status = '11'
            print("Test key 6 ok!")
        else:
            general_status = 'error'
            print("Test key 6 Fail!")
    if general_status == '11':
        status_y = DeskTerminalTest()
        status_y.terminalInstantState()
        if status_x.status_display != status_y.status_display:
            # MoveTinyArm.moveTo("8")
            time.sleep(2)
            general_status = '12'
            print("Test key 7 ok!")
        else:
            general_status = 'error'
            print("Test key 7 Fail!")
    if general_status == '12':
        status_x = DeskTerminalTest()
        status_x.terminalInstantState()
        if status_x.status_display != status_y.status_display:
            # MoveTinyArm.moveTo("9")
            time.sleep(2)
            general_status = '13'
            print("Test key 8 ok!")
        else:
            general_status = 'error'
            print("Test key 8 Fail!")
    if general_status == '13':
        status_y = DeskTerminalTest()
        status_y.terminalInstantState()
        if status_x.status_display != status_y.status_display:
            # MoveTinyArm.moveTo("G")
            time.sleep(2)
            general_status = '14'
            print("Test key 9 ok!")
        else:
            general_status = 'error'
            print("Test key 9 Fail!")
    if general_status == '14':
        status_x = DeskTerminalTest()
        status_x.terminalInstantState()
        if status_x.status_display != status_y.status_display:
            # MoveTinyArm.moveTo("0")
            time.sleep(2)
            general_status = '15'
            print("Test key CORRIGE ok!")
        else:
            general_status = 'error'
            print("Test key CORRIGE Fail!")
    if general_status == '15':
        status_y = DeskTerminalTest()
        status_y.terminalInstantState()
        if status_x.status_display != status_y.status_display:
            # MoveTinyArm.moveTo("C")
            time.sleep(2)
            print("Test key 0 ok!")
            general_status = '16'
        else:
            general_status = 'error'
            print("Test key 0 Fail!")
    if general_status == '16':
        status_x = DeskTerminalTest()
        status_x.terminalInstantState()
        if status_x.status_display != status_y.status_display:
            time.sleep(2)
            print("Test key CONFIRMA ok!")
        else:
            general_status = 'error'
            print("Test key CONFIRMA Fail!")
    if general_status == 'error':
        print("Final Result: Test Fail!")

    else:
        print("Successful Test!")


class DeskTerminalTest:

    def __init__(self):
        self.frame = TakePicture.takeGrayPicture()

        self.status_screen = None

        self.cropped_sections = [None, None, None, None, None, None, ]
        self.frame_led_sec_cropped = self.cropped_sections[0]
        self.frame_led_bat_cropped = self.cropped_sections[1]
        self.frame_led_wait_cropped = self.cropped_sections[2]
        self.frame_led_free_cropped = self.cropped_sections[3]
        self.frame_display_cropped = self.cropped_sections[4]
        self.frame_lcd_cropped = self.cropped_sections[5]

        self.status_leds = False, False, False, False
        self.status_display = None
        self.status_lcd = None

    def crop(self):
        self.cropped_sections = Crop.croppingSections(self.frame)
        return self.cropped_sections

    def statusLeds(self):
        self.status_leds = StatusLeds.execute(self.cropped_sections)
        return self.status_leds

    def statusScreen(self, frame):
        self.status_screen = StatusScreen.execute(frame)
        return self.status_screen

    def terminalInstantState(self):
        # GENERATE 6 CROPS
        self.cropped_sections = self.crop()

        # STATE OF 4 LEDS:
        self.status_leds = self.statusLeds()

        # STATE OF SCREEN ("FINGERPRINT")
        self.status_lcd = self.statusScreen(self.cropped_sections[5])
        self.status_display = self.statusScreen(self.cropped_sections[4])


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
        general_status = '1'
        startDeskTerminalTest(general_status)
