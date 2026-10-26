import pyautogui

while True:
    pyautogui.FAILSAFE = False
    try:
        pyautogui.click()
        print("click")

    except Exception as Errn_click:
        print("Errn in click", f"{Errn_click}")