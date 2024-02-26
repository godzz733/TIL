def solve():
    n, x, y = map(int, input().split())
    v = list(map(int, input().split()))
    mp = {}
    # 자기 자신이 x의 나머지가 몇 인지 저장하고 그 값에 y의 나머지를 저장
    for i in range(n):
        val_x, val_y = v[i] % x, v[i] % y
        if val_x not in mp:
            mp[val_x] = {}
        if val_y not in mp[val_x]:
            mp[val_x][val_y] = 0
        mp[val_x][val_y] += 1
    
    tot = 0
    # 이건 나의 x의 나머지와 무엇을 더해야 x의 배수가 되는지를 알아 내는 함수임
    # 예를들어 x = 5 일때 3의 경우 2를 더해야 5의 배수가 되므로 2를 반환
    cmp = lambda val: (x - (val % x)) % x
    for i in v:
        # 만약 나의 x의 나머지가 mp에 있고 그 값에 y의 나머지가 있으면 그 값을 더해줌
        if cmp(i) in mp and i % y in mp[cmp(i)]:
            # 이때 i % x == cmp(i)는 한마디로 나 자신이 포함되어있다는 말임, 즉 나와 나의 쌍은 불가능하므로 1을 빼줌
            tot += mp[cmp(i)][i % y] - (1 if i % x == cmp(i) else 0)
    # 이때 문제의 조건 상 i < j 이므로 위의 반복문에서는 (i,j) 와 (j,i) 를 둘다 더해줬으므로 2로 나눠줌 (i != j 이므로 2로 나눠도 됨
    print(tot // 2)

def main():
    tc = int(input())
    for _ in range(tc):
        solve()

if __name__ == "__main__":
    main()

