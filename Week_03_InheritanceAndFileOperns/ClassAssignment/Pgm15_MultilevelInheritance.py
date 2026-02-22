#Base Class
class Person:
    def __init__(self,name):
        self.name = name
        print("Employee name from Person class")

#Derived Class
class Employee(Person):
    def __init__(self,name,employee_id):
        Person.__init__(self,name)
        self.employee_id = employee_id
        print("Employee id from Employee class")

#Derived class D1.1
class Manager(Employee):
    def __init__(self, name, employee_id,team_size):
        Employee.__init__(self,name,employee_id)
        self.team_size = team_size
        print("Team size from Manager class")
    
    def showDetails(self):
        print(f"Employee name : {self.name}")
        print(f"Employee id   : {self.employee_id}")
        print(f"Team size     : {self.team_size}")
        
m1 = Manager('Anu',10,25)
m1.showDetails()