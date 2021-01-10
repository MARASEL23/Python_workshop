print("MARASEL PİZZA KAFEYE HOŞGELDİNİZ")
print("*********************************************")
print("\n MENÜMÜZ : \n Small Pizza : $15 \n Medium Pizza : $20 \n Large Pizza : $25")

seçim = input("\nLütfen Seçtiğiniz Pizzanın Baş Harfine Tıklayınız : ")
smallpizza = 15
mediumpizza = 20
largepizza = 25
speynir = 2
mpeynir = 3
lpeynir = 4
peperoni = 1



if seçim == "S":
    smallpeynir = input("$2 Fark ile Peynir istermisin Y or N : ")
    if smallpeynir == "Y":
        pay = speynir + smallpizza
        pepe = input("$1 Fark ile Peperoni istermisin Y or N : ")
        if pepe == "Y":
            pay = speynir + smallpizza + peperoni
            print(f"Ödemeniz Gereken Tutar: ${pay}")
        if pepe == "N":
            print(f"Ödemeniz Gereken Tutar: ${pay}")

    if smallpeynir == "N":
        pepe = input("$1 Fark ile Peperoni istermisin Y or N : ")
        if pepe == "Y":
            pay = smallpizza + peperoni
            print(f"Ödemeniz Gereken Tutar: ${pay}")
        if pepe == "N":
            print(f"Ödemeniz Gereken Tutar: ${smallpizza}")



elif seçim == "M":
    mediumpeynir = input("$2 Fark ile Peynir istermisin Y or N : ")
    if mediumpeynir == "Y":
        pay = mpeynir + mediumpizza
        pepe = input("$1 Fark ile Peperoni istermisin Y or N : ")
        if pepe == "Y":
            pay = mpeynir + mediumpizza + peperoni
            print(f"Ödemeniz Gereken Tutar: ${pay}")
        if pepe == "N":
            print(f"Ödemeniz Gereken Tutar: ${pay}")

    if mediumpeynir == "N":
        pepe = input("$1 Fark ile Peperoni istermisin Y or N : ")
        if pepe == "Y":
            pay = mediumpizza + peperoni
            print(f"Ödemeniz Gereken Tutar: ${pay}")
        if pepe == "N":
            print(f"Ödemeniz Gereken Tutar: ${mediumpizza}")



elif seçim == "L":
    largepeynir = input("$2 Fark ile Peynir istermisin Y or N : ")
    if largepeynir == "Y":
        pay = lpeynir + largepizza
        pepe = input("$1 Fark ile Peperoni istermisin Y or N : ")
        if pepe == "Y":
            pay = lpeynir + largepizza + peperoni
            print(f"Ödemeniz Gereken Tutar: ${pay}")
        if pepe == "N":
            print(f"Ödemeniz Gereken Tutar: ${pay}")

    if largepeynir == "N":
        pepe = input("$1 Fark ile Peperoni istermisin Y or N : ")
        if pepe == "Y":
            pay = largepizza + peperoni
            print(f"Ödemeniz Gereken Tutar: ${pay}")
        if pepe == "N":
            print(f"Ödemeniz Gereken Tutar: ${largepizza}")
print("\nBizi Tercih Ettiğiniz İçin Teşekkürler")
