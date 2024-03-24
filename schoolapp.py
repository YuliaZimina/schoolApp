# Определение класса "Student" для представления ученика
class Student:
    # Метод инициализации класса, который вызывается при создании нового объекта класса
    def __init__(self, full_name, grade, username, password):
        # Имя ученика
        self.full_name = full_name
        # Класс ученика
        self.grade = grade
        # Логин ученика
        self.username = username
        # Пароль ученика
        self.password = password


# Определение класса "Discipline" для представления предмета
class Discipline:
    # Метод инициализации класса
    def __init__(self, name, description, priority):
        # Название предмета
        self.name = name
        # Описание предмета
        self.description = description
        # Приоритет предмета
        self.priority = priority
        # Список заданий по предмету
        self.tasks = []

    # Метод для добавления задания к предмету
    def add_task(self, task):
        self.tasks.append(task)

    # Метод для удаления задания из предмета
    def remove_task(self, task):
        self.tasks.remove(task)


# Определение базового класса "Task" для представления задания
class Task:
    # Метод инициализации класса
    def __init__(self, task_type, content, answers=None, grade=None, comments=None):
        # Тип задания (например, домашнее задание, контрольная работа)
        self.task_type = task_type
        # Содержание задания
        self.content = content
        # Ответы на задание
        self.answers = answers
        # Оценка за задание (по умолчанию None)
        self.grade = grade
        # Комментарии к заданию (по умолчанию None)
        self.comments = comments


# Определение подкласса "Homework" для представления домашнего задания
class Homework(Task):
    # Метод инициализации класса
    def __init__(self, content, answers=None, grade=None, comments=None):
        # Вызов конструктора базового класса "Task" с указанием типа задания "Homework"
        super().__init__('Домашняя работа', content, answers, grade, comments)


# Определение подкласса "Exam" для представления контрольной работы
class Exam(Task):
    # Метод инициализации класса
    def __init__(self, content, answers=None, grade=None, comments=None):
        # Вызов конструктора базового класса "Task" с указанием типа задания "Exam"
        super().__init__('Контрольная работа', content, answers, grade, comments)


# Определение подкласса "IndependentWork" для представления самостоятельной работы
class IndependentWork(Task):
    # Метод инициализации класса
    def __init__(self, content, answers=None, grade=None, comments=None):
        # Вызов конструктора базового класса "Task" с указанием типа задания "Independent Work"
        super().__init__('Самостоятельная работа', content, answers, grade, comments)


# Определение класса "SubjectWork" для представления работы по предмету
class SubjectWork:
    # Метод инициализации класса
    def __init__(self, discipline):
        # Предмет, к которому относится работа
        self.discipline = discipline
        # Домашнее задание по предмету
        self.homework_list = []
        # Список контрольных работ
        self.exams = []
        # Список самостоятельных работ
        self.independent_works = []


    # Метод для добавления домашней работы
    def add_homework(self, homework):
        self.homework_list.append(homework)

    # Метод для добавления контрольной работы
    def add_exam(self, exam):
        self.exams.append(exam)

    # Метод для добавления самостоятельной работы
    def add_independent_work(self, independent_work):
        self.independent_works.append(independent_work)

    #Метод для получения списка всех заданий по предмету
    def get_tasks(self):
        return self.homework_list+self.exams+self.independent_works


# Создание ученика
student = Student("Иванов Иван Иванович", "11A", "ivanov_ii", "password123")

'''Внесение предмета математки и заданий к нему'''
# Создание предмета
math_discipline = Discipline("Математика", "Описание курса математики", "Высокий приоритет")

# Создание работы по предмету
math_work = SubjectWork(math_discipline)

# Добавление домашнего задания
math_homework = Homework("Посчитать количество углов в треугольнике","В треугольнике 3 угла",grade=2)
math_work.add_homework(math_homework)
math_homework = Homework("гл.3, c.97, упр. 22-33")
math_work.add_homework(math_homework)
# Добавление контрольной работы
math_exam = Exam("Контрольная работа по таблице умножения", grade=3)
math_work.add_exam(math_exam)

# Добавление самостоятельной работы
math_independent_work = IndependentWork("Решить одну из нерешенных математических проблем", grade=5)
math_work.add_independent_work(math_independent_work)

# Добавление работы по предмету к предмету
math_discipline.add_task(math_work)

# Вывод информации о предмете
print("Предмет:", math_discipline.name)
print("Описание:", math_discipline.description)
print("Приоритет:", math_discipline.priority)
print("Список заданий:")
for task in math_work.get_tasks():
    print("Тип задания:", task.task_type)
    print("Содержание:", task.content)
    #выводим информацию о задании только если она заполнена
    if task.answers:
        print("Ответы:", task.answers)
    if task.grade:
        print("Оценка:", task.grade)
    if task.comments:
        print("Комментарии:", task.comments)
    print()

