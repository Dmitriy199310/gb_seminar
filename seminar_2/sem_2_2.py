# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

def dictionary (n):
    dict = {i : (3*i+1) for i in range (1, n+1)}
    return dict
print (dictionary (int (input ('Введите целое число: '))))
