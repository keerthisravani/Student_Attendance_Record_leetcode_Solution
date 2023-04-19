def checkRecord(s):
    if s.count('A')>=2:
        return False
    count=0
    max_count=0
    for i in s:
        if i=='L':
            count+=1
        else:
            max_count=max(max_count,count)
            count=0
    max_count=max(max_count,count)
    if max_count<3:
        return True
    else:
        return False
s="APPALLLP"
print(checkRecord(s))