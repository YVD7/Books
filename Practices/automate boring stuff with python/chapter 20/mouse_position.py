import pyautogui

p = pyautogui.position() # get current mouse position\

print(p)

print(p[0]) # The x-coordinates is at index 0.

print(p.x) # The x-coordinates is also in the x attribute