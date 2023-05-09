#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime
import calendar
def get_user_birthday():
    year = int(input('When is your birthday? [YY] '))
    month = int(input('When is your birthday? [MM] '))
    day = int(input('When is your birthday? [DD] '))

    birthday = datetime(year,month,day)
    return birthday

def calculate_dates(original_date, now):
    delta1 = datetime(now.year, original_date.month, original_date.day)
    delta2 = datetime(now.year+1, original_date.month, original_date.day)
    return ((delta1 if delta1 > now else delta2) - now).days
name=input('What is your Name ?')
bd = get_user_birthday()
now = datetime.now()
c = calculate_dates(bd, now)
day_names = [i for i in calendar.day_name]
day = day_names[day_of_week]
print(f'{name} was born on a {day}')
print(c)

