def bi_to_dec(binary): # 1010 str으로 받기
    N = len(binary)
    decimal = 0
    for i in range(N):
        decimal += 2**i * int(binary[N-1-i])
    return decimal

def ter_to_dec(termary): # 212 str으로 받기
    N = len(termary)
    decimal = 0
    for i in range(N):
        decimal += 3**i * int(termary[N-1-i])
    return decimal

T = int(input())
for tc in range(1, T+1):
    binary = input()
    termary = input()

    for i in range(len(binary)): # 한 자리씩 숫자 바꿔보기
        c_bi = list(binary)
        if c_bi[i] == '1': # str은 immutable
            c_bi[i] = '0'
        else: 
            c_bi[i] = '1'
        
        for j in range(len(termary)):
            for k in range(2):
                c_ter = list(termary)
                ls_ter = ['0','1','2']
                ls_ter.remove(c_ter[j])
                c_ter[j] = ls_ter[k]
            
                c_bi = ''.join(c_bi)
                c_ter = ''.join(c_ter)

                if ter_to_dec(c_ter) == bi_to_dec(c_bi):
                    print(f"#{tc} {ter_to_dec(c_ter)}")