import pyautogui

print(pyautogui.size())

print(pyautogui.position())
pyautogui.moveTo(1500, 20)
while 1:
    pyautogui.moveRel(400, 0, duration=1)
    pyautogui.moveRel(0, 400, duration=1)
    pyautogui.moveRel(-400, 0, duration=1)
    pyautogui.moveRel(0, -400, duration=1)
