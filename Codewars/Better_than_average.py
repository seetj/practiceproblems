def better_than_average(class_points, your_points):
    # Your code here
    x = sum(class_points)/len(class_points)
    if your_points > x:
        return True
    else:
        return False