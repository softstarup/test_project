loop = int(input("Tsiklni kiriting: "))
k=0
i=0
while loop:
    son = int(input('Sonni kiriting: '))
    if son > i:
        i = k
        k = son
    print(k, i)
    loop-=1
