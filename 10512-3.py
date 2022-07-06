i = int(input("請輸入數字："))

str_i = str(i)
x = int(str_i[0])**3
y = int(str_i[1])**3
z = int(str_i[2])**3
if i == x+y+z:
    print(f"{i}是阿姆斯壯數")
else:
    print(f"{i}不是阿姆斯壯數")

