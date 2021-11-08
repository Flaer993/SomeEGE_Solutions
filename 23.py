for i in range(1,100):
    x = i
    Q = 15
    L = 0
    while x >= Q:
        L +=1
        x -=Q
    M = x
    if M < L:
        M = L
        L = x
    if L==3and M == 6:
        print(i,'=',L)
        print(i,'=',M)
#OTV:93
