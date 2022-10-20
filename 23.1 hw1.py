class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        return f'My name is {self.fullname} \nI am {self.age} years old \nI am {self.is_married}'


class Student(Person):
    def __init__(self, fullname, age, is_married, mark):
        super().__init__(fullname, age, is_married)
        self.mark = mark

    def gpa_student(self):
        col = self.mark.values()
        len1 = len(self.mark)
        gpa = sum(col) / len1
        return gpa


class Teacher(Person):
    salary = 10000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def get_salary(self):
        if self.experience > 3:
            Teacher.salary += ((Teacher.salary * 5) / 100) * self.experience
            return Teacher.salary
    def info_teacher(self):
        return f'Teacher:{self.introduce_myself()}\nsalary:{self.get_salary()}\nexperience: {self.experience}'


def create_student():
    student1 = Student('Elnura Dubanaeva', 18, 'not married',
                       {'math': 5, 'biology': 4, 'English': 4, 'chemistry': 3})
    student2 = Student('Shaibekova Nagima', 18, 'not married',
                       {'math': 4, 'biology': 4, 'English': 3, 'chemistry': 3})
    student3 = Student('Magarova Alfiya', 19, 'not married',
                       {'math': 3, 'biology': 5, 'English': 3, 'chemistry': 4})
    students = [student1, student2, student3]
    for student in students:
        return f'\nStudent:{student.introduce_myself()} \nGPA {student.gpa_student()} points,\nmarks:{student.mark}'


print(create_student())
teacher = Teacher('Aleksey', 40, 'married', 5)
print(teacher.info_teacher())
