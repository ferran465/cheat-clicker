import keyboard
import time
import asyncio

class cheat_keyboard:
    def __init__(self):
        pass

    def select_number_of_times(self):
            self.key = str(input("que tecla quieres escojer: "))
            self.number_time = input("quieres ejecutarlo un número de veces (y/n): ")
            if self.number_time == "y":
                self.time = int(input("cuantas veces [introduzca un número por favor]: "))
                try:
                    time.sleep(5)                
                    for _ in range(self.time):
                        time.sleep(0.3) # esto se tiene que hacer que se puede modear (.4 README)
                        keyboard.send(self.key)
                        if keyboard.is_pressed("+"):
                            print("se ha podido interrumpir la tecla correctamente")
                            break
                        else:
                            keyboard.send(self.key)
                except KeyboardInterrupt as number_time_interrupt:
                    print(f"has interrumpido la acción{number_time_interrupt}")

    def loop_times(self):
            if self.number_time == "n":
                    self.loop = input("quieres mejor ejecutarlo en bucle (y/n): ")
                    if self.loop == "y":
                        try:    
                            while True:
                                if keyboard.is_pressed("+"):
                                    print("se ha podido interrumpir la tecla correctamente")
                                    break
                                else:
                                    keyboard.send(self.key)
                        except KeyboardInterrupt as bool_interrupt:
                                    print(f"has interrumpido la acción{bool_interrupt}")

    def select_time(self):
            if self.loop == "n":
                self.ask_time = input("quieres ejecutarlo con tiempo (y/n): ")
                if self.ask_time == "y":
                    pass # tengo que pensar que hacer aquí <------
        
if "__main__" == __name__:
    c = cheat_keyboard()
    c.select_number_of_times()
    c.loop_times()
