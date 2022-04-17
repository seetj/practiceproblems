def square_digits(num):
    new_num = [int(x) for x in str(num)]
    new_num = [x**2 for x in new_num]
    new_num = [str(x) for x in new_num]
    num = "".join(new_num)
    num = int(num)
    return num