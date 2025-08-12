for tc in range(1,11):
    N = int(input()) # 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 위가 N극, 아래가 S극, 1은 N극, 2는 S극
    # 1은 밑으로 가야하고, 2는 위로가야함, 교착상태 수 구하기
    # 1. (S극 지우기) 위에서부터, 1 나올때까지 2를 0으로 치환
    # 2. (N극 지우기) 아래서부터, 2 나올때까지 1을 0으로 치환
    
    # MAGNETIC
    for j in range(N):
        i = 0
        while i < N:
            if arr[i][j] == 1:
                break
            if arr[i][j] == 2:
                arr[i][j] = 0
            i += 1

        ri = N-1
        while ri >= 0:            
            if arr[ri][j] == 2:
                break
            if arr[ri][j] == 1:
                arr[ri][j] = 0
            ri -= 1
    
    # 영역 세기: 1 아래가 2인 세트 수를 세기
    cnt = 0
    for j in range(N):
        for i in range(N-1):
            if arr[i][j] == 1:
                di = i+1
                while di<N:
                    if arr[di][j] == 1:
                        break
                    elif arr[di][j] == 2:
                        cnt += 1
                        di += 1
                        break
                    else:
                        di += 1

    print(f"#{tc} {cnt}")