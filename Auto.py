import time
import pyautogui
from pynput import keyboard

startNum = 107
moveRelX = 0
moveRelY = 20
def on_press(key):
    global startNum
    global moveRelX
    global moveRelY
    try:
        if key.char == '+':
            for _ in range(18):
                pyautogui.click()
                pyautogui.typewrite(str(startNum), 0.1)
                pyautogui.click(1183, 831, duration=0.2)
                time.sleep(0.1)
                # pyautogui.typewrite('r', 0.1)
                time.sleep(0.1)
                pyautogui.click()
                pyautogui.moveRel(moveRelX, moveRelY, 0.1)
                startNum = startNum-2

    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

