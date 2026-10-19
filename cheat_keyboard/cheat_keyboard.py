import keyboard
import time

class prototipe_keyboard:
    def __init__(self):
        self.add_block = ""
        self.number_time = ""
        self.block = ""             # empiezan des de "" str vacio ya que són solo texto
        self.add_block = ""                 
        self.key = ""
        self.number_time = ""
        self.repeat = 0 # empieza des de 0 ya que són números
        self.time = 0

    def block_key(self):
        try:    
            motivo_bloqueo = "tu tecla ha sido bloqueada perfectamente"
            self.block = str(input("quieres bloquear algúna tecla (y/n): "))
            if self.block.lower() == "y":
                self.add_block = str(input("añade la tecla que quieres bloquear ej [win + e, win + q...]: "))
                print(motivo_bloqueo)
        except Exception as block_exception:
            print(f"{block_exception}")

    def _select_number_n_(self):
        try:
            if self.block.lower() == "n": # si dices que "no" que se ejecute esta parte igual por una simple razón y es que si self.block == "n" hace la función igual pero sin la tecla bloqueada
                self.key = str(input("que tecla quieres escojer para el loop temporal: "))
                self.number_time = input("quieres ejecutarlo un número de veces (y/n): ")
                if self.number_time.lower() == "y":
                    self.repeat = int(input("cuantas veces [introduzca un número por favor]: "))
                    self.time = float(input("cual es el lapso de tiempo en el que quieres que ocurra cada iteración ej recomendable = 0.4 0.5 [Advertencia contra menos pongas más rapido será y contra más pongas más lento será]: "))

        except KeyboardInterrupt as key_errn_select_y:
            print(f"has interrumpido la acción{key_errn_select_y}")
        
    def _select_number_y_(self):
        try:
            if self.block.lower() == "y": # si dices que "si" que se ejecute esta parte igual pero con el bloqueo puesto
                self.key = str(input("que tecla quieres escojer para el loop temporal: "))
                self.number_time = input("quieres ejecutarlo un número de veces (y/n): ")
                if self.number_time.lower() == "y":
                    self.repeat = int(input("cuantas veces [introduzca un número por favor]: "))
                    self.time = float(input("cual es el lapso de tiempo en el que quieres que ocurra cada iteración ej recomendable = 0.4 0.5 [Advertencia contra menos pongas más rapido será y contra más pongas más lento será]: "))
            
        except KeyboardInterrupt as key_errn_select_n:
            print(f"has interrumpido la acción{key_errn_select_n}")
        
    def execute_number_times(self):
        try:
            print("espera 5 segundos antes de que se ejecute")
            time.sleep(5)                
            for _ in range(self.repeat):
                if self.time > 0:
                    time.sleep(self.time)
                    if self.key == self.add_block: # compara para que el programa evite tragarse la tecla bloqueada 
                        print("recuerda que tu tecla ya habia sido bloqueada anteriormente")
                        return False
                    else:
                        if self.block == "n":
                            keyboard.send(self.key)
                        else:
                            if self.block == "y":
                                keyboard.block_key(self.add_block) # bloquea la tecla física
                                keyboard.send(self.key)
                        if keyboard.is_pressed("+"):
                            return True
                        else:
                            if keyboard.is_pressed("-"):
                                print("se ha podido interrumpir la tecla correctamente")
                                break
                                        
                elif self.time < 0:
                        print("es demasiado bajo el número prueba con un número más alto")
                        return False
        except KeyboardInterrupt as number_time_interrupt:
            print(f"has interrumpido la acción{number_time_interrupt}")

    def loop_times(self):
        if self.number_time.lower() == "n":
            self.loop = input("quieres mejor ejecutarlo en bucle (y/n): ")
            if self.loop.lower() == "y": # hay que hacer que se tenga que elegir una tecla porque si no petaria des de aquí
                try:    
                    while True:
                        if self.key == self.add_block: # compara para que el programa evite tragarse la tecla bloqueada
                            print("recuerda que tu tecla ya habia sido bloqueada anteriormente")
                            return False
                        else:
                            if self.block == "n":
                                time.sleep(0.3) # duerme durante un segundo pero se mantiene vivo el otro segundo es decir que se ejecuta la cosa seria si no hubiera que congelaria la CPU
                                keyboard.send(self.key)
                            else:
                                if self.block == "y":
                                    keyboard.block_key(self.add_block) # bloquea la tecla física
                                    keyboard.send(self.key)
                                time.sleep(1)
                            if keyboard.is_pressed("+"):
                                return True
                                
                            else:
                                if keyboard.is_pressed("-"):
                                    print("se ha podido interrumpir la tecla correctamente")
                                    break
                except KeyboardInterrupt as bool_interrupt:
                            print(f"has interrumpido la acción{bool_interrupt}")
       
if "__main__" == __name__:
    # cuidado que esto tiene relevancia en el orden en el que llamas a cada función por culpa de eso me petaba
    K_Cheat = prototipe_keyboard()
    K_Cheat.block_key()
    if K_Cheat.block == "y":
        K_Cheat._select_number_y_()
        if K_Cheat.number_time == "y":
            K_Cheat.execute_number_times()
        else:
            K_Cheat.number_time == "n"
            K_Cheat.loop_times()
    else:
        K_Cheat.block == "n"
        K_Cheat._select_number_n_()
        if K_Cheat.number_time == "y":
            K_Cheat.execute_number_times()
        else:
            K_Cheat.number_time == "n"
            K_Cheat.loop_times()
            ## arreglar __main__