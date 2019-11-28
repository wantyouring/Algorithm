import math
a = []
for i in range(5):
    a.append(int(input()))

print(a[0] - max(int(math.ceil(a[1]/a[3])),int(math.ceil(a[2]/a[4]))))