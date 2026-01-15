employees = ["Alice","Bob","Charlie","David","Eve"]
for i in range(0,len(employees)):
    print(i+1,".",employees[i])

#with enumerate()
print("Using enumerate()") 
for emp in enumerate(employees):
    print(emp)