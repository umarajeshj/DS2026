class User:
    all_users = []

    def __init__(self, name):
        self.name = name
        self.isActive = True
        User.all_users.append(self)

    def login(self):
        return f"{self.name} logged in."

class Student(User):
    def enroll_course(self, course):
        course.students.append(self.name)
        return f"{self.name} joined {course.title}"
    
    def pay_fee(self):
        return f"Fee paid by {self.name}."

    def login(self): # Override
        return f"Student Dashboard: Welcome {self.name}"

class Instructor(User):
    def create_course(self, title):
        print(f"{title} is created by {self.name}")
        return Course(title, self.name)

class Admin(User):
    def block_user(self, user):
        user.active = False
        return f"{user.name} is now blocked."

    def generate_report(self):
        return f"Total Users: {len(User.all_users)}"

class Course:
    def __init__(self, title, instructor):
        self.title = title
        self.instructor = instructor
        self.students = []

# --- Simple Test ---
admin = Admin("John")
instructor = Instructor("Prof. Bala")
student = Student("Sam")

# Features
course = instructor.create_course("Python")
print(admin.login())
print(student.enroll_course(course))
print(student.login())  # Shows override
print(admin.block_user(student))
print(f"Enrolled in {course.title}: {course.students}")
