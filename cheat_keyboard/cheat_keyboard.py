import keyboard
import time

class cheat_keyboard:
    def __init__(self):
        pass

    def block_key(self):
        try:    
            motivo_bloqueo = "este keybind puede llegar a ser dañino para el propio sistema"
            self.block = str(input("quieres bloquear algúna tecla (y/n): "))
            if self.block.lower() == "y":
                self.add_block = str(input("añade la tecla que quieres bloquear ej [win + e, win + q...]: "))
                self.add_block = False
                print("tu tecla ha sido bloqueada perfectamente")
        except Exception as block_exception:
            print(f"{block_exception}")
    def select_number_of_times(self):
        try:
            if self.block.lower() == "n":
                self.key = str(input("que tecla quieres escojer: "))
                self.number_time = input("quieres ejecutarlo un número de veces (y/n): ")
                if self.number_time.lower() == "y":
                    self.repeat = int(input("cuantas veces [introduzca un número por favor]: "))
                    self.time = float(input("cual es el lapso de tiempo en el que quieres que ocurra cada iteración ej recomendable = 0.3 0.4 0.5 [Advertencia contra menos pongas más rapido será y contra más pongas más lento será]: "))
            else:
                self.block.lower() == "y"
                self.key = str(input("que tecla quieres escojer: "))
                self.number_time = input("quieres ejecutarlo un número de veces (y/n): ")
                if self.number_time.lower() == "y":
                    self.repeat = int(input("cuantas veces [introduzca un número por favor]: "))
                    self.time = float(input("cual es el lapso de tiempo en el que quieres que ocurra cada iteración ej recomendable = 0.3 0.4 0.5 [Advertencia contra menos pongas más rapido será y contra más pongas más lento será]: "))
                
        except KeyboardInterrupt as key_errn_select:
            print(f"has interrumpido la acción{key_errn_select}")                    
    def execute_number_times(self):            
        try:
            print("espera 5 segundos antes de que se ejecute")
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
        if self.number_time.lower() == "n":
            self.loop = input("quieres mejor ejecutarlo en bucle (y/n): ")
            if self.loop.lower() == "y":
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
    # cuidado que esto tiene relevancia en el orden en el que llamas a cada función por culpa de eso me petaba
    c = cheat_keyboard()

    c.block_key()
    if c.block == "y":
        c.select_number_of_times()
        c.block == "n"
        c.select_number_of_times()
    if c.number_time == "y":        
        c.execute_number_times()
    else:
        c.number_time == "n"
        c.loop_times()