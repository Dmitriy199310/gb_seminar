#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

def n_multiplication (n):
    l = []
    for index_1 in range (1, n+1):
        mult = 1
        for index_2 in range (1, index_1+1):
            mult *= index_2
        l.append (mult)
    return l
print (n_multiplication(int(input ('Введите целое число: '))))