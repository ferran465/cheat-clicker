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
                        for _ in range(self.time): # intuio que por un while lo puedes parar más facil ya que con un while se ejecuta infinitamente así que cuando presionamos puedes pararlo cuando quieras pero con un for es como si tuvieras que acabar con la tarea
                            time.sleep(0.3) # ya lo he entendido con un time.sleep() hace que el programa pueda hacer que en 0,3 segundos se ejecute y ahí estava el problema estaba en que se ejecutaba tan rapido que no se podia parar
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