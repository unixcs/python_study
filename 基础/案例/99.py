for x in range(1,10):
    print("\t")
    for y in range(1,x+1):
        result = x * y
        print("%d * %d = %d " %(x,y,x*y),end="\t")