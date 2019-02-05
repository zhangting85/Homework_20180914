# -*- coding:utf-8 -*-：

with open('3.csv','r+') as f:
    r=f.readlines()
    with open('4.csv', 'a+') as nf:
        nf.write(r[0])
    for i in range(1,len(r)):
        s=r[i].split(',', 2)
        t=s[1]
        t=float(t)
        t*=0.8
        t=round(t,2)
        s=s[0]+','+str(t)+','+s[2]
        with open('4.csv','a+') as nf:
            nf.write(str(s))


