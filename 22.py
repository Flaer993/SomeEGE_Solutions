for i in range(1,1000):
    x = i
    a = 0; b = 1
    while x >0:
        if x % 2 > 0:
            a = a + x % 9
        else:
            b = b * (x % 9)
        x = x // 9
    if a==4 and b == 5:
        print(i,'=',a)
        print(i,'=',b)
#OTV:122
