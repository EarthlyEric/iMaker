h = int(input('請輸入邊長:'))
for x in range(h+1): 
    for y in range(x): 
        print("*",end="") 
    print()
for x in range(h,-1,-1):
    for y in range(x):
        print("*",end="")
    print()