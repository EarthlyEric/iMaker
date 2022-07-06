x=int(input('請輸入本金:'))
y=int(input('請輸入年利率(%):'))
z=int(input('請輸入年數:'))
for i in range(z):
    x=x+x*(y/100)
print(round(x))