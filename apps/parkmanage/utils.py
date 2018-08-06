#_*_coding:utf-8_*_
import random

def get_lottery_num():

    a = 0
    b = 100
    c = [random.radnint(a,b) for _ in range(3)]
    return c