import keyboard

try:
    while True:
        if keyboard.is_pressed("+"):
            print("se ha podido ejecutar")
        if keyboard.is_pressed("-"):
            break
except:
    pass