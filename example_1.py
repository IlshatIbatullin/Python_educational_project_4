# s = 'Это обычная строка, а в ней адрес почты golos@mail.ru'
# words = s.split()
# for w in words:
#     n = w.find('mail.ru')
#     if n != -1:
#         print('В строке присутствует емайл: ' +str(w))

# a = ""
# b = "bar"
# # пусть a и b - переменные, которые мы хотим проверить
# if a and b: # проверка истинности обеих переменных
#     print("Обе переменные истинные")
#     print(a,b)

# a = int(input('Введите число: \n')) # 666 удовлетворяет, 99 не удовлетворяет
# if type(a) == int:
#     if 100 <= a <= 999:
#         if a % 2 == 0:
#             if a % 3 == 0:
#                 print("Число удовлетворяет условиям")
# else:
#     print("Число не удовлетворяет условиям")

# a = int(input('Введите число: \n')) # 666 удовлетворяет, 99 не удовлетворяет
# if type(a) == int and 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
#     print("Число удовлетворяет условиям")
# else:
#     print("Число не удовлетворяет условиям")

# a = int(input('Введите числа: \n'))
# s = []

# L = list(map(int, input().split()))
#
# print(all(L))

# M = [[i+j for j in range(1, 11)] for i in range(1, 11)]
# print(M)

# M = [[i+j for j in range(1, 11)] for i in range(1, 11)]
# for i in M:
#     print(i)

# T = [[i*j for j in range(1,11)] for i in range(1,11)]
# print(T)

# L = [i for i in range(10)]  # 0 1 2 3 4 5 6 7 8 9
# M = [i for i in range(10,0,-1)]  # 10 9 8 7 6 5 4 3 2 1

# N = [ ]
# for i in range(10):
#     N.append(L[i] * M[i])
# print(N)

# for a, b in zip(L,M):
#     print('a =', a, 'b =', b)

# N = [a*b for a,b in zip(L,M)]
# print(N)

text = input()  # получаем строку

first = text[0]  # сохраняем первый символ
count = 0  # заводим счетчик
result = ''  # и результирующую строку

for c in text:
    if c == first:  # если символ совпадает с сохраненным,
        count += 1  # то увеличиваем счетчик
    else:
        result += first + str(count)  # иначе - записываем в результат
        first = c  # и обновляем сохраненный символ с его счетчиком
        count = 1

result += first + str(count)  # и добавляем в результат последний символ
print(result)
#t_13.8.1
