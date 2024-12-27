import pyautogui

print(pyautogui.size())
print(pyautogui.position())
pyautogui.moveTo(150, 1100, duration=.5)
pyautogui.click()
pyautogui.moveRel(0, -200, duration=.5)
