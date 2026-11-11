import keyboard


def stop_and_run_executions():
        stop = "-"
        run = "+"
        if keyboard.on_press_key(run):
            return True
        else:
            keyboard.on_press_key(stop) 
            return False