N,a,b = map(int,input().split())

cnt = 0
while True:
    cnt += 1
    a = int(a/2) + a%2
    b = int(b/2) + b%2
    if a==b:
        break
print(cnt)