import keyboard
import pyautogui
import time

class prototipe_mouse:
    def __init__(self):
        velocity = ""
        question_velocity = float

    def velocidad(self):
            self.velocity = str(input("quieres disminuir velocidad (y/n) "))
            if self.velocity == "y":
                self.question_velocity = float(input("cuanta velocidad ? "))
                while True:
                    if keyboard.is_pressed("f5"):
                        print("activar")
                        while True:
                            time.sleep(self.question_velocity)
                            pyautogui.click()
                            print("click")
    
                            if keyboard.is_pressed("f4"):
                                print("stop")
                                break

            

    def activate_stop(self):
        pyautogui.FAILSAFE = False
        if self.velocity == "n":
            while True:
                try:
                    if keyboard.is_pressed("f6") == True:
                        print("activar")
                        while True:
                            pyautogui.click()
                            print("click")

                            if keyboard.is_pressed("f7"):
                                print("stop")
                                break

                except Exception as Clicking_errn:
                        print("no se ha podido clicar", f"{Clicking_errn}")

    
        

if "__main__" == __name__:
    M_Cheat = prototipe_mouse()
    M_Cheat.velocidad()
    M_Cheat.activate_stop()

        