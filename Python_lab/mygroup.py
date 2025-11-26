groupmates = [
    {
        "name": "Александр",
        "surname": "Александрович",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 5, 5],
    },
    {
        "name": "Анна",
        "surname": "Афанасьева",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 3, 5],
    },
    {
        "name": "Иван",
        "surname": "Будников",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [3, 3, 4],
    },
    {
        "name": "Савелий",
        "surname": "Булгаров",
        "exams": ["КТП", "Программирование 1С", "ПИС"],
        "marks": [5, 4, 3],
    },
    {
        "name": "Георгий",
        "surname": "Данилов",
        "exams": ["КТП", "ПИС", "Философия"],
        "marks": [4, 4, 4],
    },
]


def print_students(students):
    print(
        "Имя".ljust(15), "Фамилия".ljust(20), "Экзамены".ljust(38), "Оценки".ljust(20)
    )
    for student in students:
        print(
            student["name"].ljust(15),
            student["surname"].ljust(20),
            str(student["exams"]).ljust(38),
            str(student["marks"]).ljust(20),
        )


print_students(groupmates)


def filter_students_by_average(students, min_average):
    filtered = []
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg > min_average:
            filtered.append(student)
    return filtered


try:
    print()
    threshold = float(input("Введите минимальный средний балл для фильтрации: "))
    filtered_group = filter_students_by_average(groupmates, threshold)
    if filtered_group:
        print(f"\nСтуденты со средним баллом выше {threshold}:")
        print_students(filtered_group)
    else:
        print(f"\nНет студентов со средним баллом выше {threshold}.")
except ValueError:
    print("Ошибка: введите корректное число.")
