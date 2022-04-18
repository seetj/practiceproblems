def barista(coffees):
    total = []
    clean_time = 2
    coffees_sorted = sorted(coffees)
    x = len(coffees)
    for i in range(1,x):
        z = 2 * i
        total.append(z)
    for i in coffees_sorted:
        y = x * i
        total.append(y)
        x -= 1
    return sum(total)