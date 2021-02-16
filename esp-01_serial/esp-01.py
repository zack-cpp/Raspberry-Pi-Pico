from machine import Pin, UART
import utime

#initiate UART1
uart1 = UART(1, baudrate=9600, bits=8, parity=None, stop=1, tx=Pin(8), rx=Pin(5))

#initiate PIN
led = Pin(15, Pin.OUT)

def readUART(uart):
    rawData = ""
    data = ""
    while uart.any():
        rawData = uart.readline()
    if rawData != "":
        for i in range(0, len(rawData)-1):
            data = data + chr(rawData[i])
    return data

while True:
    data = readUART(uart1)
    if data == "LEDON":
        led.value(1)
        print(data)
    elif data == "LEDOFF":
        led.value(0)
        print(data)
    utime.sleep_ms(50)
