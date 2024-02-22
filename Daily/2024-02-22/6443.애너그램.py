import sys; input = sys.stdin.readline
n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
def back(lst,ans,idx,v,tem):
    global dic
    if idx == len(lst):
        dic.add(''.join(ans))
        return
    if ''.join(ans) in tem:
        return
    tem.add(''.join(ans))
    for i in range(len(lst)):
        if i not in v:
            ans.append(lst[i])
            v.add(i)
            back(lst,ans,idx+1,v,tem)
            ans.pop()
            v.remove(i)

for i in arr:
    ans = set()
    dic = set()
    back(i,[],0,set(),set())
    for i in sorted(dic):
        print(i)