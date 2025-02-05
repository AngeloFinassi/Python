import pyautogui
from time import sleep

msg = str(input("Msg:"))
time_start = 5
time_run = 100
Point = (1096, 968)

sleep(time_start)

pyautogui.click(Point[0], Point[1])

print("Start")
for c in range(0, time_run):
    pyautogui.write(msg)
    pyautogui.press("enter")

print("End.")