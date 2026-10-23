import pyautogui
import time
import keyboard


def activate_mouse_and_desactivate():
    if keyboard.is_pressed("1") == True:
        print("escuchando evento")
        keyboard.wait("space")
        print("parar")
      


while True:
    keyboard.add_hotkey("space", activate_mouse_and_desactivate)