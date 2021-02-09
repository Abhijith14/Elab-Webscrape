num = 1811110
j = 1
for i in range(1,101):
    ans = num + j
    print(ans,j)
    j = j + 1
    if i%10 == 0:
        num = num + 1000
        j = 1