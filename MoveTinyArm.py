import serial

def moveTo(key):

    try:
        ser = serial.Serial()  # open serial port
        ser.baudrate = 9600
        ser.port = 'COM3'
        ser.open()
        print("serial opened!")
        key = 'b'+ key
        ser.write(key)
    except:
        print("error to open serial port!")
    ser.close()             # close port