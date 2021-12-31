print("lütfen üç notunuzu da giriniz")

a = int(input("1. vizenizi giriniz:"))
b = int(input("2. vizenizi giriniz:"))
c = int(input("final notunuzu giriniz:"))

genel_not = a*(1/3) + b*(1/3) + c*(4/10)

if (genel_not >= 90):
    print("AA")
    
elif (genel_not >= 85):
    print("BA")
    
elif (genel_not >= 80):
    print("BB")
    
elif (genel_not >= 75):
    print("CB")
    
elif (genel_not >= 70):
    print("CC")
    
elif (genel_not >= 65):
    print("DC")
    
elif (genel_not >= 60):
    print("DD")

elif (genel_not >= 55):
    print("FD")
    
elif (genel_not >= 50):
    print("FF")

else :
    print("sınıfta kaldınız")
    
