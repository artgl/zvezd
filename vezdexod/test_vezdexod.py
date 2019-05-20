def speed(x,y):
    if x < 1499:
        xi = (x - 1499)
        xi = xi + (int(str(xi)[1:]) * 2)
        xi = xi / 2
        xi = int(xi)
    elif x > 1501:
        xi = (x - 1500)/2
        xi = int(xi)
    else:
        xi = 0

    if y < 1499:
        yy = (y - 1499)
        yy = yy + (int(str(yy)[1:]) * 2)
        yy = yy / 2
        yy = int(yy)
        #yy = (y - 1000) * 150 / 1000
        lr = [int(xi-int(yy)),int(xi)]
        if lr[0] < 0:
            lr[0] = 0
    elif y > 1501:
        yy = (y - 1500)/2
        lr = [int(xi),int(xi-yy)]
        if lr[1] < 0:
            lr = [int(xi),int(0)]
    else:
        yy = 0
        lr = [int(xi),int(xi)]

    return xi,lr

for i in range(1001,1999):
    for o in range(1001,1999):
        s = speed(i,o)
        print (s,"s   i",i)