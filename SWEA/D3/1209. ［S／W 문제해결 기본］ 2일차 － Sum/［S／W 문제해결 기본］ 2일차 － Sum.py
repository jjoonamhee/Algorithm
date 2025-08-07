for _ in range(1, 11):
    t = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    max_v = 0
    # 행 검사
    for i in range(100):
        sum_v = 0
        for j in range(100):
            sum_v += matrix[i][j]
        if max_v < sum_v:
            max_v = sum_v

    # 열 검사
    for j in range(100):
        sum_v = 0
        for i in range(100):
            sum_v += matrix[i][j]
        if max_v < sum_v:
            max_v = sum_v

    # \ 검사
    sum_v = 0
    for i in range(100):
        sum_v += matrix[0 + 1*i][0 + 1*i]
    if max_v < sum_v:
        max_v = sum_v

    # / 검사
    sum_v = 0
    for i in range(100):
        sum_v += matrix[0 + 1*i][99 - 1*i]
    if max_v < sum_v:
        max_v = sum_v

    print(f"#{t} {max_v}")