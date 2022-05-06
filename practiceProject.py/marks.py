increment = 1
num_of_students = int(input("Enter numbers of student:"))
student_marks = []
while increment <= num_of_students:
    print(f"=======Student NO:{increment}=====")
    for i in range(1):
        nep = int(input("Enter nep mark:"))
        english = int(input("Enter english mark:"))
        social = int(input("Enter social mark:"))
        math = int(input("Enter math mark:"))
        science = int(input("Enter science mark:"))
        mark = [nep, english, social, math, science]
        student_marks.append(mark)
    increment += 1

x = 1

for mark in student_marks:
    total = 0
    for mk in mark:
        total += mk
    pre = total / 5
    division = ""
    if pre > 40 and pre <= 50:
        division += "third"
    elif pre > 50 and pre <= 60:
        division += "Second"
    elif pre > 60 and pre <= 70:
        division += "first"
    elif pre > 80 and pre <= 100:
        division += "Distinction"
    else:
        division += "Try again"
    print(f"student number:{x} pre: {pre} Div:{division} ")
    x += 1
