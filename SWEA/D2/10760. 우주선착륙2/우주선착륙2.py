# [[2, 3, 1, 8, 9], [7, 6, 2, 2, 6], [5, 7, 3, 8, 7]]
matrix = [[2, 3, 1, 8, 9], [7, 6, 2, 2, 6], [5, 7, 3, 8, 7]]

def explore_lower_gound(i,j):
    global matrix, N, M
    lower_ground = 0 # 저지대 개수 초기화

    # 8위치 세트 (1,2,3,4,5,6,7,8)
    r_direction = [-1, -1, -1, 0, 0, 1, 1, 1]
    c_direction = [-1, 0, 1, -1, 1, -1, 0, 1]

    # 위치별 조사
    for d in range(8):
        row = i + r_direction[d]
        col = j + c_direction[d]

        if row>=0 and row<N and col>=0 and col<M:
            if matrix[row][col] < matrix[i][j]: # 타겟 지점 matrix[i][j] 보다 낮으면
                lower_ground += 1

    return lower_ground

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for n in range(N)]
    candidate_site = 0

    for i in range(N):
        for j in range(M):
            if explore_lower_gound(i, j) >= 4:
                candidate_site += 1
    print(f"#{test_case} {candidate_site}")