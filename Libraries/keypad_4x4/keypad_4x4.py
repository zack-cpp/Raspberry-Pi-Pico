from machine import Pin
import utime

keypad = ["1","4","7","*"],["2","5","8","0"],["3","6","9","#"],["A","B","C","D"]

key1 = Pin(2, Pin.IN, Pin.PULL_DOWN)
key2 = Pin(3, Pin.IN, Pin.PULL_DOWN)
key3 = Pin(4, Pin.IN, Pin.PULL_DOWN)
key4 = Pin(5, Pin.IN, Pin.PULL_DOWN)
key5 = Pin(6, Pin.OUT)
key6 = Pin(7, Pin.OUT)
key7 = Pin(8, Pin.OUT)
key8 = Pin(9, Pin.OUT)

key5.value(1)
key6.value(1)
key7.value(1)
key8.value(1)

state1 = [False,False,False,False]
state2 = [False,False,False,False]

def reverse():
    key1 = Pin(2, Pin.OUT)
    key2 = Pin(3, Pin.OUT)
    key3 = Pin(4, Pin.OUT)
    key4 = Pin(5, Pin.OUT)
    key5 = Pin(6, Pin.IN, Pin.PULL_DOWN)
    key6 = Pin(7, Pin.IN, Pin.PULL_DOWN)
    key7 = Pin(8, Pin.IN, Pin.PULL_DOWN)
    key8 = Pin(9, Pin.IN, Pin.PULL_DOWN)
    
    key1.value(1)
    key2.value(1)
    key3.value(1)
    key4.value(1)

def detect():
    keyState = False
    if key1.value() == 1 or key2.value() == 1 or key3.value() == 1 or key4.value() == 1:
        keyState = True
        
    if key1.value() == 1:
        state1[3] = True
    else:
        state1[3] = False
    if key2.value() == 1:
        state1[2] = True
    else:
        state1[2] = False
    if key3.value() == 1:
        state1[1] = True
    else:
        state1[1] = False
    if key4.value() == 1:
        state1[0] = True
    else:
        state1[0] = False
        
    return keyState

def detectReverse():
    if key5.value() == 1:
        state2[3] = True
    else:
        state2[3] = False
    if key6.value() == 1:
        state2[2] = True
    else:
        state2[2] = False
    if key7.value() == 1:
        state2[1] = True
    else:
        state2[1] = False
    if key8.value() == 1:
        state2[0] = True
    else:
        state2[0] = False

def check():
    x = 0
    y = 0
    for i in range(0, 4):
        if state1[i] == True:
            x = i
    for i in range(0, 4):
        if state2[i] == True:
            y = i
    return keypad[x][y]

def normalize():
    key1 = Pin(2, Pin.IN, Pin.PULL_DOWN)
    key2 = Pin(3, Pin.IN, Pin.PULL_DOWN)
    key3 = Pin(4, Pin.IN, Pin.PULL_DOWN)
    key4 = Pin(5, Pin.IN, Pin.PULL_DOWN)
    key5 = Pin(6, Pin.OUT)
    key6 = Pin(7, Pin.OUT)
    key7 = Pin(8, Pin.OUT)
    key8 = Pin(9, Pin.OUT)

    key5.value(1)
    key6.value(1)
    key7.value(1)
    key8.value(1)
    
    state1 = [False,False,False,False]
    state2 = [False,False,False,False]

def getKey():
    if(detect()):
        reverse()
        detectReverse()
        karakter = check()
        normalize()
        if karakter is not None:
            return karakter
        else:
            return False

def debounce():
    while key1.value() != 0 or key2.value() != 0 or key3.value() != 0 or key4.value() != 0:
        doNothing = True
        