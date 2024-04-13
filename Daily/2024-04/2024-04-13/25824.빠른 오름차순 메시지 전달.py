arr = [list(map(int,input().split())) for _ in range(12)]
ans = int(1e9)
lst = [[(0,1),(1,0)],[(2,3),(3,2)],[(4,5),(5,4)],[(6,7),(7,6)],[(8,9),(9,8)],[(10,11),(11,10)]]
ans_arr = []
for x,y in lst[0]:
    for a,b in lst[1]:
        for c,d in lst[2]:
            for e,f in lst[3]:
                for g,h in lst[4]:
                    for i,j in lst[5]:
                        ans_arr.append([x,y,a,b,c,d,e,f,g,h,i,j])
for i in ans_arr:
    cnt = 0
    for j in range(1,12):
        cnt += arr[i[j-1]][i[j]]
    ans = min(ans,cnt)
print(ans)