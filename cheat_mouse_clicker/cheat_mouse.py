import keyboard
import pyautogui

class prototipe_mouse:
    def __init__(self):
        pass
    def activate_stop(self):
        pyautogui.FAILSAFE = False
        while True:
            try:
                if keyboard.is_pressed("1") == True:
                    print("activar")
                    while True:
                        pyautogui.click()
                        print("click")

                        if keyboard.is_pressed("space"):
                            print("----")
                            break

            except Exception as Clicking_errn:
                    print("no se ha podido clicar", f"{Clicking_errn}")

if "__main__" == __name__:
    M_Cheat = prototipe_mouse() 
    M_Cheat.activate_stop()