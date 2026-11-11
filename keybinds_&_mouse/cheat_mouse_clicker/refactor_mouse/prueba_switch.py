import keyboard
import pyautogui

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