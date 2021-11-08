for i in range(1,100):
    x = i
    L = 0
    M = 0
    while x > 0:
        M+=2
        if x %8!=0:
           L+=1
        x//=8
    if L==2 and M==6:
        print(i,"=",L,", ", M)


