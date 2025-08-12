T = int(input())
for tc in range(1, T+1):
    S = input()
    card = [S[3*n-3:3*n] for n in range(1, (len(S)//3)+1)]
    need = [13, 13, 13, 13] # S D H C 순
    ERROR = False

    for i in range(len(card)):
        for j in range(i+1, len(card)):
            if card[i] == card[j]:
                ERROR = True
                break
        if ERROR:
            print(f"#{tc} ERROR")
            break
        
        if card[i][0] == 'S':
            need[0] -= 1
        if card[i][0] == 'D':
            need[1] -= 1
        if card[i][0] == 'H':
            need[2] -= 1
        if card[i][0] == 'C':
            need[3] -= 1
    
    if not ERROR:
        print(f"#{tc} {' '.join(map(str,need))}")