for i in range(1,100):
    s = i
    n = 105
    while n>s:
        s+=3
        n-=2
    if n == 67:
        print(i,"=",n)
    
