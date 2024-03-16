n = int(input())
arr = [["",""] for _ in range(n)]
for i in range(n):
    a,b,c = map(str,input().split())
    arr[ord(a) - 65][0] = b
    arr[ord(a) - 65][1] = c

def preorder(x):
    print(chr(x+65), end="")
    if arr[x][0] != ".":
        preorder(ord(arr[x][0])-65)
    if arr[x][1] != ".":
        preorder(ord(arr[x][1])-65)

def inorder(x):
    if arr[x][0] != ".":
        inorder(ord(arr[x][0])-65)
    print(chr(x+65), end="")
    if arr[x][1] != ".":
        inorder(ord(arr[x][1])-65)

def postorder(x):
    if arr[x][0] != ".":
        postorder(ord(arr[x][0])-65)
    if arr[x][1] != ".":
        postorder(ord(arr[x][1])-65)
    print(chr(x+65), end="")

preorder(0)
print()
inorder(0)
print()
postorder(0)