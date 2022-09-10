dict_basa = {"Фамилия Имя": {"Предмет1": 5, "Предмет2": 5},
             "Фамилия2 Имя2": {"Предмет1": 5, "Предмет2": 5}}

list_sub = {"Предмет1", "Предмет2"}
# добавить ученика
dict_basa["Фамилия3 Имя3"] = {}
# добавить предмет
list_sub.add("Предмет3")
# добавить оценку
sub = input("Введите предмет: ").title()  # Русский язык
if sub in list_sub:
    user = input("Введите ФИ: ").capitalize()  # Фамилия Имя
    if user in dict_basa:
        dict_basa[user][sub] = int(input("Введите оценку: "))
    else:
        print("Ученика в базе нет")
else:
    print("Предмета в базе нет")


file = open("base_test.txt", "w", encoding='utf-8')
print(dict_basa, list_sub, sep=", ", end="", file=file)
file.close()

file2 = open("base_test.txt", "r", encoding='utf-8')
data = file2.read()
dict_basa2, list_sub2 = eval(data)
file2.close()
print(dict_basa2)
print(list_sub2)
