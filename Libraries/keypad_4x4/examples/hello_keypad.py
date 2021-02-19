from machine import Pin
import keypad_4x4 as keypad
import utime

data = ""

while True:
    karakter = keypad.getKey()
    if karakter:
        keypad.debounce()
        print(karakter)
