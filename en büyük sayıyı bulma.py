print(" üç adet sayı giriniz ")

a = int(input("birinci sayıyı giriniz:"))
b = int(input("ikinci sayıyı giriniz:"))
c = int(input("üçüncü sayıyı giriniz:"))

if (a>=b and a>=c):
    print(a)

elif (b >= a and b >= c):
    print(b)
    
elif (c>= a and c>= b):
    print(c)
    
