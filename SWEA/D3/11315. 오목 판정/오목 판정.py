T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)] # N*N

    di = [0, 1, 1, 1] # 가로, 세로, 우하향, 좌하향
    dj = [1, 0, 1,-1]

    answer = 'NO'

    for i in range(N):
        for j in range(N):
            for d in range(4):
                cnt = 0
                for k in range(5):
                    ni = i + di[d] * k
                    nj = j + dj[d] * k
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj]=='o':
                        cnt += 1
                if cnt == 5:
                    answer = 'YES'

    print(f"#{tc} {answer}")