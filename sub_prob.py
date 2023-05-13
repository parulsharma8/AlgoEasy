def sub_prob(arr):
    res = []
    for i in range(0, len(arr)):
        res.append(1)
        for j in range(0, i):
            if arr[i] > arr[j]:
                res[i] = max(1 + res[j], res[i])
    return max(res)

arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

output = sub_prob(arr)
print(output)

