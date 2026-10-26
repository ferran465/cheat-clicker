     
     
1.     File "c:\Users\Usuario\cheat-clicker\cheat_keyboard\cheat_keyboard.py", line 86, in <module>
            if c.number_time == "y":
            ^^^^^^^^^^^^^
        AttributeError: 'cheat_keyboard' object has no attribute 'number_time'
        PS C:\Users\Usuario\cheat-clicker>

2. File "c:\Users\ferra\cheat-clicker\cheat_keyboard\cheat_keyboard.py", line 101, in <module>
    K_Cheat.execute_number_times()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "c:\Users\ferra\cheat-clicker\cheat_keyboard\cheat_keyboard.py", line 51, in execute_number_times
    if self.key == self.add_block:
                   ^^^^^^^^^^^^^^
AttributeError: 'cheat_keyboard' object has no attribute 'add_block'
PS C:\Users\ferra\cheat-clicker>


3. PS C:\Users\Usuario\cheat-clicker> (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& c:\Users\Usuario\cheat-clicker\.venv\Scripts\Activate.ps1)
(.venv) PS C:\Users\Usuario\cheat-clicker> & c:\Users\Usuario\cheat-clicker\.venv\Scripts\python.exe c:/Users/Usuario/cheat-clicker/cheat_mouse_clicker/refactor_mouse/prueba_switch_wait.py
----
desactivar
|||||||
activar
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
click
no se ha podido clicar PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set pyautogui.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED.
Traceback (most recent call last):
  File "c:\Users\Usuario\cheat-clicker\cheat_mouse_clicker\refactor_mouse\prueba_switch_wait.py", line 5, in <module>
    if keyboard.is_pressed("1") == True:
       ~~~~~~~~~~~~~~~~~~~^^^^^
  File "C:\Users\Usuario\cheat-clicker\.venv\Lib\site-packages\keyboard\__init__.py", line 417, in is_pressed
    steps = parse_hotkey(hotkey)
  File "C:\Users\Usuario\cheat-clicker\.venv\Lib\site-packages\keyboard\__init__.py", line 344, in parse_hotkey
    scan_codes = key_to_scan_codes(hotkey)
  File "C:\Users\Usuario\cheat-clicker\.venv\Lib\site-packages\keyboard\__init__.py", line 309, in key_to_scan_codes
    normalized = normalize_name(key)
  File "C:\Users\Usuario\cheat-clicker\.venv\Lib\site-packages\keyboard\_canonical_names.py", line 1246, in normalize_name
    return canonical_names.get(name, name)
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
## dice que no es muy recomendable pero para habilitarlo en un bucle infinito donde la opinión del usuario importa más que la nuestra pondremso que Failsafe tenga un valor de False