from tkinter import N
from unittest import result


def dec_to_cc (n, cc):
    remainder  = 0 
    l = ''
    while n >= cc:
        remainder = n % cc
        n = n // cc
        l = f'{remainder}' + l
    l =f'{n}' + l
    return l
print (dec_to_cc(16,2))

