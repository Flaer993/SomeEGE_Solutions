for i in range(1,1000):
    x = i
    a = 0; b = 1
    while x >0:
        if x % 2 > 0:
            a = a + x % 12
        else:
            b = b * (x % 12)
        x = x // 12
        if a==5 and b == 16:
            print(i,'=',a)
            print(i,'=',b)
#OTV:356
