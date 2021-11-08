s = '3' * 250
while '3333' in s or '7777' in s:
    if '3333' in s:
        s = s.replace('3333', '7',1)
    else:
        s = s.replace('777','3',1)
print(s)
#№9:564
