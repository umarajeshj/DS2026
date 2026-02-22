#Base Class 1
class Employee:
    def __init__(self,name):
        self.name = name
        print(f"Employee Name: {self.name}")

#Base Class 2
class AutomationSkills:
    def write_script(self):
        print("Writing Selenium scripts")

#Derived Class
class AutomationTester(Employee,AutomationSkills):
    def execute_tests(self):
        print(f"{self.name} is an Automation Tester")

#Creating objects
a1 = AutomationTester("Bala")
a1.write_script()
a1.execute_tests()