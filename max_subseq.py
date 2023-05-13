def max_subsequence(lst):
    max_sub = []
    for i in range(0, len(lst)):
        max_sub.append(1)
        for j in range(0, i):
            if lst[i] > lst[j]:
                max_sub[i] = max(1 + max_sub[j], max_sub[i])

    print(max(max_sub[0:4]))
    return max(max_sub)

lst = [1, 2, 5, 7, 3, 2, 6, 8, 0, 1, 4, 9, 10, 19, 22, 14, 15]
max_subsequence(lst)