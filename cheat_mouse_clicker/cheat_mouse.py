import pyautogui
import time
import keyboard


def _activate_mouse_and_desactivate():
    while True:
        try:
            keyboard.is_pressed("f6") # lo que pasa es que aquí si le decimos al programa que si está presionando el usuario tendrá que estár presionando todo el rato y no queremos eso
            if keyboard.is_pressed("F6") == True:
                print("se ha podido activar")
                time.sleep(1)
                pyautogui.click()
        except Exception as f6_event__activate:
            print(f"{f6_event__activate}")

        else:
            try:
                keyboard.is_pressed("f7")
                if keyboard.is_pressed("f7") == True:
                    print("se ha podido parar")
                    break
            except Exception as f6_event_desactivate:
                print(f"{f6_event_desactivate}")
                
            
_activate_mouse_and_desactivate()