import pyautogui

pyautogui.click()
pyautogui.typewrite("Hello Venkatesh", interval=.1)
print(pyautogui.KEYBOARD_KEYS)
pyautogui.hotkey('ctrl', 'N')
pyautogui.click()
pyautogui.typewrite(['a', 'b', 'left', 'left', 'x', 'y'],interval=1)
