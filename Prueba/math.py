import math
from turtle import *
def hearta(k):
    return 15*math.sin(k) **3
def heartb(k):
    return 12 * math.cos(k) - 5 *\
math.cos(2 * k) - 2 * \
math.cos(3 * k) - \
math.cos(4 * k)
speed(90000)
bgcolor("black")
for i in range(9000):
    goto(hearta(i) *20, heartb(i) *28)
    for j in range(5):
        color ("#0026FF")
        goto(0,0)