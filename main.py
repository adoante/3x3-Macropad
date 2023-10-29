import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

btnGP = [board.GP0,board.GP7,board.GP15, board.GP4, board.GP9,board.GP13,board.GP27,board.GP20,board.GP16]

keyboard = Keyboard(usb_hid.devices)

btngtn = digitalio.DigitalInOut(btnGP[0])
btngtn.direction = digitalio.Direction.INPUT
btngtn.pull = digitalio.Pull.DOWN

btnC = digitalio.DigitalInOut(btnGP[1])
btnC.direction = digitalio.Direction.INPUT
btnC.pull = digitalio.Pull.DOWN

btnF = digitalio.DigitalInOut(btnGP[2])
btnF.direction = digitalio.Direction.INPUT
btnF.pull = digitalio.Pull.DOWN

btnA = digitalio.DigitalInOut(btnGP[3])
btnA.direction = digitalio.Direction.INPUT
btnA.pull = digitalio.Pull.DOWN

btnD = digitalio.DigitalInOut(btnGP[4])
btnD.direction = digitalio.Direction.INPUT
btnD.pull = digitalio.Pull.DOWN

btnG = digitalio.DigitalInOut(btnGP[5])
btnG.direction = digitalio.Direction.INPUT
btnG.pull = digitalio.Pull.DOWN

btnB = digitalio.DigitalInOut(btnGP[6])
btnB.direction = digitalio.Direction.INPUT
btnB.pull = digitalio.Pull.DOWN

btnE = digitalio.DigitalInOut(btnGP[7])
btnE.direction = digitalio.Direction.INPUT
btnE.pull = digitalio.Pull.DOWN

btnH = digitalio.DigitalInOut(btnGP[8])
btnH.direction = digitalio.Direction.INPUT
btnH.pull = digitalio.Pull.DOWN

while True:
    if btngtn.value:
        print("Button >. pressed")
        keyboard.press(Keycode.RETURN)
        time.sleep(0.1)
        keyboard.release(Keycode.RETURN)
        
    if btnA.value:
        print("Button A pressed")
        keyboard.press(Keycode.RETURN)
        time.sleep(0.1)
        keyboard.release(Keycode.RETURN)
        
    if btnB.value:
        print("Button B pressed")
        keyboard.press(Keycode.RETURN)
        time.sleep(0.1)
        keyboard.release(Keycode.RETURN)
        
    if btnC.value:
        print("Button C pressed")
        keyboard.press(Keycode.RETURN)
        time.sleep(0.1)
        keyboard.release(Keycode.RETURN)
        
    if btnD.value:
        print("Button D pressed")
        keyboard.press(Keycode.RETURN)
        time.sleep(0.1)
        keyboard.release(Keycode.RETURN)
        
    if btnE.value:
        print("Button E pressed")
        keyboard.press(Keycode.F5)
        time.sleep(0.1)
        keyboard.release(Keycode.F5)

    # control + shift + t,  shortcut to reopen closed tabs in an Internet browser
    if btnF.value:
        print("Button F pressed")
        keyboard.press(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.T)
        time.sleep(0.1)
        keyboard.release(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.T)
        
    if btnG.value:
        print("Button G pressed")
        keyboard.press(Keycode.RETURN)
        time.sleep(0.1)
        keyboard.release(Keycode.RETURN)
        
    if btnH.value:
        print("Button H pressed")
        keyboard.press(Keycode.RETURN)
        time.sleep(0.1)
        keyboard.release(Keycode.RETURN)
        
    
    
    time.sleep(0.1)
