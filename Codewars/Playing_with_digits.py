def dig_pow(n, p):
    # your code
    n = str(n)
    factor = []
    rule = []
    for i in n:
        digit = (int(i)**p)
        p += 1
        rule.append(digit)
    add = sum(rule)
    z = add / int(n)
    if add % int(n) == 0: 
        return z
    else:
        return(-1)