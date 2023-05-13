def longest_increasing_subsequence(arr):
    longest_sub = []
    for i in range(0, len(arr)):
        longest_sub.append(1)
        for j in range(0, i):
            if arr[i] > arr[j]:
                longest_sub[i] = max(1 + longest_sub[j], longest_sub[i])
    return max(longest_sub)

arr = [3, 4, 1, 5]
result = longest_increasing_subsequence(arr)
print(result)