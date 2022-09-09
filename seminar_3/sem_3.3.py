# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def create_list (amount):
    l_1 =[]
    for index in range (amount):
        l_1.append (float (input('Введите число: ')))
    return l_1

def min_max (n):
    l_2 = create_list(n)
    min = round(l_2[0] - int(l_2[0]), 2)
    max = round(l_2[0] - int(l_2[0]), 2)
    for i in range (1,n):
        if l_2[i] - int(l_2[i]) > max:
            max = round(l_2[i] - int(l_2[i]),2)
        if l_2[i] - int(l_2[i]) < min:
            min = round (l_2[i] - int(l_2[i]),2)
    return max-min

print (min_max(int(input('Введите количество чисел в последовательности: '))))