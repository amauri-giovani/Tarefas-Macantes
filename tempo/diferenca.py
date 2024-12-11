import datetime, time
from datetime import datetime, timedelta

now = datetime.now() + timedelta(hours=2, minutes=2)

while(True):
    horaSistema = datetime.now()
    delta = now - horaSistema
    if now > horaSistema:
        print ('Diferenca de: ', delta)
        time.sleep(3)
    else:
        print ('Terminado a impressao')
        break