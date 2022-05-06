# set the value of length and breadth and check if its a rectangular or square.

length = 20
breadth = 10
if length > breadth:
    print("it is a rectangular")
elif length == breadth:
    print("it is a square")

# write a program that allows student to attend if he/she has 75% attendence

print("what is the percentage of your attendence? ")
percentage = int(input())
if percentage >= 75:
    print("you can attend")
elif percentage < 75:
    print("you can not attend")

absent=60
present=50
if absent >present:
    print("you can not attend")
elif present<=absent:
    print("you can attend")
else:
    print("we will consider")


