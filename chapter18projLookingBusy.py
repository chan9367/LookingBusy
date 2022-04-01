import pyautogui, time

while True:
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    time.sleep(10)