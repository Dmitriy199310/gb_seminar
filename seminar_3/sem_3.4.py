# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def dec_to_cc (n, cc):
    remainder  = 0 
    l = ''
    while n >= cc:
        remainder = n % cc
        n = n // cc
        l = f'{remainder}' + l
    l =f'{n}' + l
    return l

print (dec_to_cc(int(input('Введите десятичное число для преобразования: ')),2))