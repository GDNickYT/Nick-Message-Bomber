from xml.dom import NoModificationAllowedErr
import keyboard
import pyautogui
import time
import colorama
import sys
from colorama import Fore,Back,Style
colorama.init(autoreset = True)
delay_type = None
total_messages = 0
print("███╗░░░███╗███████╗░██████╗░██████╗░█████╗░░██████╗░███████╗  ██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░")
print("████╗░████║██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝░██╔════╝  ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗")
print("██╔████╔██║█████╗░░╚█████╗░╚█████╗░███████║██║░░██╗░█████╗░░  ██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝")
print("██║╚██╔╝██║██╔══╝░░░╚═══██╗░╚═══██╗██╔══██║██║░░╚██╗██╔══╝░░  ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗")
print("██║░╚═╝░██║███████╗██████╔╝██████╔╝██║░░██║╚██████╔╝███████╗  ██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║")
print("╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═════╝░╚═╝░░╚═╝░╚═════╝░╚══════╝  ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝")
print( Back.LIGHTMAGENTA_EX + Fore.LIGHTBLACK_EX +  "                                                  By GDNick                                                            ")
print(" ")
time.sleep(0.7)
def start_bomb():
    global total_messages
    try:
        while True:
            time.sleep(delay)
            pyautogui.write(message1)
            pyautogui.press('enter')
            total_messages += 1
            print('Messages Sent: ' + str(total_messages), end='\r')    
    except KeyboardInterrupt:
        print("\nExiting...")
        time.sleep(0.1)
        exit()

message1 = str(input("Message:"))
print(Fore.LIGHTYELLOW_EX + "Tip:Some messengers have anti-spam,so dont make the delay less than 0.25!")
delay = input("Delay: ")
type = isinstance(delay,int)
print(str(type))
print(Fore.RED + "ERROR:The value is not an integer. Quitting...")
exit()
print(Fore.RED + "WARNING! You have 15 seconds to choose a prompt that the text will be inserted in.")
time.sleep(15)
start_bomb()
