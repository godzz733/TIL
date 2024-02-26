n,m = map(int,input().split())
month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
d = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
idx = 0
for i in range(1,n):
    for j in range(1,month[i]+1):
        idx += 1
        if idx%7 == 0:
            idx = 0
for i in range(1,m):
    idx += 1
    if idx%7 == 0:
        idx = 0
print(d[idx])
