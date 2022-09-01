# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

list = []
for i in range(5):
    number = int(input('Введите число: '))
    list.append(number)
print(max(list))

# maxx = list[0]
# for j in list:
#     if j>maxx:
#         maxx = j
# print(maxx)

# maxx = int(input('Введите число: '))
# for i in range(4):
#     number = int(input('Введите число: '))
#     if number > maxx:
#         maxx = number

# print(maxx)


