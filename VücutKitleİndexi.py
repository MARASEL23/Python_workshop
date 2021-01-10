kilo = int(input("Kilonuzu Giriniz ( KG ) : "))
boy = int(input("Boyunuzu Giriniz ( CM ) : "))
boy = boy / 100
sonuc = kilo / (boy**2)
sonuc = round(sonuc)
if sonuc <= 18.5:
    print(f"Vücut Kitle İndexin: {sonuc} Çok Zayıfsın Gardaşım")
elif sonuc <= 25:
    print(f"Vücut Kitle İndexin: {sonuc} Helalin Var Gardaşım Adamsın")
elif sonuc <= 30:
    print(f"Vücut Kitle İndexin : {sonuc} Azıcık Baklavaları Götürmüşsün")
elif sonuc <= 35:
    print(f"Vücut Kitle İndexin : {sonuc} Gardaşım Yapma Böyle Yaa  ")
else:
    print(f"Vücut Kitle İndexin : {sonuc}Gardaşım İşi Gücü Bırak Direk Hastaneye")
