print("""**************************
    Kullanıcı Girişi
      
************************** """)

sys_kullanıcı_adı = "enest3"
sys_parola = "5521"

kullanıcı_adı =input("kullanıcı adı:")
parola =input("parola:")

if (kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola):
    print("parola hatalı")
    
elif (kullanıcı_adı != sys_kullanıcı_adı and sys_parola == parola):
    print("kullanıcı adı hatalı")
    
elif (kullanıcı_adı != sys_kullanıcı_adı and sys_parola != parola):
    print("kullanıcı adı ve parola hatalı ")
    
else :
    print("Başarıyla giriş yaptınız")
    
    






 
