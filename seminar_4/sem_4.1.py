# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def simple_multiplier (n):
    l = []
    index_1 = 1
    while(index_1 <= n):
        count = 0
        if(n % index_1 == 0):
            index_2 = 1
            while(index_2 <= index_1):
                if(index_1 % index_2 == 0):
                    count += 1
                index_2 += 1
            if (count == 2):
                l.append(index_1)
        index_1 += 1
    return l

print (simple_multiplier(int(input('Введите натуральное число: '))))