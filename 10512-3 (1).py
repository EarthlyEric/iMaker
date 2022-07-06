import math
num=int(input("請輸入正整數:"))
for i in range(2,int(math.sqrt(num))+1):
    if num%i == 0:
        print("%d不是質數" % (num))
        exit()
print("%d是質數" % (num))