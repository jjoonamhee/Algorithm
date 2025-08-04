# 풍선팡 함수
def balloonpang(row, column): 
    global N, M, matrix, max_powder
    # 타겟 풍선의 꽃가루 개수(n_move) = 전파 가능 칸 수
    n_move = matrix[row][column]
    # 상,하,좌,우 
    r_direction = [-1, 1, 0, 0]
    c_direction = [0, 0, -1, 1]
    # 현재 탐색하는 순서에서 터지는 꽃가루 개수 저장
    tmp_powder = [n_move] # 타겟 풍선의 꽃가루 개수는 미리 저장
    
    for v in range(4): # 상하좌우 똑같이 탐색
        for n in range(1, n_move+1): # 입력 받은 위치에서 상하좌우 ~n칸의 인덱스 값
            r = row + (n * r_direction[v])
            c = column + (n * c_direction[v])
            if 0 > r or r > N-1 or 0 > c or c > M-1: # 인덱스가 매트릭스 넘어가면 처리하지 않기
                pass
            else:
                tmp_powder.append(matrix[r][c])
    return sum(tmp_powder) # 풍선팡 꽃가루 개수 합 반환

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for n in range(N)] # 매트릭스 입력받기
    max_powder = [] # tmp_powder 저장할 빈 리스트
    
    # 0,0 부터 N,M 까지 탐색 루프
    for i in range(N):
        for j in range(M):
            max_powder.append(balloonpang(i, j))
    
    print(f"#{test_case} {max(max_powder)}")