# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint

def create_list (amount):
    l_1 = []
    for index in range(amount):
        l_1.append(randint (1,50))
    print (l_1)
    return l_1

def multiplication_list (n):
    k = create_list(n)
    l_2 = []
    for i in range(0, len(k) // 2):
        l_2.append (k[i]*k[-1-i])
    if len(k) % 2 !=0: 
        l_2.append(k[len(k)//2]**2)
    return l_2

print (multiplication_list(int(input('Введите количество чисел в последовательности: '))))