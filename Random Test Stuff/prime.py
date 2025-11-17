x = 1
for y in range(100):
    IsPrime = True
    x+=1
    for i in range(1,x-1):
        if(x%i == 0):
            IsPrime = False
    if(IsPrime):
        print(f"{x} is prime.")