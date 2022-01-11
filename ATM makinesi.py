print("""
*******************************************

           Atm ye hoşgeldiniz
         
 işlemler;

1-Bakiye sorgulama
     
2-Para yatırma            
      
3-Para çekme      

      Çıkmak için "Q" ya basınız
********************************************     
""")

bakiye = 2000

while True:
    işlem = input("İşlem giriniz:")

    if (işlem == "q"):
        print("Çıkış yapılıyor...")
        break

    elif (işlem == "1"):
        print("Bakiyeniz {}  Tl dir.".format(bakiye))
        
    elif (işlem == "2"):
        
        miktar = int(input("Lütfen miktarı giriniz:"))
        bakiye += miktar
        
    elif (işlem == "3"):
        
        miktar = int(input("Lütfen miktarı giriniz:"))
        
        if(bakiye - miktar < 0 ):
            print("Böyle bir miktar çekemezsiniz")
            continue
        
    else:
        print("Geçersiz işlem")
        
        
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                 
                             
        
    
