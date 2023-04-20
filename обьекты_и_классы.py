from statistics import mean
from functools import total_ordering


class Mentor:
 
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
       
        
class Student():
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached2 = []
        self.grades = {}
        self.ins = mean([9.9, 9.9, 10])
        self.progress = 'Python', 'Git'
        
    def rate_sp(self, lecturer, course, grade):
        '''выставляет оценку лекторам'''
        if isinstance(lecturer, Lecturer) and course in self.courses_attached2 and course in lecturer.courses_in_progress2:   
            if course in lecturer.gradess:
                lecturer.gradess[course] += [grade]
            else:
                lecturer.gradess[course] = [grade]
        else:
            return 'Ошибка'
         
    def __str__(self,):               
        return "Имя: {0} \nФамилия: {1} \nСредняя оценка за лекции: {2}".format(self.name, self.surname, self.ins)
    
    def fg(self, courses, stude):
        '''4 задание'''
        print('Курс: ' + courses)   
        for student in stude: 
            print(student)            
    task_four = []  
   

class Reviewer(Mentor):
     
    def __init__(self, name, surname):
        super().__init__(name, surname)        
                
    def rate_hw(self, student, course, grade):
        '''Выставляет студентам оценки за домашнее задание''' 
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return "Имя: {0} \nФамилия: {1}".format(self.name, self.surname) 


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.inss = mean([9.9, 9.9, 10])
        self.courses_in_progress2 = []
        self.gradess = {}
    def __str__(self):
        return "Имя: {0} \nФамилия: {1} \nСредняя оценка за лекции: {2}".format(self.name, self.surname, self.inss) 
    
    def fg(self, courses, stude):
        '''4 задание'''
        print('Курс: ' + courses)   
        for student in stude: 
            print(student)            
    task2_four = []


   
R = Mentor('Павел', 'Маркович')
T = Mentor('Вячеслав', 'Маркович')

best_student = Student('Сергей', 'Павловичь', 'M')
best_student.courses_in_progress += ['Python']
best_student.task_four.append(best_student)


cool_student = Student('Светлана', 'Иванова', 'M')
cool_student.courses_attached2 += ['Python']
print(cool_student,  '\nКурсы в процессе изучения: %s, %s' % cool_student.progress, '\nЗавершенные курсы: Введение в программирование')
cool_student.task_four.append(cool_student)
cool_student.fg('Python', cool_student.task_four)

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
print(cool_reviewer)
B = Reviewer('Jim', 'Ted')


best_lecturer = Lecturer('Денис', 'Сергеевичь')  
best_lecturer.courses_in_progress2 += ['Python'] 
print(best_lecturer)
G = Lecturer('Вова', 'Иванович') 
best_lecturer.task2_four.append(best_lecturer)
G.task2_four.append(G)
best_lecturer.fg('Python', best_lecturer.task2_four)


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_student.rate_sp(best_lecturer, 'Python', 9)

print(best_student.grades)
print(best_lecturer.gradess)


@total_ordering
class GF:
    h = cool_student.ins
    a = best_lecturer.inss
    def __eq__(self, other):
        return self.h == other.a
    def __gt__(self, other):
        return self.h > other.a

Z = GF()
D = GF()
print(Z == D )
print(Z != D )  
print(Z > D )
print(Z < D )

