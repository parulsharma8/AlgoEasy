def duplicate(q):
    res = set()
    hash_set = set()

    for i in range(len(q)):
        if q[i] in hash_set:
            res.add(q[i])
        else:
            hash_set.add(q[i])
    return res

q = [1, 3, 4, 5, 3]
print(duplicate(q))