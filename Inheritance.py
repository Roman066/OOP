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

# Класс преподователей
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
# Класс лекторов
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        self.courses_attached = []

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
