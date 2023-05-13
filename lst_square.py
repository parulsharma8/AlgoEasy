def squares(x):
    y = []
    for i in range(len(x)):
        y.append(pow(x[i], 2))

    return y

x = [1,2,3,4,5,6,7,8,9]
print(squares(x))