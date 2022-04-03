
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f"Имя:{self.name}" \
               f"\nФамилия:{self.surname}" \
               f"\nСредняя оценка за домашние задания: {sum(map(sum, self.grades.values()))/sum(map(len, self.grades.values()))}" \
               f"\nКурсы в процессе изучения: {self.courses_in_progress}" \
               f"\nЗавершенные курсы: {self.finished_courses}"

    def rate_student(self, lecturer, course, grade):
            if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'


    def __gt__(self, other_student):
        if sum(map(sum, self.grades.values()))/sum(map(len, self.grades.values())) > sum(map(sum, other_student.grades.values()))/sum(map(len, other_student.grades.values())):
            return f"\nСредния оценка {self.name} выше, чем {other_student.name} ({sum(map(sum, self.grades.values()))/sum(map(len, self.grades.values()))} > {sum(map(sum, other_student.grades.values()))/sum(map(len, other_student.grades.values()))})"
        else:
            return f"\nСредния оценка {self.name} не выше, чем {other_student.name} ({sum(map(sum, self.grades.values()))/sum(map(len, self.grades.values()))} < {sum(map(sum, other_student.grades.values()))/sum(map(len, other_student.grades.values()))})"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class  Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


    def __str__(self):
        return f"Имя:{self.name}" \
               f"\nФамилия:{self.surname}" \
               f"\nСредняя оценка за лекцию: {sum(map(sum, self.grades.values()))/sum(map(len, self.grades.values()))}"

    def __gt__(self, other_lecturer):
            if sum(map(sum, self.grades.values()))/sum(map(len, self.grades.values())) > sum(map(sum, other_lecturer.grades.values()))/sum(map(len, other_lecturer.grades.values())):
                return f"\nСредния оценка {self.name} выше, чем {other_lecturer.name} ({sum(map(sum, self.grades.values()))/sum(map(len, self.grades.values()))} > {sum(map(sum, other_lecturer.grades.values()))/sum(map(len, other_lecturer.grades.values()))})"
            else:
                return f"\nСредния оценка {self.name} не выше, чем {other_lecturer.name} ({sum(map(sum, self.grades.values()))/sum(map(len, self.grades.values()))} < {sum(map(sum, other_lecturer.grades.values()))/sum(map(len, other_lecturer.grades.values()))})"


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
        return f"Имя:{self.name}" \
               f"\nФамилия:{self.surname}"

Student_list = []
Lecturer_list = []

def rate_average_student(Student_list, course):
    x = 0
    count = 0
    for i in Student_list:
        if course in i.courses_in_progress:
            x += sum(map(sum, i.grades.values()))/sum(map(len, i.grades.values()))
            count += 1
    return x/count

def rate_average_lecturer(Lecturer_list, course):
    x = 0
    count = 0
    for i in Lecturer_list:
        if course in i.courses_attached:
            x += sum(map(sum, i.grades.values()))/sum(map(len, i.grades.values()))
            count += 1
    return x/count

Lektor_1 = Lecturer('IVAN', 'GROZNIY')
Lektor_2 = Lecturer('BORIS', 'BRITVA')

Lecturer_list.append(Lektor_1)
Lecturer_list.append(Lektor_2)

Lektor_1.courses_attached += ['Python']
Lektor_2.courses_attached += ['Gyt']

Reviewer_1 = Reviewer('HUAN', 'GONSALES')
Reviewer_2 = Reviewer('DON', 'PEDRO')

Reviewer_1.courses_attached += ['Python']
Reviewer_2.courses_attached += ['Gyt']

best_student = Student('Rodri', 'Eman', 'female')
bad_student = Student('Rodrigo', 'Emanuel', 'female')

Student_list.append(best_student)
Student_list.append(bad_student)

best_student.finished_courses += ['Введение в програмирование']
bad_student.finished_courses += ['Введение в програмирование']

best_student.courses_in_progress += ['Gyt']
best_student.courses_in_progress += ['Python']

bad_student.courses_in_progress += ['Gyt']
bad_student.courses_in_progress += ['Python']

Reviewer_1.rate_hw(best_student, 'Python', 8)
Reviewer_1.rate_hw(best_student, 'Python', 9)
Reviewer_1.rate_hw(best_student, 'Python', 8)

Reviewer_2.rate_hw(best_student, 'Gyt', 8)
Reviewer_2.rate_hw(best_student, 'Gyt', 9)
Reviewer_2.rate_hw(best_student, 'Gyt', 4)

Reviewer_1.rate_hw(bad_student, 'Python', 5)
Reviewer_1.rate_hw(bad_student, 'Python', 6)
Reviewer_1.rate_hw(bad_student, 'Python', 7)

Reviewer_2.rate_hw(bad_student, 'Gyt', 4)
Reviewer_2.rate_hw(bad_student, 'Gyt', 5)
Reviewer_2.rate_hw(bad_student, 'Gyt', 6)

best_student.rate_student(Lektor_1, 'Python', 7)
bad_student.rate_student(Lektor_1, 'Python', 3)

best_student.rate_student(Lektor_2, 'Gyt', 8)
bad_student.rate_student(Lektor_2, 'Gyt', 4)

print(best_student.grades)
print(bad_student.grades)
print("-------------------")
print(best_student)
print("-------------------")
print(Reviewer_1)
print("-------------------")
print(Lektor_1)
print("-------------------")
print(Lektor_1.grades)
print("-------------------")
print(best_student.__gt__(bad_student))
print("-------------------")
print(Lektor_1.__gt__(Lektor_2))
print("-------------------")
print(rate_average_student(Student_list, 'Python'))
print("-------------------")
print(rate_average_lecturer(Lecturer_list, 'Python'))

