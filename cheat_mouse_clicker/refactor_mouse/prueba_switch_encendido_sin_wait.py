import keyboard
import pyautogui

while True:
    if keyboard.is_pressed("1") == True:
        print("activar")

        try:
            while True:        
                pyautogui.click()
                print("click")

        except Exception as Click_errn:
            print("no se ha podido clicar", f"{Click_errn}")