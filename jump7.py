a=0
while a in range(100):
    a=a+1
    if a%7==0 or (a//10)%10==7 or a%10==7: 
        continue
    else:
        print(a)
