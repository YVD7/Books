import pyautogui, time

pyautogui.FAILSAFE = True

time.sleep(3)

text = open("test.txt")
for each_line in text:
    pyautogui.write(each_line)
