#! python3
import pyautogui

pyautogui.size() # Returns the screen resolution
width, height = pyautogui.size() # Putting size into variables
pyautogui.position() # Returns where the mouse is at in the coordinates

# Moving the mouse
pyautogui.moveTo(10, 10) # Moves the mouse instantly to 10, 10
pyautogui.moveTo(10, 10, duration=1.5) # Moves the mouse to the coordinates in a span of 1.5 seconds 
pyautogui.moveRel(20, 0) # Moves the mouse 20 pixels to the right where it is relatively, can also add duration
pyautogui.click() # Clicks the mouse where it currently is, can enter coordinates
pyautogui.doubleClick() # Doubleclicks the mouse where it is, can enter coordinates
pyautogui.dragRel(10, 10) # Clicks and holds to the coordinates
pyautogui.displayMousePosition()