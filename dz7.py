"""Написать рекурсивную функцию, принимающую число n и
рассчитывающую сумму всех нечетных чисел от 1 до n.
"""

def ex1(n):
    if n <= 1:
        return n
    if n % 2 != 0:
        return n + ex1(n - 2)
    return ex1(n - 1)

# print("sum: 0 =", ex1(0))
# print("sum: 1 =", ex1(1))
# print("sum: 1 + 3 + 5 =", ex1(5))
# print("sum: 1 + 3 + 5 + 7 + 9 =", ex1(1500))


"""Написать программу: Учет оценок. Программа должна иметь 
возможность добавления ученика, предметов и оценок.

Также реализовать вывод, изменение и удаление данных. 
Все данные хранить в текстовом файле. """

def ex2():
    import os
    import time
    import pyfiglet

    FILE_NAME = "base.txt"
    LINE = "*" * 72

    def start_program():
        title_start = pyfiglet.figlet_format("SCHOOL  RECORD")
        print(title_start)
        print(LINE)
        string = f"{{0:^{len(LINE)}}}"
        print(string.format("Программа учета оценок"))
        print(LINE)
        # Создать файл если отсутствует
        if not os.path.exists(FILE_NAME):
            file = open(FILE_NAME, "w")
            file.close()
        time.sleep(2)

    def end_program():
        screen_clear()
        title_finish = pyfiglet.figlet_format("THE END")
        print(title_finish)
        time.sleep(2)
        screen_clear()

    def screen_clear():
        if os.name == 'nt':
            os.system('cls')  # Windows
        elif os.name == 'posix':
            os.system("clear")  # Mac os

    def base_write(main_base, classes, filename):
        print_title("База успешно обновлена!")
        with open(filename, "w", encoding='utf-8') as file:
            print(main_base, classes, sep=", ", end="", file=file)

    def base_read(filename):
        with open(filename, "r", encoding='utf-8') as file:
            data = file.read()
            if data:
                return eval(data)
        return {}, []

    def get_main_menu():
        menu = pyfiglet.figlet_format("MAIN  MENU")
        menu += LINE
        string = f"\n{{0:^{len(LINE)}}}\n"
        menu += string.format("Возможные действия:")
        menu += LINE
        menu += "\n1 - Вывести журнал на экран\n"
        menu += "2 - Вывести список предметов\n3 - Добавить предмет\n"
        menu += "4 - Вывести список учеников\n5 - Добавить ученика\n"
        menu += "6 - Добавить/Изменить оценку\n7 - Удалить предмет\n"
        menu += "8 - Удалить оценку\n9 - Удалить ученика\n"
        menu += LINE
        menu += "\n0 - Выход\n"
        menu += LINE
        return menu

    def print_title(title):
        print(LINE)
        string = f"{{0:^{len(LINE)}}}"
        print(string.format(title))
        print(LINE)

    def get_classes(main_base):
        classes = []
        for user in main_base:
            classes.extend(main_base[user].keys())
        return classes

    def print_users(main_base):
        if len(main_base) > 0:
            users = sorted(main_base)
            for start in range(0, len(users), 20):
                end = start + 20 if len(users) - start > 20 else len(users)
                screen_clear()
                print_title("Список учеников:")
                for id in range(start, end):
                    print(id + 1, users[id])
                print(LINE)
                if end != len(users):
                    input("Нажмите Enter для продолжения")
        else:
            print("В базе еще нет учеников!")
        input("Нажмите Enter для возврата в меню")

    def print_classes(classes):
        if len(classes) > 0:
            for start in range(0, len(classes), 20):
                end = start + 20 if len(classes) - start > 20 else len(classes)
                screen_clear()
                print_title("Список Предметов:")
                for id in range(start, end):
                    print(id + 1, classes[id])
                print(LINE)
                if end != len(classes):
                    input("Нажмите Enter для продолжения")
        else:
            print("В базе еще нет предметов!")
        input("Нажмите Enter для возврата в меню")

    def choice_user(main_base, title):
        while True:
            screen_clear()
            print_title(title)
            user = input("Введите Фамилию и Имя или 'все' - показать весь список:")
            user = user.title()
            if user == "Все":
                print_users(main_base)
            elif user in main_base:
                return user
            else:
                choice = input("Ученик в базе не найден. Повторить ввод? (да/нет): ")
                if choice.lower() not in ["y", "yes", "д", "да"]:
                    return ""

    def choice_class(classes, title):
        while True:
            screen_clear()
            print_title(title)
            q = "Введите название предмета или 'все' - показать весь список: "
            subject = input(q)
            subject = subject.capitalize()
            if subject == "Все":
                print_classes(classes)
            elif subject in classes:
                return subject
            else:
                choice = input("Предмет в базе не найден. Повторить ввод? (да/нет): ")
                if choice.lower() not in ["y", "yes", "д", "да"]:
                    return ""

    def print_records(main_base, classes):
        line = f"|:{'-' * (len(LINE) - 13)}:|:{'-' * 6}:|"
        string = f"|{{0:^{len(LINE) - 11}}}|{{1:^8}}|"

        def print_records_by_user():
            user = choice_user(main_base, "Выбор ученика для поиска")
            if user:
                screen_clear()
                print_title(f"Список оценок для {user}")
                print(line)
                print(string.format("Предмет", "Оценка"))
                print(line)
                for subject in sorted(main_base[user]):
                    print(string.format(subject, main_base[user][subject]))
                print(line)
                input("Нажмите Enter для возврата в меню")

        def print_records_by_class():
            subject = choice_class(classes, "Выбор предмета для поиска")
            if subject:
                screen_clear()
                print_title(f"Список оценок по предмету {subject}")
                print(line)
                print(string.format("Фамилия Имя", "Оценка"))
                print(line)
                for user in sorted(main_base):
                    if subject in main_base[user]:
                        print(string.format(user, main_base[user][subject]))
                print(line)
                input("Нажмите Enter для возврата в меню")

        def print_records_all():
            len_fio = max((len(user) for user in main_base))
            len_class = max((len(subj) for subj in classes))
            line = f"|:{'-' * 3}:|:{'-' * (len_fio - 2)}:|" \
                   + f":{'-' * (len_class - 2)}:|" * len(classes)
            string = f"|{{:^5.5}}|{{:^{len_fio}}}|" \
                     + f"{{:^{len_class}}}|" * len(classes)
            users = sorted(main_base)
            for start in range(0, len(users), 20):
                end = start + 20 if len(users) - start > 20 else len(users)
                screen_clear()
                print_title(f"Содержимое журнала")
                print(line)
                print(string.format("№", "Фамилия Имя", *classes))
                print(line)
                for i in range(start, end):
                    grades = []
                    for subject in classes:
                        if subject in main_base[users[i]]:
                            grades.append(main_base[users[i]][subject])
                        else:
                            grades.append("-")
                    print(string.format(str(i + 1), users[i], *grades))
                print(line)
                if end != len(users):
                    input("Нажмите Enter для продолжения")
            input("Нажмите Enter для возврата в меню")

        if len(main_base) == 0 or len(classes) == 0:
            return input("База пуста! Нажмите Enter для возврата в меню")
        while True:
            screen_clear()
            print_title("Выберите формат вывода записей:")
            print("1 - По ученику")
            print("2 - По предмету")
            print("3 - Весь журнал")
            print_title("0 - Вернуться в главное меню")
            choice = input("Ваш выбор: ")
            if choice == "0":
                return
            elif choice == "1":
                return print_records_by_user()
            elif choice == "2":
                return print_records_by_class()
            elif choice == "3":
                return print_records_all()
            else:
                print("Выбор не распознан. Повторите ввод!")
                time.sleep(2)

    def add_class(main_base, classes, filename):
        screen_clear()
        print_title("Добавление предмета")
        new_subject = input("Введите название нового предмета:")
        new_subject = new_subject.capitalize()
        if new_subject not in classes:
            classes.append(new_subject)
            classes.sort()
            base_write(main_base, classes, filename)
            choice = input("Успешно добавлен! Добавить еще? (да/нет): ")
        else:
            choice = input("Предмет уже в базе. Добавить еще? (да/нет): ")
        if choice.lower() in ["y", "yes", "д", "да"]:
            add_class(main_base, classes, filename)

    def add_user(main_base, classes, filename):
        screen_clear()
        print_title("Добавление ученика")
        new_user = input("Введите Фамилию и Имя нового ученика: ")
        new_user = new_user.title()
        if new_user not in main_base:
            main_base[new_user] = {}
            base_write(main_base, classes, filename)
            choice = input("Успешно добавлен! Добавить еще? (да/нет): ")
        else:
            choice = input("Ученик уже в базе. Добавить еще? (да/нет): ")
        if choice.lower() in ["y", "yes", "д", "да"]:
            add_user(main_base, classes, filename)

    def add_or_edit_grade(main_base, classes, filename):
        title = "Добавление/Изменение оценки для"
        if (not (user := choice_user(main_base, f"{title} ученика")) or
                not (subject := choice_class(classes, f"{title} {user}"))):
            return
        while True:
            screen_clear()
            print_title(f"{title} {user}")
            grade = input(f"Введите оценку по {subject} (1-5): ")
            if grade in "12345":
                main_base[user][subject] = grade
                base_write(main_base, classes, filename)
                choice = input("Успешно добавлена. Добавить еше? (да/нет): ")
                if choice.lower() not in ["y", "yes", "д", "да"]:
                    return
                if not (subject := choice_class(classes, f"{title} {user}")):
                    return
            else:
                choice = input("Некорректная оценка. Повторить ввод? (да/нет): ")
                if choice.lower() not in ["y", "yes", "д", "да"]:
                    return

    def del_grade(main_base, classes, filename):
        if (not (user := choice_user(main_base, "Удаление оценки для ученика")) or
                not (subject := choice_class(classes, f"Удаление оценки для {user}"))):
            return
        if subject in main_base[user]:
            grade = main_base[user].pop(subject)
            base_write(main_base, classes, filename)
            input(f"Оценка {grade} по предмету {subject} удалена. Нажмите Enter.")
        else:
            input(f"Оценка по предмету {subject} не найдена. Нажмите Enter.")

    def del_class(main_base, classes, filename):
        if not (subject := choice_class(classes, f"Удаление предмета")):
            return
        choice = input(f"Действительно хотите удалить {subject}? (да/нет): ")
        if choice.lower() not in ["y", "yes", "д", "да"]:
            return
        for user in main_base:
            if subject in main_base[user]:
                main_base[user].pop(subject)
        classes.remove(subject)
        base_write(main_base, classes, filename)
        input(f"Предмет {subject} удален. Нажмите Enter.")

    def del_user(main_base, classes, filename):
        user = choice_user(main_base, "Удаление ученика")
        if user:
            choice = input(f"Действительно хотите удалить {user}? (да/нет): ")
            if choice.lower() in ["y", "yes", "д", "да"]:
                main_base.pop(user)
                # del main_base[user]
                base_write(main_base, classes, filename)
                input(f"Ученик {user} удален! Нажмите Enter.")

    start_program()
    base, list_classes = base_read(FILE_NAME)
    list_classes = sorted(set(list_classes + get_classes(base)))
    menu = get_main_menu()

    run = True
    while run:
        screen_clear()
        print(menu)
        choice = input("Ваш выбор: ")
        if choice == "0":
            print("Завершение работы....")
            run = False
        elif choice == "1": print_records(base, list_classes)
        elif choice == "2": print_classes(list_classes)
        elif choice == "3": add_class(base, list_classes, FILE_NAME)
        elif choice == "4": print_users(base)
        elif choice == "5": add_user(base, list_classes, FILE_NAME)
        elif choice == "6": add_or_edit_grade(base, list_classes, FILE_NAME)
        elif choice == "7": del_class(base, list_classes, FILE_NAME)
        elif choice == "8": del_grade(base, list_classes, FILE_NAME)
        elif choice == "9": del_user(base, list_classes, FILE_NAME)
        else: print("Выбор не распознан. Повторите ввод!")
        time.sleep(2)
    # end_program()

