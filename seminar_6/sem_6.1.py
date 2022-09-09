# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

s = input ('Введите строку: ').split()
print(' '.join([index  for index in s if 'абв' not in index]))