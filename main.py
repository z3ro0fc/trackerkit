import requests
from colorama import Fore, init
import time
import os

init()

rojo = Fore.RED
azul = Fore.BLUE
verde = Fore.GREEN
violeta = Fore.MAGENTA
cyan = Fore.CYAN
blanco = Fore.WHITE
amarillo = Fore.YELLOW


print(f"""{verde}██╗░░██╗██████╗░██╗░░░██╗██████╗░████████╗░█████╗░███╗░░██╗
██║░██╔╝██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔══██╗████╗░██║
█████═╝░██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║░░██║██╔██╗██║
██╔═██╗░██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║░░██║██║╚████║
██║░╚██╗██║░░██║░░░██║░░░██║░░░░░░░░██║░░░╚█████╔╝██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═╝░░╚══╝
{verde}
{rojo}           <<< {rojo} {amarillo} Tool Created by @s1krypton {amarillo} {rojo} >>>
{rojo}           <<< {rojo} {amarillo}Tra{amarillo}{azul}cker{azul}{verde}kit{verde}{rojo} >>>
{rojo} 
 """)


msg = "Loading recurses.."
print(msg)
time.sleep(2)


if os.name == "posix":
   os.system ("clear")
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   os.system ("cls")
   
   
   
#otra portada xd 


print(f"""{verde}
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗░░░░░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝░░░░░
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░░░░░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░░░░░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗░░░░░
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝░░░░░

{verde}
{rojo}           <<< {rojo} {amarillo} Tool Created by @s1krypton {amarillo} {rojo} >>>
{rojo}           <<< {rojo} {amarillo}Tra{amarillo}{azul}cker{azul}{verde}kit{verde}{rojo} >>>
{rojo} 
 """)
 
 
 
msg = "iniciando tracker kit.."
print(msg)
time.sleep(2)


if os.name == "posix":
   os.system ("clear")
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   os.system ("cls")
   
   
print(f"""╔════╗╔═══╗╔═══╗╔═══╗╔╗╔═╗╔═══╗╔═══╗────╔╗╔═╗╔══╗╔════╗
║╔╗╔╗║║╔═╗║║╔═╗║║╔═╗║║║║╔╝║╔══╝║╔═╗║────║║║╔╝╚╣╠╝║╔╗╔╗║
╚╝║║╚╝║╚═╝║║║─║║║║─╚╝║╚╝╝─║╚══╗║╚═╝║────║╚╝╝──║║─╚╝║║╚╝
──║║──║╔╗╔╝║╚═╝║║║─╔╗║╔╗║─║╔══╝║╔╗╔╝────║╔╗║──║║───║║──
──║║──║║║╚╗║╔═╗║║╚═╝║║║║╚╗║╚══╗║║║╚╗────║║║╚╗╔╣╠╗──║║──
──╚╝──╚╝╚═╝╚╝─╚╝╚═══╝╚╝╚═╝╚═══╝╚╝╚═╝────╚╝╚═╝╚══╝──╚╝──

[ 1 ] CREATER TRACKER
[ 2 ] DNI TRACKER
[ 3 ] INFO TRACKER""")


def dni_tracker():
    dni = int(input("COLOCA EL DNI == "))
    
    url = f"https://dni-finder.herokuapp.com/api/dni/{dni}"
    
    resp = requests.get(url)
    
    data = resp.json()
    
person = ['data']['person']
sex = ['data']['sex']
cuit = ['data']['cuit']

print(f"NOMBRE COMPLETO = {person}")
print(f"SEXO = {sex}")
print(f"CUIT = {cuit}")
