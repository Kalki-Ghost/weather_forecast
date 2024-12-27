import pyautogui

size = 0
pyautogui.click()
while size < 400:
    pyautogui.dragRel(size, 0, duration=.2)
    size = size + 25
    pyautogui.dragRel(0, size, duration=.2)
    pyautogui.dragRel(-size, 0, duration=.2)
    size = size + 25
    pyautogui.dragRel(0, -size, duration=.2)
# while size > 0:
#   pyautogui.dragRel(size, 0, duration=.1)
#   size = size - 25
#   pyautogui.dragRel(0, size, duration=.1)
#   pyautogui.dragRel(-size, 0, duration=.1)
#   size = size - 25
#   pyautogui.dragRel(0, -size, duration=.1)
print(pyautogui.KEYBOARD_KEYS)
