#calculo de hora actual v1
#julio alaniz
#**********importar**********
from datetime import datetime
now = datetime.now()
#**********variables*********
hora = now.hour
minuto = now.minute
hora2 = now.hour +2
#**********aplicacion********
print("\n\nla hora actual es: \n", hora, ":", minuto, "\n\n")

