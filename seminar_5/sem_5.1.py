# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def delete (s):
    result = ''
    for i in s.split():
        if 'абв' not in i:
            result += i + ' '
    return result

print(delete(input(' ')))