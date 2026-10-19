import pyautogui
import time
import keyboard
class prototipe_mouse:
    def __init__(self):
        self.mouse_block = ""
        self.mouse_activate = ""
        self.stop_mouse = "-"
        self.run_mouse = "+"
    def _activate_mouse(self):
        try:        
            self.mouse_activate = str(input("quiere activar su ratón (y/n): "))
            if self.mouse_activate == "y":
                while True:
                    time.sleep(0.1)
                    pyautogui.click()
                    if keyboard.is_pressed("-"):
                        break
                    else:
                        keyboard.is_pressed("+")

        except Exception as E: # necesito hacer una excepción propia
            print(f"{E}")

if "__main__" == __name__:
    M_Cheat = prototipe_mouse()
    M_Cheat._activate_mouse()
