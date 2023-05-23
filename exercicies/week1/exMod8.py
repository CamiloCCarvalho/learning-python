import datetime
import random

# MODULO 8 - EX01
double_value = lambda value: value * 2

# MODULO 8 - EX02
date_now = f'{random.randint(0, 31)}/{random.randint(1, 12)}/{random.randint(1500, 2050)}'

def day_now(date):
    list_months = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    datas = date.split('/')
    month = int(datas[1])
    return print(f'{datas[0]} {list_months[month-1]} {datas[2]}')

print(date_now)
day_now(date_now)
