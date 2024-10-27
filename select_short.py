def selectionsort1(S):
    R = []
    while len(S) > 0:
       print (R, S)
       smallest = S.index(min(S))
       R.append(S[smallest])
       S.pop(smallest)
    return R
S = [50, 30, 40, 10, 20]
R = selectionsort1(S)
print (R)
