from datetime import datetime

while True:
   try:
       fecha_str = input('\n Ingrese fecha ==> ejemplo "18/01/1952"...: ')
       fecha = datetime.strptime(fecha_str, '%d/%m/%Y %H:%M')
       break
   except:
       print("\n No ha ingresado una fecha correcta...")

print("\n ", fecha)