class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, mentor, course, grade):
        if isinstance(mentor, Mentor) and course in mentor.courses_attached and course in self.courses_in_progress:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_score(self):
        k = 0
        s = 0
        for mark in self.grades.values():
            k += len(mark)
            s += sum(mark)
        if k != 0:
            return s / k
        else:
            return 0


    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Error')
            return
        return self._average_score() < other._average_score()


    def __str__(self):
        res1=' '.join(self.courses_in_progress)
        res2=' '.join(self.finished_courses)
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self._average_score()}\nКурсы в процессе изучения: {res1} \nЗавершенные курсы: {res2}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def _average_course_score(self):
        k = 0
        s = 0
        for mark in self.grades.values():
            k += len(mark)
            s += sum(mark)
        if k != 0:
            return s / k
        else:
            return 0


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Error')
            return
        return self._average_course_score() < other._average_course_score()


    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за курсы: {self._average_course_score()}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


best_student1 = Student('Ruoy', 'Eman', 'your_gender')
best_student1.courses_in_progress += ['Python']
best_student1.finished_courses += ['Введение в программирование']

best_student2 = Student('Kevin', 'McCalister', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.finished_courses += ['Введение в программирование']

cool_lecturer1 = Lecturer('Some', 'Buddy')
cool_lecturer1.courses_attached += ['Python']

cool_lecturer2 = Lecturer('Emma', 'Watson')
cool_lecturer2.courses_attached += ['Python']

cool_reviewer1 = Reviewer('Rob', 'Shnider')
cool_reviewer1.courses_attached += ['Python']

cool_reviewer2 = Reviewer('Dan', 'Syaopin')
cool_reviewer2.courses_attached += ['Python']

cool_reviewer1.rate_hw(best_student1, 'Python', 10)
cool_reviewer2.rate_hw(best_student1, 'Python', 10)
cool_reviewer1.rate_hw(best_student2, 'Python', 8)

print(best_student1.grades)

best_student1.rate_lect(cool_lecturer1, 'Python', 7)
best_student1.rate_lect(cool_lecturer1, 'Python', 6)

print(cool_lecturer1.grades)

print(best_student1)
print()

print(cool_lecturer1)
print()

print(cool_reviewer1)
print()

print(cool_reviewer2)
print()

print('Второй студент лучше первого?', best_student1 < best_student2)

print('Второй лектор лучше первого?', cool_lecturer1 < cool_lecturer2)

def average_score_of_students(students_list, course_name):
    k = 0
    s = 0
    for student in students_list:
        if student.grades.get(course_name) != None:
            mark_list = student.grades.get(course_name)
            k += len(mark_list)
            s += sum(mark_list)
    if k != 0:
        return s / k
    else:
        return 0


def average_score_of_lects(lects_list, course_name):
    k = 0
    s = 0
    for lect in lects_list:
        if lect.grades.get(course_name) != None:
            mark_list = lect.grades.get(course_name)
            k += len(mark_list)
            s += sum(mark_list)
    if k != 0:
        return s / k
    else:
        return 0

print()

print('Средняя оценка за домашние задания по всем студентам в рамках курса:', average_score_of_students([best_student1, best_student2], 'Python'))
print()

print('Cредняя оценка за лекции всех лекторов в рамках курса:', average_score_of_lects([cool_lecturer1, cool_lecturer2], 'Python'))



