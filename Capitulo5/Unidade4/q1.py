def partition1(S, low, high):
    pivot = S[low]
    left, right = low + 1, high
    while left < right:
        print(S)
    while left <= right and S[left] <= pivot:
        left += 1
    while left <= right and S[right] >= pivot:
        right -= 1
    if left < right:
        S[left], S[right] = S[right], S[left]
    pivotpoint = right
    S[low], s[pivotpoint] = S[pivotpoint], S[low]
    return pivotpoint
S = [15, 10, 12, 20, 25, 13, 22]
partition1(S, 0, len(S) - 1)
print(S)