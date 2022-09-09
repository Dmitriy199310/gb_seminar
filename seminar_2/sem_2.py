# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# def sum_variables (n : list):
#     for index_2 in range (n):
#         if index_2 % 2 != 0:
#             s += n[index_2]
#     return s

# def n_list (quantity):
#     l = []
#     for index_1 in range (quantity):
#         l.append (print(int(input('Введите целое число: '))))
#     return sum_variables (l)
# print (n_list(int(input('Введите целое число: '))))


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.


# from random import randint

# def create_list (amount):
#     l_1 = []
#     for index in range(amount):
#         l_1.append(randint (1,50))
#     print (l_1)
#     return l_1

# def multiplication_list (n):
#     k = create_list(n)
#     l_2 = []
#     for i in range(0, len(k) // 2):
#         l_2.append (k[i]*k[-1-i])
#     if len(k) % 2 !=0: 
#         l_2.append(k[len(k)//2]**2)
#     return l_2

# print (multiplication_list(int(input('Введите количество чисел в последовательности: '))))


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def create_list (amount):
    l_1 =[]
    for index in range (amount):
        l_1.append (float (input('Введите число: ')))

def min_max (n):
    l_2 = create_list(n)
    min = int (l_2[0])
    max = int (l_2[0])
    for i in range (1,n):
        if int (l_2[i]) > max:
            max = int (l_2[i])
        if int(l_2[i]) < min:
            min = int(l_2[i])
    return max-min

print (min_max(int(input('Введите количество чисел в последовательности: '))))