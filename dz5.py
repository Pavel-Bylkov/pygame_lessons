"""Создать функцию, принимающую год, и возвращающую является
ли данных год високосным."""
def is_spec_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return "YES"
    return "NO"

# print("2020 -", is_spec_year(2020))
# print("2022 -", is_spec_year(2022))
# print("1700 -", is_spec_year(1700))
# print("1600 -", is_spec_year(1600))

"""Создать функцию, принимающую список целых чисел и возвращающую, 
сумму всех элементов, сумму всех четных элементов, а также разность 
между самым большим и самым маленьким элементами списка."""
def ex2(nums):
    return sum(nums), sum((x for x in nums if x % 2 == 0)), max(nums) - min(nums)

#
# nums = [-10, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# all, even, delta = ex2(nums)
# print(f'Сумма всех эл.: {all}\nСумма четных эл.: {even}\nДельта: {delta}')


"""Написать функцию, которая принимает строку, и записывает её в 
текстовый файл. При запуске программы в консоль должен выводиться 
текст из текстового файла. (Текстовый файл можно создать вручную, 
чтобы при запуске не возникала ошибка о отсутствии данного файла)."""

def ex3(text):
    # file_name = text if len(text) < 7 else text[:6]
    file_name = 'text_file.txt'
    with open(file_name, 'w') as file:
        file.write(text)
    # print(f"Строка - {text}\nуспешно записана в файл '{file_name}'")


# ex3("Python - is the best of the best!")
# ex3("blabla text")
# ex3("examle text")
# with open("text_file.txt", "r") as file:
#     print(file.read())
