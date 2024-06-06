import pyautogui, time

# 

def position():
    time.sleep(5)
    x, y = pyautogui.position()
    print("Coordenadas atuais do mouse: x = {}, y = {}".format(x, y))
    return x, y

def click(x , y, times, sec):
    time.sleep(sec)
    for c in range(0, times):
        time.sleep(1.5)
        pyautogui.click(x, y)

#print(position())

x = 1337
y = 782
sec = 5
times = 90

click(x, y, times, sec)

