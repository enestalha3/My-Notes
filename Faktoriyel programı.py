print("""
***************************************************    
          Faktöriyel makinesine hoşgeldiniz   
      
   Çıkmak için 'Q' ya basınız.     
***************************************************
      
   """)


while True:
    
    sayı =input("Lütfen bir sayı giriniz:")
    
    if(sayı == "q"):
        print("Çıkış yapılıyor...")
        break 
    
    else:
        sayı = int(sayı)
        
        faktoriyel = 1
        
        for i in range(2,sayı+1):
            faktoriyel *= i
            
        print("faktoriyel:",faktoriyel)
        
        
        
    
      








      