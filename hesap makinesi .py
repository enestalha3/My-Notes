print("""*******************************************

        Hesap makinesi programı

İşlemler;


1. işlem Toplama işlemi.

2. işlem Çıkarma işlemi.

3. işlem Çarpma işlemi.

4. işlem Bölme işlemi.      
      
*******************************************   
     """)

a = int(input("birinci sayı:"))
b = int(input("ikinci sayı:"))

işlem = input("işlem giriniz")

if işlem=="1":
    print("{} ile {} in toplamı {} dir ".format(a,b,a+b))
    
elif işlem=="2":
    print("{} ile {} nin farkı {} dir".format(a,b,a-b))

elif işlem=="3":
    print(" {} ile {} nin çarpımı {} dir".format(a,b,a*b))
    
elif işlem=="4":
    print("{} ile {} nin bölümü {} dir".format(a,b,a/b))

else :
    print("geçersiz işlem")
    

    

    
