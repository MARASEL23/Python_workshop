import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

nick = input("Nickinizi giriniz : ")
nickTitle = nick.title()
handList = [rock, paper, scissors]

userSelect = int(input(f"{nickTitle} oyun masasına hoşgeldin. Başlayalım mı ?\nTaş için 0 , Kağıt için 1 , Makas için 2 \n> "))
if userSelect >= 3 or userSelect < 0:
    print("Hatalı bir tuşlama yaptınız.Kaybettiniz !")
else:
    print(f"{nick} Seçimi: ")
    print(handList[userSelect])

    computerSelect = random.randint(0, 2)
    print("Bilgisayarın Seçimi:")
    print(handList[computerSelect])


    if userSelect == 0 and computerSelect == 2:
        print("Tebrikler,kazandınız!")
    elif computerSelect == 0 and userSelect == 2:
        print("Maalesef,kaybettiniz !")
    elif computerSelect > userSelect:
        print("Maalesef,kaybettiniz !")
    elif userSelect > computerSelect:
        print("Tebrikler,kazandınız!")
    elif computerSelect == userSelect:
        print("Berabere kaldınız !")