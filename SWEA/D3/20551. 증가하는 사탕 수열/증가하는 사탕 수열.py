T = int(input())
for tc in range(1, T+1):
    order = list(map(int, input().split()))
    eat = 0
    print(f'#{tc}', end = ' ')

    # 두번째 사탕은 2개보다는 많아야 하고, 세번째 사탕은 3개보다는 많아야 함
    if order[1] < 2 or order[2] < 3: # 불가능
        print(-1) 
    else:
        if order[1] >= order[2]: # 뒤부터 작업
            eat += order[1] - order[2] + 1
            order[1] = order[2] - 1
        if order[0] >= order[1]:
            eat += order[0] - order[1] + 1
        
        print(eat)