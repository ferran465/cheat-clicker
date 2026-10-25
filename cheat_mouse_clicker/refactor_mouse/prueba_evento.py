import pyautogui
import time
import keyboard

def activate_mouse_and_desactivate():
        if keyboard.is_pressed("1") == True:
            print("escuchando evento")
            
        
def desactivate():
        if keyboard.wait("space"):
            print("parar")


while True:
    keyboard.add_hotkey("1", activate_mouse_and_desactivate)
    keyboard.add_hotkey("space", desactivate)