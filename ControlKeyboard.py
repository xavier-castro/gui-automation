#! python3

import pyautogui

print(pyautogui.KEYBOARD_KEYS) # All the keyboard names you can use

# 2 actions at the same time noted by the semicolon inbetween actions
pyautogui.click(100,100); pyautogui.typewrite('Hello world', interval=0.2) # Make sure wherever you are focused in the text input area

pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=1) # Prints a list of things you want to write with a second interval each 

pyautogui.hotkey('cmd', 'o') # Uses the CMD + O (open for mac) shortcut