# import the relevent modules
import pyautogui
import time

# Give python file some time before continuing
time.sleep(3)

# mouse functions
# print(pyautogui.size()) # Prints resultion of your screen
# print(pyautogui.position()) # Prints the current position
#
# # move the mouse over time
# pyautogui.moveTo(100, 100, duration=0.25)

# Move the mouse to relative position
# pyautogui.moveRel(100, 100, 3)

# Click
# pyautogui.click(100,100, 3, 3, button='left')
# pyautogui.tripleClick()
# pyautogui.doubleClick()
# pyautogui.leftClick()
# pyautogui.rightClick()

# scrolls up 200
# pyautogui.scroll(200)
#
# # scroll down
# pyautogui.scroll(-200)
#
# # mouse move up and down
# pyautogui.mouseUp(100, 100, button="left")

# Example of mouse up and down
# pyautogui.mouseDown(300, 400, button='left', duration=3)
# pyautogui.moveTo(800, 400, 3)
# pyautogui.mouseUp()
# pyautogui.moveTo(1000, 400, 3)
#
# # spiral drawing using pyautogui
# time.sleep(1)
#
# distance = 300
# while distance > 0:
#     pyautogui.dragRel(distance, 0, 1, button="left")
#     distance = distance - 20
#     pyautogui.dragRel(0, distance, 1, button="left")
#     pyautogui.dragRel(-distance, 0, 1, button="left")
#     distance = distance - 20
#     pyautogui.dragRel(0, -distance, 1, button="left")
#     time.sleep(4)

# Tik tok liker - Example
# time.sleep(3)
# # range will be the number of tik tok
# for i in range(10):
#     pyautogui.moveTo(450, 500)
#     time.sleep(2)
#     pyautogui.doubleClick()
#     time.sleep(2)
#     pyautogui.moveTo(845, 515)
#     time.sleep(1)
#     pyautogui.leftClick()


# Key Board functinos
# time.sleep(2)
# pyautogui.write("hello")
# pyautogui.press("enter")
# pyautogui.press("space")
# hello

# print(pyautogui.position())

#p = pyautogui.size()
#print(p)

text = """
An essay is, generally, a piece of writing that gives the author's own argument, but the definition is vague, overlapping with those of a letter, a paper, an article, a pamphlet, and a short story. Essays have been sub-classified as formal and informal: formal essays are characterized by "serious purpose, dignity, logical organization, length," whereas the informal essay is characterized by "the personal element (self-revelation, individual tastes and experiences, confidential manner), humor, graceful style, rambling structure, unconventionality or novelty of theme," etc.
"""

#time.sleep(4)
#def send_message(): # sending message automatically
#    time.sleep(1)
#    pyautogui.click()
#    pyautogui.write(text)
#    pyautogui.press("enter")
#    with pyautogui.hold('shift'):
#         pyautogui.press('s')
#         pyautogui.press("enter")
#    
#send_message()

# screen shot
#time.sleep(2)
#def screen_shot():
#    pyautogui.screenshot("screeshot2.png")
#
#screen_shot()

# Image recognation
#b = list(pyautogui.locateAllOnScreen('screeshot2.png'))
#print(b)
#print(b[0])
#print(b.left)

#try:
#    location = pyautogui.locateOnScreen('screenshot.png')
#    print(location)
#except:
#    print('Image could not be found.')

# Getting Window Information
fw = pyautogui.getActiveWindow()
print(fw.isActive())
