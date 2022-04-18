def spin_words(sentence):
    # Your code goes here
    new_x = []
    y = [str(i) for i in sentence.split(" ")]
    for i in y:
        if len(i) >= 5:
            w = i[::-1]
            new_x.append(w)
        else:
            new_x.append(i)

    new_x = " ".join(new_x)
    return new_x