for i in range(1,400):
    s = i
    n = 0
    a = 0
    while s+n<=300:
        s-=5
        n+=25
    if n == 250:
        print(i,"=",n)
    
