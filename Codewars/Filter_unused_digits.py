def unused_digits(*numbers):
    #your code here
    list = []
    list2 = []
    list3 = []
    list4 = []
    for i in numbers:
        list4.append(i)
    print(list4)
    z =[str(x) for x in list4]
    n = "".join(z)
    
    for i in range(0,10):
        list.append(i)

    for i in n:
        list2.append(int(i))

    digits = set(list) - set(list2)

    for i in digits:
        list3.append(i)
    list3.sort()
    print(list3)
    z = [str(x) for x in list3]
    z = "".join(z)
    return z