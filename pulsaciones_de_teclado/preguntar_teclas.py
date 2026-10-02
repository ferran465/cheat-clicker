import keyboard

import asyncio

class ask_keyboard:
    def __init__(self):
        pass

    async def wich_key_do_you_want(self):
        self.key = str(input("que tecla quieres escojer: "))
        try:
            if self.key == "a":
                self.ask_time = input("quieres establecer tiempo (y/n) :")
                if self.ask_time == "y":
                    self.time = int(input("cuanto tiempo quieres establecer: "))
                    if self.time:
                            await asyncio.sleep(self.time)
                            while True:
                                keyboard.send("a")
                        
                elif self.ask_time == "n":
                        self.loop = input("quieres mejor ejecutarlo en bucle (s/n) :")
                        if self.loop == "y":
                            while True: # no se ejecuta el while...
                                keyboard.send("a")
                        else:
                            self.loop == "n"
                            return False               
        except Exception as A:
            print(f"no se ha podido ejecutar la tecla{A}")



if "__main__" == __name__:
    c = ask_keyboard()
    asyncio.run(c.wich_key_do_you_want())