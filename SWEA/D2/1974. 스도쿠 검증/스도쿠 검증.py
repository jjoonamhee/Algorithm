T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    # 가로 검증
    for i in range(9):
        n = set()
        for j in range(9):
            n.add(arr[i][j])
        if len(n) != 9:
            result = 0

    # 세로 검증
    for j in range(9):
        n = set()
        for i in range(9):
            n.add(arr[i][j])
        if len(n) != 9:
            result = 0
    
    # 영역 검증
    for i in [0,3,6]:
        for j in range(0,3,6):
            n = set()
            for a in range(3):
                ni = i + a
                for b in range(3):
                    nj = j + b
                    n.add(arr[ni][nj])
            if len(n) != 9:
                result = 0
    print(f"#{tc} {result}")