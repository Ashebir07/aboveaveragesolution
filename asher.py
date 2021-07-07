tc=int(input())
for i in range(tc):
    l=[int(i) for i in input().split()]
    h=l[1:]
    s=0
    g=[]
    for i in range(len(h)):
        s+=h[i]
    avg=s/len(h)
    for i in range(len(h)):
        if h[i]<=avg:
            continue
        else:
            g.append(h[i])
    ans=(len(g)/len(h))*100
    print(str("%.3f"%ans)+"%")
