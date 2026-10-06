import keyboard
import time

class refactorized_:


    def __init__(self):
        pass
    def select_number_of_times(self):
                self.key = str(input("que tecla quieres escojer: "))
                self.number_time = input("quieres ejecutarlo un número de veces (y/n): ")
                if self.number_time == "y":
                    self.time = int(input("cuantas veces [introduzca un número por favor]: "))
                    try:
                        time.sleep(5)
                        while True: # no sé porque pero funciona mejor con un while que con un for pero tengo que ver la forma de rompe el bucle del for con le break
                            print("se ha podido ejecutar")
                            if keyboard.is_pressed("+"):
                                print("se ha podido presionar la tecla")
                                break
                    except KeyboardInterrupt as number_time_interrupt:
                        print(f"has interrumpido la acción{number_time_interrupt}")


if "__main__" == __name__:
    c = refactorized_()
    c.select_number_of_times() 
     



# necesito hacer que funcione las teclas + para poder parar el teclado