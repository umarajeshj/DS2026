marks = [78,85,62,90,55,88]
print("highest = ",max(marks))
numberOfStudents = len(marks)
print("average = ",sum(marks)/numberOfStudents)

#Distinction
distinction_marks = []

for mark in marks:
    if(mark > 75):
        distinction_marks.append(mark)
    else:
        continue
print("Distinction marks = ",distinction_marks)

#Adding new mark to list
marks.append(95)
print("After appending = ",marks)

#Removing 55 from list
marks.remove(55)
print("After removing = ",marks)

#Sorting
marks.sort()
print("After sorting = ",marks)