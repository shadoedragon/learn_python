for n in range(100,999,1):
    x = n//100
    y = (n-x*100)//10
    z = n-(x*100+y*10)
    ##print(x,y,z)
    if (x**3+y**3+z**3==n):
        print(n)