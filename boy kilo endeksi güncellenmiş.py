print("""*************************
      
      Beden Kitle Endeksi
**************************

""")

kilo = float(input("kilonuzu giriniz:"))
boy = float(input("boyunuzu giriniz"))

bke = kilo/(boy*boy)

if bke<18.15:
    print("zayıf")
    
elif 18.15<bke<=25:
    print("normal kilo")
    
elif 25<=bke<30:
    print("fazla kilolu")
    
elif 30<bke:
    print("obez")

else :
    print("tanımlanamadı")
    

    

    