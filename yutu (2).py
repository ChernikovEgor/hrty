
list = [1, 2, 3]
answer = 0
print(f"Находим сумму квадратов данных чисел {list}")
for i in range(len(list)):
    answer = list[i] * list[i] + answer
print(f"Ответ: {answer}")

