def solution(number):
    multiples = []
    for i in range(1,number):
        if i % 3 == 0:
            multiples.append(i)
        if i % 5 == 0:
            if i not in multiples:
                multiples.append(i)
    
    x = sum(multiples)
    return x
    pass
  