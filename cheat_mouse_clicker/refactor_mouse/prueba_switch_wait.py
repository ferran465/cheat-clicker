import keyboard
import pyautogui

while True:
    print("|||||||")
    if keyboard.is_pressed("1") == True:
        print("activar")

        try:
            while True:        
                pyautogui.click()
                print("click")

        except Exception as Click_errn:
            print("no se ha podido clicar", f"{Click_errn}")
        
        

    else:
        try:
            print("----")
            keyboard.wait("space")
            print("desactivar")
        except Exception as errn_wait:
            print("no se ha podido parar", f"{errn_wait}")