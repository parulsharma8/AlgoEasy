def countarray(z):
    return_dict = dict()
    for i in range(len(z)):
        k = z[i]
        if k in return_dict:
            return_dict[k] = return_dict[k] + 1
        else:
            return_dict[k] = 1

    return return_dict
z = [1, 1, 1]

print(countarray(z))