from datetime import datetime

repeat = True
list = [1, 2, 3]
while repeat:
    print(f"Сейчас в списке {list}")
    for i in range(len(list)):
        list[i] = list[i] * 2
    print(f"Стало {list}")
    TaskOne = int(input("\n1. Продолжить умножение \n2. Выйти\n"))
    if TaskOne == 2:
        repeat = False

