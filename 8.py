st = 'РАЗМАХ'
i =0

for b1 in st:
    for b2 in st:
        for b3 in st:
            for b4 in st:
                for b5 in st:
                    for b6 in st:
                        s = b1+b2+b3+b4+b5+b6
                        if s.count('Р')>3 or s.count('З')>3 or s.count('М')>3 or s.count('Х') >3  :
                            i+=1
print(i)
