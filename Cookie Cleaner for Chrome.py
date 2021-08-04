import os

user = input('Enter user Name: ')

path = f"C:/Users/{user}/AppData/Local/Google/Chrome/User Data/Default/Cookies"
pathz = f"C:/Users/{user}/AppData/Local/Google/Chrome/User Data/Default/Cookies-journal"
pathx = f"C:/Users/{user}/AppData/Local/Google/Chrome/User Data/Default/databases"

if os.path.exists(path):
    os.remove(path)
    print("Cookies Removed")
else:
    print("Error.")
if os.path.exists(pathz):
    os.remove(pathz)
    print("Cookies-journal Removed")
else:
    print("Error.")
if os.path.exists(pathx):
    os.remove(pathx)
    print("Databases Removed")
else:
    print("Error.")

power = input("Escribe apagar para terminar el proceso | Pulsa Enter para cerrar el programa de forma segura. | ")   
if power == "apagar":
    print(exit())
