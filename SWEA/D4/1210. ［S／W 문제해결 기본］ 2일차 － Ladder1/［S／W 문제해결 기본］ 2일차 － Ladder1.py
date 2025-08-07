for tc in range(10):
    T = int(input())
    lad = [list(map(int, input().split())) for _ in range(100)] # 사다리 정보

    ni, nj = 99, lad[-1].index(2) # now_point i,j : 끝점으로 초기화
    v = 0 # 움직이던 방향 초기화 : 왼(-1), 위(0), 오(1)

    while True:
        # 이전에 오른쪽으로 이동중인게 아니고, 왼쪽에 1 있으면
        if nj>0 and lad[ni][nj-1] == 1 and v != 1:
            nj = nj -1
            v = -1
            if ni == 0:
                break
        # 이전에 왼쪽으로 이동중인게 아니고, 오른쪽에 1 있으면
        elif nj<99 and lad[ni][nj+1] ==1 and v != -1:
            nj = nj +1
            v = 1
            if ni == 0:
                break
        # 위쪽이 1이면
        elif lad[ni-1][nj] == 1:
            ni = ni-1
            v = 0
            if ni == 0:
                break

    print(f"#{T} {nj}")