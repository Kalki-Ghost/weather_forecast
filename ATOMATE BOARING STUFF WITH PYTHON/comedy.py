import time
import random
import pyautogui as pa

time.sleep(8)

animals = ["donkey", "donkey", "dog"]

for i in range(100):
    pa.write("You are a " + random.choice(animals))
    pa.press('enter')
