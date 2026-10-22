import keyboard
import time
import pyautogui


def evento():
    while True:
        try:
            if keyboard.is_pressed("f6"):
                print("tu tecla ha sido pulsada")
                pyautogui.click()
            else:
                print("no ha sido pulsada")

            if keyboard.is_pressed("f7"):
                print("break")
                break

        except:
            pass


keyboard.on_press_key("f6", evento)

evento()
