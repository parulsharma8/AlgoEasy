def split_array(array1, v):
    array2 = []
    array3 = []
    array4 = []

    for i in range(0, len(array1)):
        if array1[i] > v:
            array2.append(array1[i])
        elif array1[i] == v:
            array3.append(array1[i])
        else:
            array4.append(array1[i])

    return array2, array3, array4

array1 = [1, 2, 3, 4, 5, 6, 7, 8 ,9 , 9, 10, 11, 7, 6, 5, 4, 3, 2, 9, 0]
v = 7
result = split_array(array1, v)
print(result)