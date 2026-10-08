import keyboard
import time

class refactorized_:


    def __init__(self):
        pass
    def select_number_of_times(self):
                self.key = str(input("que tecla quieres escojer: "))
                self.number_time = input("quieres ejecutarlo un número de veces (y/n): ")
                if self.number_time == "y":
                    self.repeat = int(input("cuantas veces [introduzca un número por favor]: "))
                    self.time = float(input("cual es el lapso de tiempo en el que quieres que ocurra cada iteración ej recomendable = 0.3 0.4 0.5 [Advertencia contra menos pongas más rapido será y contra más pongas más lento será]: ")) 
                    try:
                        time.sleep(5)
                        for _ in range(self.repeat):
                            if self.time == {0, 0.1, 0.2}:
                                time.sleep(self.time) # ya lo he entendido con un time.sleep() hace que el programa pueda hacer que en 0,3 segundos se ejecute y ahí estava el problema estaba en que se ejecutaba tan rapido que no se podia parar // ## ahora lo que hace es hacerlo con input
                                keyboard.send(self.key)
                                if keyboard.is_pressed("+"):
                                    print("se ha podido presionar la tecla")
                                    break
                    except KeyboardInterrupt as number_time_interrupt:
                        print(f"has interrumpido la acción{number_time_interrupt}")


if "__main__" == __name__:
    c = refactorized_()
    c.select_number_of_times() 
     



# necesito hacer que funcione las teclas + para poder parar el teclado