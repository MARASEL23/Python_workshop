print('''

                                    __________
                           ________|          |________
                          |       /   ||||||   \       |
                          |     ,'              `.     |
                          |   ,'                  `.   |
                          | ,'   ||||||||||||||||   `. |
                          ,'  /____________________\  `.
                         /______________________________ |
                        |                                |
                        |                                |
                        |                                |
                        |________________________________|
                        |____________________--------__|

              ,----------------------------------------------------,
              | [][][][][]  [][][][][]  [][][][]  [][__]  [][][][] |
              |                                                    |
              |  [][][][][][][][][][][][][][_]    [][][]  [][][][] |
              |  [_][][][][][][][][][][][][][ |   [][][]  [][][][] |
              | [][_][][][][][][][][][][][][]||     []    [][][][] |
              | [__][][][][][][][][][][][][__]    [][][]  [][][]|| |
              |   [__][________________][__]              [__][]|| |
              `----------------------------------------------------'
''')

print("MARASEL GAME TABLE ---> OYUNUMA HOŞGELDİNİZ")
print("*******************************************")

print("Marasel Adasına Hoşgeldin. Adada Saklı Olan Hazineleri Bulmaya Hazır Mısın ?")
onay = input("Y/N ? ")

if onay == "Y":
    print("********************************************************************************")
    devam = input("Bunu Duyduğuma Çok Sevindim. Hikayemiz Başlıyor. Devam etmek için 1'e basınız! : ")
    if devam == "1":
        print("Günlerdir uçsuz bucaksız bir denizdesin. İki gün önce geminize aldığınız hasar sonucu malesef mürettabatınızda sadece siz hayatta kaldınız.")
        print("Küçük bir bot ile umutsuz bir şekilde denizde sürükleniyorsunuz.Yemeğiniz ve suyunuz bitmek üzere. O da ne bir ada buldunuz. Hemen adaya doğru kürek çekmeye başlıyorsunuz.")
        print("Adaya çıktığınızda büyük bir kaya görüyorsunuz. Fakat iki girişi var.")
        print("***************************************************************************")
        giris1 = input("Hangi Girişi Tercih Ediceksiniz ? Sol Kapı için : 1'e  , Sağ Kapı İçin : 2'ye Basınız....")
        if giris1 == "1":
            print("İlerlemek için sol kapıyı seçtiniz. Olamaz girdiğiniz giriş bir uçuruma çıkıyormuş. Malesef Seçiminiz Yanlış!")
        elif giris1 == "2":
            print("İlerlemek için sağ kapıyı seçtiniz. Mağarada ilerlemeye başlıyorsunuz.İçerisi zifiri karanlık.İleri de bir ışık görüyorsunuz ve meraktan oraya doğru gidiyorsunuz.")
            print("Işığın olduğu yer bir ormana çıkıyor.")
            orman = input("Ormana giricekmisiniz yoksa mağaradan devam mı ediceksiniz ? Orman için : 1 , Mağara İçin : 2 Basınız.... : ")
            if orman == "1":
                print("Büyük bir cesaret ile ormana daldınız. Gemicilik okulunda öğrendiğiniz bitki dersleri sayesinde zehirli olmadığından emin olduğunuz meyveleri ile karnınızı doyurdunuz.")
                print("Hava yavaştan kararmaya başladığı için gece uyumak için bir yer aramaya başlıyorsunuz. Topladığınız çalı çırpı ile uyucak yer yapmaya başlıyorsunuz. ")
                yer = input("Yatacağınız yeri belirlemeniz gerek. Geceyi ağaçta mı geçiriceksiniz yoksa topladığınız çalı çırpılar ile zeminde mi bir yer yapıcaksınız ?\n Ağaç için : 1 , Zemin için : 2 Basınız..... : ")
                if yer == "1":
                    print("Geceyi geçirmek için ağaca çıktınız.Güzel bir uykudan sonra sabah devam ettiniz. Ormanda ilerledikçe uzaktan sesler gelmeye başladı. Adanın yerli halkı.Hemen saklandınız")
                    yamyam = input("Şuan ne yapmak istiyorsunuz : \n İletişime Geç : 1 \n Saklan : 2 \n Oradan hemen kaç : 3 \n Cevabınınız? : ")
                    if yamyam == "1":
                        print("Adanın yerli halkı ile iletişime geçmeye çalıştınız fakat sizi ormanda kovalamaya başlayıp öldürdüler")
                        print("GAME OVER.........")
                        print("""
          /)               ,-^-----^-. 
         //               /           \
.-------| |--------------/  __     __  \-------------------.__
|WMWMWMW| |>>>>>>>>>>>>> | />>\   />>\ |>>>>>>>>>>>>>>>>>>>>>>:>
`-------| |--------------| \__/   \__/ |-------------------'^^
         \\               \    /|\    /
          \)               \   \_/   /
                            |       |
                            |+H+H+H+|
                            \       /
                             ^-----^                """)

                    elif yamyam == "2":
                        print("Saklanmaya başladın.Kısa bir süre sonra oradan uzaklaştın ve adanın sahiline ulaştın. Şans eseri oradan geçen bir balıkçı teknesi seni farkediyor ve teknesine alıyor seni.")
                        print("TEBRİKLER BÖLÜMÜ GEÇTİNİZ...... !")
                        print("""
       __    __    __
                             |==|  |==|  |==|
                           __|__|__|__|__|__|_
                        __|___________________|___
                     __|__[]__[]__[]__[]__[]__[]__|___
                    |............................o.../
                    \.............................../
               hjw_,~')_,~')_,~')_,~')_,~')_,~')_,~')/,~')_                     """)
                    elif yamyam == "3":
                        print("Hemen kaçmaya başladınız. Fakat adanın yamyamları sizi farketti ve kovalamaya başladı. Malesef yakalayıp öldürdüler.")
                        print("GAME OVER...........")
                        print("""
          /)               ,-^-----^-. 
         //               /           \
.-------| |--------------/  __     __  \-------------------.__
|WMWMWMW| |>>>>>>>>>>>>> | />>\   />>\ |>>>>>>>>>>>>>>>>>>>>>>:>
`-------| |--------------| \__/   \__/ |-------------------'^^
         \\               \    /|\    /
          \)               \   \_/   /
                            |       |
                            |+H+H+H+|
                            \       /
                             ^-----^                                        """)
                    else:
                        print("Herhangi bir seçim yapmadığın için öldün.")
                        print("GAME OVER.......................................")
                        print("""
          /)               ,-^-----^-. 
         //               /           \
.-------| |--------------/  __     __  \-------------------.__
|WMWMWMW| |>>>>>>>>>>>>> | />>\   />>\ |>>>>>>>>>>>>>>>>>>>>>>:>
`-------| |--------------| \__/   \__/ |-------------------'^^
         \\               \    /|\    /
          \)               \   \_/   /
                            |       |
                            |+H+H+H+|
                            \       /
                             ^-----^                                         """)
        else:
            print("Malesef hiçbir kapıya girmediniz.Adada yaşayan bir yabani tarafından Öldürüldünüz.")
            print("GAME OVER.................. ")
            print("""
            
          /)               ,-^-----^-. 
         //               /           \
.-------| |--------------/  __     __  \-------------------.__
|WMWMWMW| |>>>>>>>>>>>>> | />>\   />>\ |>>>>>>>>>>>>>>>>>>>>>>:>
`-------| |--------------| \__/   \__/ |-------------------'^^
         \\               \    /|\    /
          \)               \   \_/   /
                            |       |
                            |+H+H+H+|
                            \       /
                             ^-----^
            """)

else:
    print("Anlıyorum. Bu Büyülü Maceraya Hazır Olduğunda Seni Tekrardan Bekliyoruz!")


print("Umarım Eğlenmişsinizdir. \n ................MARASEL.............")



