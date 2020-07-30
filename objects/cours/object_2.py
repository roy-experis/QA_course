class Student():

    def __init__(self,id,name,list_of_grades={}):
        self.id=id
        self.name=name
        self.list_of_grades=list_of_grades

    def add_grade(self,subject,grade):
        self.list_of_grades.update({subject:grade})

    def __repr__(self):
        return f'id: {self.id}, name: {self.name},list of grades: {self.list_of_grades}'

    def calc_factor(self,subject,factor):
        for i in self.list_of_grades:
            if(i==subject and self.list_of_grades[i]<=100-factor):
                self.list_of_grades[i]=self.list_of_grades[i]+factor
            if(i==subject and self.list_of_grades[i]>100-factor):
                self.list_of_grades[i] =100

    def average(self):
        sum=0
        for i in self.list_of_grades:
            sum = sum + self.list_of_grades[i]
        return "the average is:", sum/len(self.list_of_grades)

class Course:
    def __init__(self,course_id,course_name,name_subject_and_profesor={},list_of_students=[],max_num_of_students=1):
        self.course_id=course_id
        self.course_name=course_name
        self.name_subject_and_profesor=name_subject_and_profesor
        self.list_of_students=list_of_students
        self.max_num_of_students=max_num_of_students

    def __str__(self):
        return f'cours id: {self.course_id}, cours name: {self.course_name}, subject name and professor: {self.name_subject_and_profesor},students: {self.list_of_students.__str__()} ,max num of students:{self.max_num_of_students}'

    def add_student(self,Student):
        if(self.max_num_of_students>len(self.list_of_students)):
            self.list_of_students.append(Student)
            return True
        else:
            return False

    def del_student(self,id):
        for i in self.list_of_students:
            if i.id==id:
                self.list_of_students.remove(i)

    def add_factor(self,subject,factor):
        for i in self.list_of_students:
            i.calc_factor(subject,factor)



