import pyautogui
from pynput.keyboard import Listener, KeyCode, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import sys
import time
from colorama import init, Fore

stop_flag = False
init(autoreset=True)
keyboard = KeyboardController()
mouse = MouseController()

print(Fore.WHITE + "Welcome To Minecraft Automation")
time.sleep(1)
print(Fore.YELLOW + "MENU")
print(Fore.CYAN + "1. Automate attacking (hitting single click)")
print(Fore.CYAN + "2. Automate mining (clicking only)")
print(Fore.CYAN + "3. Automate mining (clicking and moving)")
print(Fore.CYAN + "4. Automate running (Moving only)")
print(Fore.CYAN + "5. Automate running (Moving and jumping)")
print("")
print("")
print(Fore.YELLOW + "NOTE THE PROCESS STARTS AFTER 5 SECONDS ON ENTERING THE OPTION NUMBER")
print(Fore.YELLOW + "TO END THE PROCESS PRESS" + Fore.RED + " P ")
option = input(Fore.WHITE + "ENTER OPTION NUMBER: ")
time.sleep(5)

def on_press(key):
    global stop_flag
    if key == KeyCode.from_char('p'):
        print(Fore.RED + "Stopping the process...")
        stop_flag = True
        return False

def start_pressing():
    while not stop_flag:
        if option == '1':
            mouse.click(Button.left, 1)
        elif option == '2':
            mouse.press(Button.left)
        elif option == '3':
            mouse.press(Button.left)
            keyboard.press('w')
            time.sleep(0.5)
            keyboard.release('w')
        elif option == '4':
            keyboard.press('w')
        elif option == '5':
            keyboard.press('w')

# Start pressing the keys and listen for the 'p' key press
with Listener(on_press=on_press) as listener:
    start_pressing()

# End the process
sys.exit()
