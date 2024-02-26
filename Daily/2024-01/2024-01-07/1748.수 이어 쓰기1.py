n = int(input())
arr = [0,0]
for i in range(9):
    arr.append(9*(i+1)*10**i+arr[-1])
l = len(str(n))
print(arr[l] + (n-10**(l-1)+1)*l)