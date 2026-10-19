import keyboard
import time

def loop_times():
    input_1 = input("introduce una tecla...: ")
    try:    
        while True: # va demasiado rápido como para captar .is_pressed el break
            if keyboard.is_pressed("+"):
                time.sleep(3)
                print("se ha podido interrumpir la tecla correctamente")
                break
            else:
                keyboard.send(input_1)
    except KeyboardInterrupt as bool_interrupt:
                print(f"has interrumpido la acción{bool_interrupt}")

loop_times()