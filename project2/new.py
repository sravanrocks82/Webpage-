from datetime import datetime,timedelta

current_date=datetime.now()
activation_date=datetime(2020, 1, 1)
def sync(activation_date):
    while activation_date<=current_date:
        activation_date=activation_date+timedelta(90)
    return activation_date
m=datetime(2020, 9, 1) 
sync(m)