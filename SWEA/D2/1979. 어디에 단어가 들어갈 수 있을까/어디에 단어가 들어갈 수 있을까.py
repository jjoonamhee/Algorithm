T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    # 가로 방향
    for i in range(N):
        for j in range(N-K+1):
            check = True
            if arr[i][j] == 1 and (j==0 or arr[i][j-1]==0): # 시작이전이 벽이나 흑
                if j+K == N or arr[i][j+K] ==0: # 끝 이후가 벽이나 흑
                    for k in range(1,K):
                        if arr[i][j+k] == 0:
                            check = False
                            break
                else:
                    check = False
                    # break
            else:
                check = False
            
            if check:
                answer += 1

    # 세로방향
    for j in range(N):
        for i in range(N-K+1):
            check = True
            if arr[i][j] == 1 and (i==0 or arr[i-1][j]==0):
                if i+K == N or arr[i+K][j] == 0:
                    for k in range(1,K):
                        if arr[i+k][j] == 0:
                            check = False
                            break
                else:
                    check = False
                    # break
            else:
                check = False
            
            if check:
                answer += 1
    
    print(f"#{tc} {answer}")