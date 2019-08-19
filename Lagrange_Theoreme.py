import math

list_of_val = []


def lagrange_4_sqr(num):
    sqr = num
    counter = 0
    flag = True
    while flag:
        if math.sqrt(sqr).is_integer():
            flag = False
            list_of_val.append(math.sqrt(sqr))
            if counter > 0:
                lagrange_4_sqr(counter)
        else:
            sqr -= 1
            counter += 1

    return list_of_val


in_val = int(input())
print(lagrange_4_sqr(in_val))
