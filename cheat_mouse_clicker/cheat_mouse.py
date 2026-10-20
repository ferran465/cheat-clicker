import pyautogui
import time
import keyboard

def _activate_mouse_and_desactivate():
    while True:
        pass           
if keyboard.add_hotkey("f6", _activate_mouse_and_desactivate):
        try:
            time.sleep(0.1)
            pyautogui.click()
        except Exception as f6_event__activate:
                print(f"{f6_event__activate}")

else:
    try:
        keyboard.add_hotkey("f6", _activate_mouse_and_desactivate)
        desactivate_mouse = False
        pyautogui.click() = desactivate_mouse
    except Exception as f6_event_desactivate:
        print(f"{f6_event_desactivate}")
              
                
        

_activate_mouse_and_desactivate()