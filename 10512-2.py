i = int(input("請輸入單價:"))
i2 = int(input("請輸入數量:"))
if i2>=3:
    i = round(i*i2*0.5)
    print(f"總價：{i}")
elif i2 == 2:
    i = round(i*i2*0.7)
    print(f"總價：{i}")
else:
    print(f"總價：{i}")