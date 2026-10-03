import keyboard
import time
import asyncio

class ask_keyboard:
    def __init__(self):
        pass

    def wich_key_do_you_want(self):
        self.key = str(input("que tecla quieres escojer: "))
        self.number_time = input("quieres ejecutarlo un número de veces (y/n): ")
        if self.number_time == "y":
            self.time = int(input("cuantas veces [introduzca un número por favor]: "))
            try:                
                for _ in range(self.time):
                    keyboard.send(self.key)
                    if keyboard.is_pressed("f6"): # esto no funciona
                        break
            except KeyboardInterrupt as number_time_interrupt:
                print(f"has interrumpido la acción{number_time_interrupt}")
                
        elif self.number_time == "n":
            self.loop = input("quieres mejor ejecutarlo en bucle (y/n): ")
            if self.loop == "y":
                try:    
                    while True:
                        keyboard.send(self.key)
                        if keyboard.is_pressed("f7"): # esto no funciona
                            break
                except KeyboardInterrupt as bool_interrupt:
                            print(f"has interrumpido la acción{bool_interrupt}")
                                    
            else:
                self.loop == "n"
                self.ask_time = input("quieres ejecutarlo con tiempo (y/n): ")
                if self.ask_time == "y":
                    pass # tengo que pensar que hacer aquí
                    


        
if "__main__" == __name__:
    c = ask_keyboard()
    c.wich_key_do_you_want()