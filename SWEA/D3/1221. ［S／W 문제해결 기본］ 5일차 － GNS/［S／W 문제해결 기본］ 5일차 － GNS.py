T = int(input())

dict = {"ZRO" : 0,
        "ONE" : 1,
        "TWO" : 2,
        "THR" : 3,
        "FOR" : 4,
        "FIV" : 5,
        "SIX" : 6,
        "SVN" : 7,
        "EGT" : 8,
        "NIN" : 9}

for t in range(T):
    test_case, test_len = map(str, input().split())
    test_len = int(test_len)
    lst = input().split()
    lst_cnt = [0] * len(lst)
    lst_sort = [-1] * len(lst)

    # 카운팅 정렬
    for i in range(len(lst)): # lst_cnt 인덱스에 카운팅
        lst_cnt[dict[lst[i]]] += 1
    for i in range(1,len(lst_cnt)): # 누적합
        lst_cnt[i] += lst_cnt[i-1]
    for i in range(len(lst)):
        lst_cnt[dict[lst[i]]] -= 1
        lst_sort[lst_cnt[dict[lst[i]]]] = lst[i]
    print(test_case)
    print(' '.join(lst_sort))