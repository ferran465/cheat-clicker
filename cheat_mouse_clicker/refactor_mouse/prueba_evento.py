import pyautogui
import time
import keyboard

try:
    def activate_mouse_and_desactivate():
        if not keyboard.is_pressed("1") == True:
            print("escuchando evento")
            
        
    def desactivate():
        if keyboard.wait("space"):
            print("parar")

except KeyError as errn_event_key:
    print(f"{errn_event_key}")

while True:
    keyboard.add_hotkey("1", activate_mouse_and_desactivate)
    keyboard.add_hotkey("space", desactivate)