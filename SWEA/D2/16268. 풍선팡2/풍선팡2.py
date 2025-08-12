T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 격자 N*M
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_powder = 0
    
    di = [0, 0, -1, 0, 1]
    dj = [0, 1, 0, -1, 0]

    for i in range(N):
        for j in range(M):
            tmp_powder = 0
            for k in range(5):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<M:
                    tmp_powder += arr[ni][nj]
            if max_powder < tmp_powder:
                max_powder = tmp_powder
    print(f"#{tc} {max_powder}")