def ex2_2():
    import os

    FILE_NAME = "data.txt"
    select = input("просмотор даннных - 1\nдобавление данных - 2\nочистить данные - 3\nизменить данные - 4\n")
    if select == '1':
        if os.path.isfile(FILE_NAME):
            with open(FILE_NAME, 'r') as file:
                fileRead = file.read()
            if fileRead:
                fileRead = eval(fileRead)
                for student, lesson in fileRead.items():
                    print('\t' + student)
                    for lesson, raiting in lesson.items():
                        print(lesson, raiting, sep=': ')
            else:
                print("в файле еще нет данных")
        else:
            print("ошибка открытия файла")
    elif select == '2':
        if os.path.isfile(FILE_NAME):
            with open(FILE_NAME, 'r') as file:
                fileRead = file.read()
            if fileRead:
                fileRead = eval(fileRead)
            else:
                fileRead = {}
            student = input("введите имя ученика ")
            lesson = input("введите предмет ")
            raiting = input("введите оценку ")
            if student in fileRead:
                fileRead[student].update({lesson: raiting})
            else:
                fileRead[student] = {lesson: raiting}
            with open(FILE_NAME, 'w') as file:
                file.write(str(fileRead))
                print("данные успешно добавлены!")
    elif select == '3':
        open(FILE_NAME, 'w').close()
    elif select == '4':
        if os.path.isfile(FILE_NAME):
            with open(FILE_NAME, 'r') as file:
                fileRead = file.read()
            if fileRead:
                fileRead = eval(fileRead)
                name = input("введите имя ученика, чьи данные хотите изменить ")
                if name in fileRead:
                    now_lesson = input("введите предмет который хотите изменить ")
                    if now_lesson in fileRead[name]:
                        now_raiting = input("введите оценку, которую хотите изменить ")
                        if now_raiting in fileRead[name][now_lesson]:
                            new_lesson = input("введите новый предмет ")
                            new_raiting = input("введите новую оценку ")
                            fileRead[name].pop(now_lesson)
                            fileRead[name].update({new_lesson: new_raiting})
                            with open(FILE_NAME, 'w') as file:
                                file.write(str(fileRead))
                                print("данные успешно обновлены")
                        else:
                            print("у ученика нет таких оценок")
                    else:
                        print("такого предмета нет у ученика")
                else:
                    print("такого ученика нет")
    else:
        print("такого варианта нет")

ex2()
# ex2_2()