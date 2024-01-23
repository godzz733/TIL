def solution(friends, gifts):
    answer = 0
    dic = {}
    arr = [0] * len(friends)
    for i in friends:
        dic[i] = [0,0,{i:0 for i in friends}]
    for i in gifts:
        a,b = i.split()
        dic[a][0] += 1
        dic[b][1] += 1
        dic[a][2][b] += 1
    for i in range(len(friends)-1):
        for j in range(i+1,len(friends)):
            if dic[friends[i]][2][friends[j]] or dic[friends[j]][2][friends[i]]:
                t = dic[friends[i]][2][friends[j]] - dic[friends[j]][2][friends[i]]
                if t > 0:
                    arr[i] += 1
                elif t < 0:
                    arr[j] += 1
                else:
                    t = dic[friends[i]][0] - dic[friends[i]][1] - dic[friends[j]][0] + dic[friends[j]][1]
                    if t > 0:
                        arr[i] += 1
                    elif t < 0:
                        arr[j] += 1
            else:
                t = dic[friends[i]][0] - dic[friends[i]][1] - dic[friends[j]][0] + dic[friends[j]][1]
                if t > 0:
                    arr[i] += 1
                elif t < 0:
                    arr[j] += 1
                    
        
    return max(arr)
