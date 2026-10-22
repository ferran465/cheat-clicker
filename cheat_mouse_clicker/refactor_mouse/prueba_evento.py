import pyautogui
import time
import keyboard


def activate_mouse_and_desactivate():
    
        if keyboard.is_pressed("f6") == True:
            print("escuchando evento")


while True:
    keyboard.add_hotkey("f6", activate_mouse_and_desactivate)