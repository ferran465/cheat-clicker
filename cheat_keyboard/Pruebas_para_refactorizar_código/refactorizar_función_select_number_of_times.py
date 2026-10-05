import keyboard
import time


def select_number_of_times(self):
            self.key = str(input("que tecla quieres escojer: "))
            self.number_time = input("quieres ejecutarlo un número de veces (y/n): ")
            if self.number_time == "y":
                self.time = int(input("cuantas veces [introduzca un número por favor]: "))
                try:
                    time.sleep(5)
                    for _ in range(self.time):
                        if keyboard.is_pressed("+"):
                            print("se ha podido presionar la tecla")
                            break
                        else:
                            keyboard.send(self.key)

                        if keyboard.is_pressed("+"):
                            print("se ha podido presionar la tecla")
                            break
                except KeyboardInterrupt as number_time_interrupt:
                    print(f"has interrumpido la acción{number_time_interrupt}")



# necesito hacer que funcione las teclas + para poder parar el teclado