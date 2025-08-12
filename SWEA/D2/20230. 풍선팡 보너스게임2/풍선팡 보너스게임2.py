T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_pang = 0

    for i in range(N):
        for j in range(N):
            pang = sum(arr[i])
            pang -= arr[i][j] # 가운데는 중복되니까 한번 빼기
            for k in range(N):
                pang += arr[k][j]
            
            if max_pang < pang:
                max_pang = pang 
    
    print(f"#{tc} {max_pang}")