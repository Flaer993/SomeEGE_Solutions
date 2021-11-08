from collections import Counter
n =(2*343**123+2401)*(3*343**137-2401)
k = int(input())
i = int(input())
ls= []
while n > 0:
    n, a = divmod(n,k)
    ls = [a] + ls
c = Counter(ls)
print(*ls)
print(c[i])
#№15:4
#№16:24
#№17:227
#№18:5
#№19:407
