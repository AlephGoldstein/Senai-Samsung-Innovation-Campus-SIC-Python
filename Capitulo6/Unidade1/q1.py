def activity_selection1(start, finish):
    result = []
    i = 0
    result.append(i)
    for j in range(1, len(start)):
        if finish[i] <= start[j]:
            result.append(j)
            i = j
    return result
start = [1,3,2,0,5,8,5] 
finish = [2, 4, 5, 6, 6, 9, 9]
meetings = activity_selection1(start,finish)
maximum = len(meetings)
print(meetings, maximum)
           