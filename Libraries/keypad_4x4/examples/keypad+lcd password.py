from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd
import keypad_4x4 as keypad
import utime

i2c = I2C(id=1,scl=Pin(11),sda=Pin(10),freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16) # LCD 16x2

data = ""

while True:
    lcd.move_to(4,0)
    lcd.putstr("Password")
    lcd.move_to(6,1)
    karakter = keypad.getKey()
    if karakter:
        keypad.debounce()
        if karakter == "#":
            if data == "123":
                lcd.clear()
                lcd.move_to(4,0)
                lcd.putstr("Correct!")
                utime.sleep_ms(2000)
                lcd.clear()
            else:
                lcd.clear()
                lcd.move_to(5,0)
                lcd.putstr("Wrong!")
                utime.sleep_ms(2000)
                lcd.clear()
            data = ""
        else:
            data = data + str(karakter)
            for i in range(0,len(data)):
                lcd.putstr("*")
