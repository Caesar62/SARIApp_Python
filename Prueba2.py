from datetime import datetime

while True:
   try:
       fecha_str = input('\n Ingrese fecha ==> ejemplo "18/01/1952 23:45"...: ')
       fecha = datetime.strptime(fecha_str, '%d/%m/%Y %H:%M')
       break
   except:
       print("\n No ha ingresado una fecha correcta...")

print("\n ", fecha)
'''

dt_string = "12/11/2018 09:15:32"

# Considering date is in dd/mm/yyyy format
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("dt_object1 =", dt_object1)

# Considering date is in mm/dd/yyyy format
dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("dt_object2 =", dt_object2)
'''