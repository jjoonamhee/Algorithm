T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for a in range(M):
                ni = i + a
                for b in range(M):
                    nj = j+b
                    kill += arr[ni][nj]
            if max_kill < kill:
                max_kill = kill
    print(f"#{tc} {max_kill}")