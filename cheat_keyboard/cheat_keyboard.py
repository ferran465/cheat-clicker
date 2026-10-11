import keyboard
import time
import asyncio

class cheat_keyboard:
    def __init__(self):
        pass

    def select_number_of_times(self):
        try:    
            motivo_bloqueo = "este keybind puede llegar a ser dañino para el propio sistema"    
            self.key = str(input("que tecla quieres escojer: "))
            if self.key == "win + e":
                print(motivo_bloqueo)
                return False
            if self.key == "win + q":
                print(motivo_bloqueo)
                return False
            else:
                    self.number_time = input("quieres ejecutarlo un número de veces (y/n): ")
                    if self.number_time == "y":
                        self.repeat = int(input("cuantas veces [introduzca un número por favor]: "))
                        self.time = float(input("cual es el lapso de tiempo en el que quieres que ocurra cada iteración ej recomendable = 0.3 0.4 0.5 [Advertencia contra menos pongas más rapido será y contra más pongas más lento será]: "))
        except KeyboardInterrupt as key_errn_select:
            print(f"has interrumpido la acción{key_errn_select}")                    
    def execute_number_times(self):            
        try:
            time.sleep(5)                
            for _ in range(self.repeat):
                if self.time > 0.3:
                    time.sleep(self.time) # esto se tiene que hacer que se puede modear (.4 README)
                    keyboard.send(self.key)
                    if keyboard.is_pressed("+"):
                        print("se ha podido interrumpir la tecla correctamente")
                        break
                    else:
                        keyboard.send(self.key)
                else:
                    self.time < 0.3
                    print("es demasiado bajo el número prueba con un número más alto")
                    return False
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
    # cuidado que esto tiene relevancia en el orden por culpa de eso me petaba
    c = cheat_keyboard()
    c.select_number_of_times()
    c.loop_times()
    c.execute_number_times()

