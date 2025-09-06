def way(i, j, sum):
    global N, arr, min_sum

    if i == N or j == N:    # 범위 밖
        return
    
    sum = sum + arr[i][j]
    if i == N-1 and j == N-1:   # 종료조건
        min_sum = min(sum, min_sum)
        return
    
    way(i+1, j, sum)
    way(i, j+1, sum)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = float('inf')
    way(0,0,0)
    print(f"#{tc} {min_sum}")