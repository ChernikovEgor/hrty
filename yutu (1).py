list = "Hello world"
print(f"Дана строка: {list}")
for i in range(len(list)):
    if list[i] == " ":
        list = list.replace(list[i + 1], list[i + 1].upper(), 1)
print(f"Стало: {list}")

