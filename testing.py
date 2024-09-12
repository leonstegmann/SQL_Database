#!/usr/bin/env python3

from random import randrange
import datetime 


def random_date(i):
    current = datetime.datetime(2013, 9, 20,13,00)
    current = current - i* datetime.timedelta(minutes=randrange(10))
    return current


rdate = random_date(1)

print(rdate)
