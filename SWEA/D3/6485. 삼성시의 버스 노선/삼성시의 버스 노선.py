T = int(input())
for test_case in range(1, T+1):
    counts = [0] * 5001
    N = int(input()) # 버스 노선 개수
    for i in range(N):
        A, B = map(int, input().split())
        for idx in range(A, B+1):
            counts[idx] += 1

    P = int(input())
    C = []
    for _ in range(P):
        C.append(int(input()))

    print(f"#{test_case}", end=' ')
    for j in C:
        print(counts[j], end=' ')
    print()