
n=input("Enter the student's name: ")
stu_marks={'Manu': '85','Sunny':'70','Kanya':'98'}
if n in stu_marks:
    print(f"{n}'s marks: {stu_marks[n]}")
else:
    print("Student not found")
