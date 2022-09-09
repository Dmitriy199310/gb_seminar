# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
def create_list (amount):
    l_1 =[]
    for index in range (amount):
        l_1.append (int (input('Введите число: ')))
    return l_1

def repeat_element (n):
    a = {i  for i in create_list(n)}
    return a

print (repeat_element(int(input('Введите количество элементов: '))))
    
