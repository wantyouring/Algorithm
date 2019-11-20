a = input()
b = input()
c = input()

'''
black	0	1
brown	1	10
red	    2	100
orange	3	1000
yellow	4	10000
green	5	100000
blue	6	1000000
violet	7	10000000
grey	8	100000000
white	9	1000000000
'''

def func(str,mul):
    if str == 'black':
        if mul:
            return 1
        else:
            return 0
    elif str == 'brown':
        if mul:
            return 10
        else:
            return 1
    elif str == 'red':
        if mul:
            return 100
        else:
            return 2
    elif str == 'orange':
        if mul:
            return 1000
        else:
            return 3
    elif str == 'yellow':
        if mul:
            return 10000
        else:
            return 4
    elif str == 'green':
        if mul:
            return 100000
        else:
            return 5
    elif str == 'blue':
        if mul:
            return 1000000
        else:
            return 6
    elif str == 'violet':
        if mul:
            return 10000000
        else:
            return 7
    elif str == 'grey':
        if mul:
            return 100000000
        else:
            return 8
    elif str == 'white':
        if mul:
            return 1000000000
        else:
            return 9

a = func(a,False)
b = func(b,False)
c = func(c,True)

if a==0:
    if b==0:
        print(0)
    else:
        print(b*c)
else:
    print((a*10 + b)*c)