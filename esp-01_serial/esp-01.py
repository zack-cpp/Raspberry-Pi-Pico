from machine import Pin, PWM, UART
from time import sleep

pwm = PWM(Pin(25))
pwm.freq(1000)

uart = UART(1, baudrate=9600, bits=8, parity=None, stop=1, tx=Pin(8), rx=Pin(5))

def uartSend(cmd):
    uart.write(cmd)

def uartRead():
    hasil = ""
    kata = ""
    while uart.any():
        kata = uart.readline()
    if kata != "":
        for i in range(0, len(kata)-1):
            hasil = hasil + chr(kata[i])
    return hasil

def fade(duty, direction):
    for i in range (8 * 256):
        duty += direction
        if duty > 255:
            duty = 255
            direction = -1
        elif duty < 0:
            duty = 0
            direction = 1
        pwm.duty_u16(duty * duty)
        sleep(0.001)

while True:
    data = uartRead()
    if data != "":
        print(data)
        fade(0,1)
    sleep(0.05)