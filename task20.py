arr = {1:"AEIOULNSTRАВЕИНОРСТ",
                2:"DGДКЛМПУ",
                3:"BCMPБГЁЬЯ",
                4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",
                8:"JXШЭЮ",
                10:"QZФЩЪ"}

input = input("Введите слово: ").upper()
sum = 0
for i in input:
    for j, d in arr.items():
        if i in d:
            sum += j
print(f"Стоимость слова: {sum}")