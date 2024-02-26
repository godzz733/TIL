n = int(input())
ans = -2**31
arr = list(input())
for i in range(n):
    if arr[i].isdigit():
        arr[i] = int(arr[i])
v = [0] * n
def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def mul(a,b):
    return a*b

def cal_ans():
    tem = 0
    if arr[1] == '+':
        tem = plus(arr[0],arr[2])
    elif arr[1] == '-':
        tem = minus(arr[0],arr[2])
    else:
        tem = mul(arr[0],arr[2])
    for i in range(3,n,2):
        if arr[i] == '+':
            tem = plus(tem,arr[i+1])
        elif arr[i] == '-':
            tem = minus(tem,arr[i+1])
        else:
            tem = mul(tem,arr[i+1])
    return tem


def back(idx):
    global arr,v, ans
    if idx == n:
        ans = max(cal_ans(),ans)
        return
    if idx == 1:
        if not v[idx+2]:
            v[idx] = 1
            if arr[idx] == '+':
                tem = plus(arr[idx-1],arr[idx+1])
            elif arr[idx] == '-':
                tem = minus(arr[idx-1],arr[idx+1])
            else:
                tem = mul(arr[idx-1],arr[idx+1])
            tnum = (arr[idx-1],arr[idx+1],arr[idx])
            arr[idx-1] = tem
            arr[idx] = '+'
            arr[idx+1] = 0
            back(idx+2)
            v[idx] = 0
            arr[idx-1] = tnum[0]
            arr[idx+1] = tnum[1]
            arr[idx] = tnum[2]
    elif idx == n-2:
        if not v[idx-2]:
            v[idx] = 1
            if arr[idx] == '+':
                tem = plus(arr[idx-1],arr[idx+1])
            elif arr[idx] == '-':
                tem = minus(arr[idx-1],arr[idx+1])
            else:
                tem = mul(arr[idx-1],arr[idx+1])
            tnum = (arr[idx-1],arr[idx+1],arr[idx])
            arr[idx-1] = tem
            arr[idx] = '+'
            arr[idx+1] = 0
            back(idx+2)
            v[idx] = 0
            arr[idx-1] = tnum[0]
            arr[idx+1] = tnum[1]
            arr[idx] = tnum[2]
    else:
        if not v[idx-2] and not v[idx+2]:
            v[idx] = 1
            if arr[idx] == '+':
                tem = plus(arr[idx-1],arr[idx+1])
            elif arr[idx] == '-':
                tem = minus(arr[idx-1],arr[idx+1])
            else:
                tem = mul(arr[idx-1],arr[idx+1])
            tnum = (arr[idx-1],arr[idx+1],arr[idx])
            arr[idx-1] = tem
            arr[idx] = '+'
            arr[idx+1] = 0
            back(idx+2)
            v[idx] = 0
            arr[idx-1] = tnum[0]
            arr[idx+1] = tnum[1]
            arr[idx] = tnum[2]
    back(idx+2)
if n == 1:
    print(arr[0])
elif n == 3:
    print(eval(''.join(map(str,arr))))
else:
    back(1)
    print(ans)