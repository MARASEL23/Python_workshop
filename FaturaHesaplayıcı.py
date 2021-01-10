fatura = int(input("Faturanızı Yazınız : "))
bahşiş = int(input("Bahşiş yüzdesini yazınız ( 12 ,15 ,17 ) : "))
kişi = int(input("Kaç kişi ödeyeceksiniz: "))

bahiş_yüzde = fatura / 100
bahşişmiktar = bahiş_yüzde * bahşiş
toplamfatura = fatura + bahşişmiktar
kişibaşıpara = toplamfatura / kişi
finalamount  = round(kişibaşıpara,2)

print(f"Kişi başı ödenen para : {finalamount}")


