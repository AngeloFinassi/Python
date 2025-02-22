import pyautogui
import time

msg = "Call?"  
sec = 2
times = 0.3
time.sleep(5)

for c in range(0, 100):
    pyautogui.write(msg)
    pyautogui.press("enter")
    time.sleep(times)


