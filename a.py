from datetime import datetime
now = datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

dt1 = dt_string.split(' ')
dt2 = dt1[0]
dt3 = dt2.split('/')
dt4 = dt3[0]
print(dt4)