def common_elements(array1, array2):

    x = set()
    array3 = []
    for i in range(0, len(array1)):
        x.add(array1[i])

    for i in range(0, len(array2)):
        if array2[i] in x:
            array3.append(array2[i])
    return array3

array1 = [1, 2, 3, 4, 5, 6]
array2 = [3, 4, 5, 6, 7]

result = common_elements(array1, array2)
print(result)