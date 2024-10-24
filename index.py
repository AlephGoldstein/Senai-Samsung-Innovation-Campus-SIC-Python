def bubblesort(S):
    n = len(S)
    for i in range(n):
        print(S) 
        for j in range(n - i - 1):  
            if S[j] > S[j + 1]:
                S[j], S[j + 1] = S[j + 1], S[j] 
S = [50, 30, 40, 10, 20]
bubblesort(S)
print(S)
