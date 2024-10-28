def mergesort2(S, low, high):
	if low < high:
		print(S)
		mid = (low + high) // 2
		mergesort2(S, low, mid)
		mergesort2(S, mid + 1, high)
		merge2(S, low, mid, high)
  
def merge2(S, low, mid, high):
	R = []
	i, j = low, mid + 1
	while i <= mid and j <= high:
		if S[i] < S[j]:
			R.append(S[i]); i += 1
		else:
			R.append(S[j]); j += 1
	if i > mid:
		for k in range(j, high + 1):
			R.append(S[j])
	else:
		for k in range(i, mid + 1):
			R.append(S[i])
	for k in range(len(R)):
		S[low + k] = R[k]
S = [27, 10, 12, 20, 25, 13, 15, 22]
mergesort2(S, 0, len(S) - 1)
print(S)