# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
def create_list (amount):
    l_1 =[]
    for index in range (amount):
        l_1.append (int (input('Введите число: ')))
    return l_1

def sum_element_position_odd(n):
    l = create_list(n)
    s = 0
    for i in range (1, n, 2):
        s += l[i]
    return s
    


print (sum_element_position_odd(int(input('Введите количество элементов: '))))
    