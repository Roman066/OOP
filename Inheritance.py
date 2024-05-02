# Класс студентов
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, specific_lecturer, course, grade):
        if isinstance(specific_lecturer, Lecturer) \
            and course in specific_lecturer.courses_attached \
            and course in self.courses_in_progress \
            and 0 < grade < 10:

            specific_lecturer.grades.append(grade)

        else:
            return 'Ошибка'

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade(self.grades)}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'

    def __lt__(self, other_student):
        if isinstance(other_student, Student):
            return average_grade(self.grades) < average_grade(other_student.grades)
        else:
            return None

# Класс преподователей
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

# Класс лекторов
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        self.courses_attached = []

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade(self.grades)}'
        return output

    def __lt__(self, other_lecturer):
        if isinstance(other_lecturer, Lecturer):
            return average_grade(self.grades) < average_grade(other_lecturer.grades)
        else:
            return None

# Класс экспертов
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, specific_student, course, grade):
        if isinstance(specific_student, Student) \
            and course in self.courses_attached \
            and course in specific_student.courses_in_progress:

            if course in specific_student.grades:
                specific_student.grades[course] += [grade]
            else:
                return 'Ошибка'

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}'
        return output
