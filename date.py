# To get current date and time 
# We import datetime library
from datetime import datetime, timedelta

current_date = datetime.now()
today = datetime.now()
print('Today is: '+str(current_date))

#timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

#formatting date
print()
print('Simplified Date format')
_date = datetime.now()

print('Day: ' +str(_date.day))
print('Month: ' +str(_date.month))
print('Year: '+str(_date.year))
print()

# convert string to date

birthday = input('When is your birthday (dd/mm/yyyy)?')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print ('birthday: '+ str(birthday_date))
one_week = timedelta(days=7)
week_to_birthday = birthday_date - one_week
print('Week before birthday: ' + str(week_to_birthday))