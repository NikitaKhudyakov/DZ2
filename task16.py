n = int(input("Размер: "))
numb = int(input("Введите число которое будем искать: "))
index = 0
list_1 = []
for i in range(n):
    array = int(input("Введите массив: "))
    list_1.append(array)
    if  array == numb:
        index+=1
print(list_1)
print(f"Встречаются {index} раз")   

