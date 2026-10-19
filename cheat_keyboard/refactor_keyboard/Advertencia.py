import os
import keyboard
import time

class _Advertencia_:
    def __init__(self):
        pass
    def caution(self):
        sleeps = float(input("mete números: "))
        if time.sleep(0.3): # necesito poner otro operador porque > y < no admiten ni int ni float
            return True
        else:
            time.sleep(0.3)
            return False 

if "__main__" == __name__:
    adv = _Advertencia_()
    adv.caution()