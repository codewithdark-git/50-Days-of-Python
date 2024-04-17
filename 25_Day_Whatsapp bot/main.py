import random
import pyautogui as pg  # pip install pyautogui
import time

# initialize the variables
animal = ("monkey", "donkey", "dog")


time.sleep(8)

# used loop for the number of messages
for i in range(500):
    a=random.choice(animal)
    # pg.write mean write message in plateform eg whatsapp, messager, etc
    pg.write("You are a" + a)
    # pg.press mean when press enter or button to start sending messages
    pg.press("enter")


 #`when you only send repeat a message`

import random
import pyautogui as pg  # pip install pyautogui
import time

time.sleep(8)

# used loop for the number of messages
for i in range(500):
    # pg.write mean write message in plateform eg whatsapp, messager, etc
    pg.write("your msg")
    # pg.press mean when press enter or button to start sending messages
    pg.press("enter")

