T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ls = list(map(int, input().split()))
    multiply = []
    multiply_max = -1
    
    # Ai * Aj
    for i in range(N-1):
        for j in range(i+1, N):
            multiply.append(ls[i] * ls[j])
    
    # 단조 증가
    for i in range(len(multiply)):
        mtp = multiply[i]
        str_mtp = str(mtp)
        corr = True
        for j in range(1, len(str_mtp)):
            if len(str_mtp) == 1 or str_mtp[j-1] > str_mtp[j]:
                corr = False
                break
        if corr and multiply_max < mtp:
            multiply_max = mtp
    
    print(f"#{tc} {multiply_max}")