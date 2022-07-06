'''
by 10512 
'''

a = int(input('請輸入第一個數字：'))
b = int(input('請輸入第二個數字：'))
print('%d + %d = %d' % (a,b,a+b ))
print('%d - %d = %d' % (a,b,a-b ))
print('%d X %d = %d' % (a,b,a*b ))
print('%d ÷ %d = %f' % (a,b, a/b ))
c = float(input('請輸入圓的半徑：'))
print('圓面積 = %s' % (round(pow(c,2)*3.14,2)))
d = int(input('請輸入雞+兔的總隻數：'))
e = int(input('請輸入雞+兔的總腳數：'))
f= (e-2*d)/2
g= d-f
print('雞 = %d隻,兔 = %d隻'%(g,f))

