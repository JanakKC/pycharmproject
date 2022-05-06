def largest_number(*a):
    count = 0
    lengtha = len(a)
    while lengtha > count:
        if count == 0:
            no1 = a[count]
        else:
            if a[count] < no1:
                pass
            else:
                no1 = a[count]
        count += 1
    print(no1)


largest_number(3, 33, 4, 55, 111)

