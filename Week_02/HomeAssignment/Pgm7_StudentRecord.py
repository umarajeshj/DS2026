class Student:
    def __init__(self,name,grade,department):
        self.name = name
        self.grade = grade
        self.department = department
    
    def print_info(self):
        print(f"Name  : {self.name}    | Grade : {self.grade}   | Department : {self.department}")

    def update_grade(self,new_grade):
        self.grade = new_grade

#Create student list
student1 = Student("Alice","A","Commerce")
student2 = Student("Bobby","B","Biology")
student3 = Student("David","C","Computer Science")

#Display student details
student_directory = [student1,student2,student3]
print("-----------Before Grade update------------------")
for student in student_directory:
    student.print_info()

#Update student grade for one student
student2.update_grade("D")

#Print after update
print("-----------After Grade update------------------")
for student in student_directory:
    student.print_info()