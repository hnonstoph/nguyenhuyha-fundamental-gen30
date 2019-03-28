a=float(input('moi nhap vao chieu cao cua ban theo don vi cm: '))
b=float(input('moi nhap vao can nang cua ban theo don vi kg:'))
bmi=b/((a/100)*(a/100))
if(bmi<16) : print('ban bi thieu can tram trong')
elif(bmi<18.5): print('ban bi thieu can')
elif(bmi<25) : print ('ban binh thuong')
elif(bmi<30) : print ('ban beo')
else : print('ban bi beo phi')
n=int(input('nhap vao so n: '))
m=1
for i in range(1,n+1):
    m=m*i
print("giai thua cua n la: ",m)
print()
print('hello',end=' ')
print(",my name",end=' ')
print('is b-max')
for i in range(20):
    print("*",end=' ')
print()
n=int(input("nhap vao so n "))
for i in range(n):
    print("*",end=' ')
print()
print()
for i in range(n):
    if i%2==0: print("x",end=' ')
    else : print('*',end=' ')
print()
print()

for i in range(3):
    for j in range(7):
        print("*",end=" ")
    print()
print()
n=int(input("nhap vao so n "))
m=int(input("nhap vao so m "))
for i in range(m):
    for j in range(n):
        print("*",end=' ')
    print()