print(""" Şeklin cinsini giriniz;
      
      1- Dörtgen 
      2- Üçgen
      """)
      
şekil =input("lütfen şeklin türünü giriniz:")

if (şekil == "dörtgen"):
    print("dört kenarın uzunluğunu giriniz")
    
    a = int(input("1. kenarın uzunlığunu girin"))
    b = int(input("2. kenarın uzunlığunu girin"))
    c = int(input("3. kenarın uzunlığunu girin"))
    d = int(input("4. kenarın uzunlığunu girin"))
    
    if (abs(a) == abs(b) == abs(c) == abs(d)):
        
        print("şekil kare")
    
    elif (abs(a) == abs(c) and abs(b) == abs(d)):
        print("şekil dikdörtgen")
    
    elif (abs(a) == abs(b) and abs(c) == abs(d)):
        print("şekil dikdörtgen")
        
    else :
        print("şekil dörtgen")
        
elif (şekil == "üçgen"):
    a = int(input("üçgenin 1. kenarını giriniz"))
    b = int(input("üçgenin 2. kenarını giriniz"))
    c = int(input("üçgenin 3. kenarını giriniz"))
    
    if((a+b)>c and (a+c)>b and (b+c)>a):
        if (abs(a) == abs(b) and abs(a)!=abs(c) or abs(a) == abs(c) and abs(a) != abs(c) or  abs(b) == abs(c) and abs(c) != abs(a) ):
            print("üçgen ikizkenar üçgendir")
            
        elif (abs(a) == abs(b) == abs(c)):
            print("üçgen eşkenar üçgendir")
            
        else:
            print("üçgen tanımlanamadı")
            
            
else:
    print("şekil tanımlanhamadı")
    
    
    
    
    