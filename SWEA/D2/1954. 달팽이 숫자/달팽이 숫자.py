# 달팽이 숫자
T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 배열의 크기 N*N
    matrix = [[0]*N for _ in range(N)]

    # 꼭짓점 위치 정보
    # top_left[0], top_right[1], bottom_right[2], bottom_left[3] 순
    pi = [0, 0, N-1, N-1]
    pj = [0, N-1, N-1, 0]

    num = list(range(N*N,0,-1)) # 채워야할 숫자 리스트

    while True:
        # 1. top_left[0]에서 top_right[1]까지 오른쪽으로 숫자 채우기
        r = pi[0] # 행 고정
        for c in range(pj[0],pj[1]+1): # 열 이동
            matrix[r][c] = num.pop()
        pi[0] += 1 # 행 다 채웠으니까 꼭짓점 위치 갱신
        pi[1] += 1
        if len(num) == 0:
            break

        # 2. top_right[1]에서 bottom_right[2]까지 밑으로 숫자 채우기
        c = pj[1] # 열 고정
        for r in range(pi[1], pi[2]+1): # 행 이동
            matrix[r][c] = num.pop()
        pj[1] -= 1 # 열 다 채웠으니까 꼭짓점 위치 갱신
        pj[2] -= 1
        if len(num) == 0:
            break

        # 3. bottom_right[2]에서 bottom_left[3]까지 왼쪽으로 숫자 채우기
        r = pi[2] # 행 고정
        for c in range(pj[2], pj[3]-1, -1): # 열 이동 (reverse)
            matrix[r][c] = num.pop()
        pi[2] -= 1 # 행 다 채웠으니까 꼭짓점 위치 갱신
        pi[3] -= 1
        if len(num) == 0:
            break

        # 4. bottom_left[3]에서 top_left[0]까지 위쪽으로 숫자 채우기
        c = pj[3] # 열 고정
        for r in range(pi[3], pi[0]-1, -1): # 행 이동 (reverse)
            matrix[r][c] = num.pop()
        pj[3] += 1 # 열 다 채웠으니까 꼭짓점 위치 갱신
        pj[0] += 1
        if len(num) == 0:
            break

    print(f"#{tc}")
    for i in range(len(matrix)):
        print(' '.join(map(str, matrix[i])))