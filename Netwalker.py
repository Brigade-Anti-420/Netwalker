from hashlib import sha256
from pystyle import * 
from time import sleep
import socket
import os
from progress.bar import Bar
from progress.spinner import MoonSpinner
############################################################################
################    Author = Brigade Anti-420 !!#1418      ##################
############################################################################

banne = """

  _   _ _____ _______        ___    _     _  _______ ____    _ 
 | \ | | ____|_   _\ \      / / \  | |   | |/ / ____|  _ \  | |
 |  \| |  _|   | |  \ \ /\ / / _ \ | |   | ' /|  _| | |_) | | |
 | |\  | |___  | |   \ V  V / ___ \| |___| . \| |___|  _ <  |_|
 |_| \_|_____| |_|    \_/\_/_/   \_\_____|_|\_\_____|_| \_\ (_)
                                                              
"""

description = """
 Discord : Brigade Anti-420 !!#1418
 Github : https://github.com/Brigade-Anti-420
    
             ┌──────────┐
             │ Enjoy ;) │
             └──────────┘
             

"""

banner = Center.XCenter(banne)
des = Center.XCenter(description)

def downloading():
    with Bar(Colors.light_red  +'Processing...') as bar:
        for i in range(100):
            sleep(0.01)
            bar.next()
            
# def verifying():
#     with MoonSpinner(Colors.green +'Verifying...') as bar:
#         for i in range(35):
#             sleep(0.05)
#             bar.next()
            
def encrypt():
    first = input(Colors.pink +"Name of the file you want to encrypt/decrypt : "+Colors.white +"")
    final = input(Colors.blue +"Enter the name of the final file + extension : "+Colors.white +"")
    key = input(Colors.cyan +"Enter the decryption/encryption key : "+Colors.white +"")
    keys = sha256(key.encode('utf-8')).digest()
    with open(first,'rb') as f_fiirst :
        with open(final,'wb') as f_fiinal:
            i = 0
            while f_fiirst.peek():
                c = ord(f_fiirst.read(1))
                j = i % len(keys)
                b = bytes([c^keys[j]])
                f_fiinal.write(b)
                i = i + 1
                       
def main():
    
    os.system("cls")
    System.Size(120, 30)
    C = socket.gethostname()
    System.Title(f"Netwalker! [USER : {C}] - Made By Brigade Anti-420 [1418] - Free To Use ! - Made the [13/11/2022]")
    print(Colors.yellow, banner)
    print(Colors.orange, des)
    encrypt()
    downloading()
    print(Colors.green +"The file has successfully been encrypted/decrypted !\nYou can find the file in the folder where you downloaded netwalker !")
    a = input(Colors.red +"Continue ? y/n :"+Colors.white +"")
    if a =="y":
        main()
    else:
        exit()
        
main()




