with open('Week_06/ClassAssignment/Calorie_Tracking_Dataset.csv', 'r') as file:
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(',')
        print(data)