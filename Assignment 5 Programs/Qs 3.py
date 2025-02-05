def calcAverageScore(stuData: dict):
    totalScore = 0
    for student in stuData.keys():
        totalScore += stuData[student]
        
    return totalScore

stuData = {}
n = int(input("Enter number of students: "))
for i in range(n):
    stuName = input("Enter student name: ")
    stuScore = int(input("Enter student score: "))
    stuData[stuName] = stuScore
    
print(f"Total Score = {calcAverageScore(stuData)}")