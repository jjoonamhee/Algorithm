T = int(input())
for t in range(1, T+1):
    word = input()
    result = 1

    start, end = 0, len(word)-1 # 회문검사 시작점과 끝점 설정
    for _ in range(len(word)//2):
        if word[start] != word[end]:
            result = 0
            break
        else:
            start += 1
            end -= 1

    print(f"#{t} {result}")