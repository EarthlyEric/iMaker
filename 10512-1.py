#!/usr/bin/python3
h = int(input("請輸入身高(公分):"))/100
w = int(input("請輸入體重(公斤):"))
i = w/pow(h,2)
result = round(i,1)
print(f"您的BMI值為: {result}")
if result >= 35:
    print("重度肥胖")
elif result >= 30:
    print("中度肥胖")
elif result >= 27:
    print("輕度肥胖")
elif result >= 24:
    print("過重")
elif result >= 18.5:
    print("正常範圍")
elif result < 18.5:
    print("體重過輕")