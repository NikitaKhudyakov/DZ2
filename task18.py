n = int(input("Размер: "))
numb = int(input("Введите число которое будем сравнивать: "))
list_1 = []
list_min = []
for i in range(n):
    array = int(input("Введите массив: "))
    list_1.append(array)

    # нахожу разницу между значениями
    a = abs(numb - list_1[i])         

    list_min.append(a)
for i in range(len(list_min)):
    if list_min[i] == min(list_min):
        index = i 
print(f"Самый близкий по величине элемент в массиве - {list_1}, к заданному числу {numb} - {list_1[index]}! ")

