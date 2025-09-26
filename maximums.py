def max_of_two(x, y):
    resu1=0
    if x>y:
        resu1=x
    else:
        resu1=y
    return resu1


def max_of_three(x, y, z):
    if x>y:
        if x>z:
            resu2=x
        else:
            resu2=z
    elif y>z:
        resu2=y
    else:
        resu2=z
    return resu2
