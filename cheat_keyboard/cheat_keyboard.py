import keyboard
import time

class cheat_keyboard:
    def __init__(self):
        self.block = ""
        self.add_block = ""
        self.number_time = ""
        self.repeat = 0              # todos inicializan des de 0 es decir todos parten en el inicializador de objetos des de 0 para poder añadir o desincrementar valor
        self.time = 0.4
        self.run = "+"
        self.stop = "-"

    def block_key(self):
        try:    
            motivo_bloqueo = "tu tecla ha sido bloqueada perfectamente"
            self.block = str(input("quieres bloquear algúna tecla (y/n): "))
            if self.block.lower() == "y":
                self.add_block = str(input("añade la tecla que quieres bloquear ej [win + e, win + q...]: "))
                print(motivo_bloqueo)
        except Exception as block_exception:
            print(f"{block_exception}")
    def select_number_of_times(self):
        try:
            if self.block.lower() == "n": # si dices que "no" que se ejecute esta parte igual
                self.key = str(input("que tecla quieres escojer: "))
                self.number_time = input("quieres ejecutarlo un número de veces (y/n): ")
                if self.number_time.lower() == "y":
                    self.repeat = int(input("cuantas veces [introduzca un número por favor]: "))
                    self.time = float(input("cual es el lapso de tiempo en el que quieres que ocurra cada iteración ej recomendable = 0.4 0.5 [Advertencia contra menos pongas más rapido será y contra más pongas más lento será]: "))
            else:
                self.block.lower() == "y" # si dices que "si" que se ejecute esta parte igual
                self.key = str(input("que tecla quieres escojer: "))
                self.number_time = input("quieres ejecutarlo un número de veces (y/n): ")
                if self.number_time.lower() == "y":
                    self.repeat = int(input("cuantas veces [introduzca un número por favor]: "))
                    self.time = float(input("cual es el lapso de tiempo en el que quieres que ocurra cada iteración ej recomendable = 0.4 0.5 [Advertencia contra menos pongas más rapido será y contra más pongas más lento será]: "))
                
        except KeyboardInterrupt as key_errn_select:
            print(f"has interrumpido la acción{key_errn_select}") 

    def stop_and_run_executions(self):
            if keyboard.on_press_key(self.run):
                return True
            else:
                keyboard.on_press_key(self.stop) 
                return False                   
    def execute_number_times(self):
        try:
            print("espera 5 segundos antes de que se ejecute")
            time.sleep(5)                
            for _ in range(self.repeat):
                if self.time > 0.3:
                    time.sleep(self.time) # esto se tiene que hacer que se puede modear (.4 README)
                    if self.key == self.add_block:
                        return False
                    else:
                        if self.key != self.add_block:
                            keyboard.send(self.key)
                            if keyboard.on_press_key(self.run, self.stop_and_run_executions): # dispara una sola vez uan callback es decir que solo una vez ejecuta la función cuando la pulsas no hace falta que la mantengas ni que esperes ni nada de eso
                                return True
                                
                        else:
                            if keyboard.on_press_key(self.stop, self.stop_and_run_executions): # necesita de una función para poderse hacer la callback no sirve con solo pasarle un solo parámetro ya que si no python peta y se calla
                                print("se ha podido interrumpir la tecla correctamente")
                                break
                                        
                elif self.time < 0.3:
                        print("es demasiado bajo el número prueba con un número más alto")
                        return False
        except KeyboardInterrupt as number_time_interrupt:
            print(f"has interrumpido la acción{number_time_interrupt}")

    def loop_times(self):
        if self.number_time.lower() == "n":
            self.loop = input("quieres mejor ejecutarlo en bucle (y/n): ")
            if self.loop.lower() == "y": # hay que hacer que se tenga que elegir una tecla porque si no petaria des de aquí
                self.loop_key = input("que tecla quieres escojer: ")
                try:    
                    while True:
                        if self.key != self.add_block:
                            time.sleep(1) # duerme durante un segundo pero se mantiene vivo el otro segundo es decir que se ejecuta la cosa seria si no hubiera que congelaria la CPU
                            keyboard.send(self.key)
                        else:
                            self.key == self.add_block
                            if keyboard.on_press_key(self.run, self.stop_and_run_executions): # dispara una sola vez uan callback es decir que solo una vez ejecuta la función cuando la pulsas no hace falta que la mantengas ni que esperes ni nada de eso
                                return True
                                
                            else:
                                if keyboard.on_press_key(self.stop, self.stop_and_run_executions): # necesita de una función para poderse hacer la callback no sirve con solo pasarle un solo parámetro ya que si no python peta y se calla
                                    print("se ha podido interrumpir la tecla correctamente")
                                    break
                except KeyboardInterrupt as bool_interrupt:
                            print(f"has interrumpido la acción{bool_interrupt}")
       
if "__main__" == __name__:
    # cuidado que esto tiene relevancia en el orden en el que llamas a cada función por culpa de eso me petaba
    c = cheat_keyboard()
    
    
    if c.block == "n":
        c.select_number_of_times()
        c.execute__number_times()
    if c.number_time == "n":
        c.loop_times()
    else:
        c.block == "y"
    c.block_key()
    c.select_number_of_times()
    c.execute_number_times()
    if c.number_time == "n":
        c.loop_times()