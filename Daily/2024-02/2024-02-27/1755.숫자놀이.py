import sys;input = sys.stdin.readline
n,m = map(int,input().split())
dic = {'0': 'zero', '1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four', '5' : 'five', '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine'}
ans = sorted([(dic[str(i)[0]]+(dic[str(i)[1]] if i > 9 else ''),i) for i in range(n,m+1)])
for i in range(len(ans)):
    if i%10 == 0 and i != 0:
        print()
    print(ans[i][1],end=' ')