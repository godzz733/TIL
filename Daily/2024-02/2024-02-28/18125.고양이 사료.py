n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
ans = [[0] * m for _ in range(n)]
for i in range(m):
    for j in range(n):
        ans[j][m-i-1] = arr[i][j]
if ans == [list(map(int, input().split())) for _ in range(n)]:
    print("""|>___/|        /}
| O < |       / }
(==0==)------/ }
| ^  _____    |
|_|_/     ||__|""")
else:
    print('''|>___/|     /}
| O O |    / }
( =0= )""""  \\
| ^  ____    |
|_|_/    ||__|
''')