nb = 'ИГРА'
i = 0
for b1 in nb:
    for b2 in nb:
        for b3 in nb:
            for b4 in nb:
                for b5 in nb:
                                     
                    s = b1 + b2 + b3 +  b4 + b5
                    if s.count('А')==2:
                        i+=1  
                        print(i,' ',s)
