#Creating class
class TestStatus:
    #Creating constructor
    def __init__(self,TestCaseID,TestStatus):
        self.id = TestCaseID
        self.status = TestStatus
  
  #Creating method
    def displayStatus(self):
        print("Test ID and Status :",self.id," , ",self.status)

#Creating objects
ts = TestStatus(1,"pass")
ts1 = TestStatus(2,"fail")

#Calling methods
ts.displayStatus()
ts1.displayStatus()