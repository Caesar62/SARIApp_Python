from datetime import datetime, date, time, timedelta

H_LKP = str(input("\n\tHora LKP  (dd-mm-yyyy hh:mm)\t:  "))
H_DATUM = str(input("\n\tHora Datum  (dd-mm-yyyy hh:mm)\t:  "))
#H_LKP = '22-02-1962 3:50'
#H_DATUM = '24-02-1962 3:50'

# Transformacion del intervalo en horas 

format = "%d-%m-%Y %H:%M"
datetime_object = datetime.strptime(H_LKP, format)


format = "%d-%m-%Y %H:%M"
datetime_object_2 = datetime.strptime(H_DATUM, format)

diferencia_days= (datetime_object_2 - datetime_object)/ timedelta(days=1)
diferencia_horas=diferencia_days*24
#diferencia_horas=('{0:.2f}'.format(diferencia_horas))

print(datetime_object)
print(datetime_object_2)
print(diferencia_horas)

INTERVALO=int(input('Intervalo en minutos\t:\t'))
N_INTERVALOS = int(diferencia_horas/(INTERVALO/60))

print(N_INTERVALOS)