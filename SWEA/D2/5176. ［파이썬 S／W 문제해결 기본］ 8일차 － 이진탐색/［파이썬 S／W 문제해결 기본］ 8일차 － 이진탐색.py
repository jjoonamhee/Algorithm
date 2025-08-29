def inorder(node):
    global N, cnt, tree
    
    # 왼쪽 보기
    if node*2 <= N:
        inorder(node*2)

    # 나 보기
    cnt += 1
    tree[node] = cnt

    # 오른쪽 보기
    if node*2+1 <= N:
        inorder(node*2+1)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 0
    N2 = N // 2
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N2]}')
