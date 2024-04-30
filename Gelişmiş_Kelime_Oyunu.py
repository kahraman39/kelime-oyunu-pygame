import pygame as pg
import random, sys
def kutu_koy():
    ekran.blit(harf_kutusu, (index*110+290,330))

pg.init()
pg.display.set_caption("Kelime Oyunu")

ekran = pg.display.set_mode((1400,730))
zaman = pg.time.Clock()   

arkaplan_yüzeyi = pg.image.load("arkaplan.png").convert()

harf_kutusu = pg.image.load("harf_kutusu.png").convert_alpha()

sorular = ["1- Hamur kızartması",
"2- Yaprakları salata olarak yenen baharlı bir bitki",
"3- Bir emek sonucu ortaya konulan ürün, eser",
"4- Futboldaki canlı barikat",
"5- Kısa süreli, beklenmedik saldırı",
"6- Halk ağzında küçük sıvı püskürteçlerine verilen ad",
"7- Kandaki alkol miktarını gösteren birim",
"8- Yıkanma, tıraş olma, giyinme, süslenme işi.",
"9- sesi büyütüp, yükseltip uzaklara ileten koni biçiminde aygıt.",
"10- Hıristiyan olmayan toplumlarda bu dini yaymaya çalışan kimse.",
"11- Endüstri Mühendisliği'nin en önemli alanlarından , ... araştırması",
"12- Aralarında ya da parçaları arasında bakışım bulunan",
"13- Yayılı aletler, bisiklet, araba parçaları, araba tekerliği ve aksamı",
"14- X Y düzlemi, iki şerli 6 tane rakam, küp çizimi, dünya çizimi",
"15- boyları 1 milimetreyle 1 metre arasında değişen elektromanyetik salınım",
"16- Belirsizlik ilkesi'ni öne süren Alman Fizikçi", "OYUN BİTTİ"]
cevaplar = ["PİŞİ","TERE","YAPIT","BARAJ","BASKIN","FISFIS","PROMİL","TUVALET","MEGAFON","MİSYONER","YÖNEYLEM","SİMETRİK","AMARTİSÖR","KOORDİNAT","MİKRODALGA","HEİSENBERG",""]


oyun_fontu = pg.font.Font(None,45)
kutuları_yerleştir = False
soru_indexi = -1
harf_alayım = False
kelimeyi_göster = False
süreyi_durdur = False
alınan_harf_sayısı = 0
skor = 0
harf_yeri = 0
toplam_alınan_harf = 0
alınan_harfler = []
harf_dörtgenleri = []
yazı_yüzeyleri = []
harf_dörtgenleri2 = []
yazı_yüzeyleri2 = []
alınan_harf_indexi = []

alınmayan_harf_sayısı = 0
durdurulan_süre_soruluk = 0
toplam_durdurulan_süre = 0

while True:
    gerçek_zaman = pg.time.get_ticks()
    ekran.blit(arkaplan_yüzeyi,(0,0))
    for olay in pg.event.get():
        if olay.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
        if olay.type == pg.KEYDOWN:
            if olay.key == pg.K_RETURN:
                kutuları_yerleştir = True
                soru_indexi += 1
                alınan_harfler = []
                harf_dörtgenleri = []
                yazı_yüzeyleri = []
                harf_dörtgenleri2 = []
                yazı_yüzeyleri2 = []                
                alınan_harf_indexi = []
                skor += (100*alınmayan_harf_sayısı)
                alınan_harf_sayısı = 0
                toplam_durdurulan_süre += durdurulan_süre_soruluk
                durdurulan_süre_soruluk = 0
                süreyi_durdur = False
                kelimeyi_göster = False

            if olay.key == pg.K_SPACE:
                harf_alayım = True
            if olay.key == pg.K_BACKSPACE:
                sürenin_durdurulduğu_an = gerçek_zaman
                süreyi_durdur = True
            if olay.key == pg.K_RSHIFT:
                kelimeyi_göster = True


    if kutuları_yerleştir == True:
        for index in range(len(cevaplar[soru_indexi])):
            kutu_koy()
        soru_yüzeyi = oyun_fontu.render(sorular[soru_indexi],True,(255,255,255))
        soru_dörtgeni = soru_yüzeyi.get_rect(topleft = (250,550))
        ekran.blit(soru_yüzeyi,soru_dörtgeni)
        kutuları_yerleştir == False
    
    if harf_alayım == False:
        alınmayan_harf_sayısı = len(cevaplar[soru_indexi]) - alınan_harf_sayısı

    if harf_alayım == True:
        harf_yeri = "muz"
        uygun_harf = True
        alınmayan_harf_sayısı = len(cevaplar[soru_indexi]) - alınan_harf_sayısı
        while uygun_harf:
            if len(alınan_harf_indexi) != len(cevaplar[soru_indexi]):
                harf_yeri = random.randint(0, len(cevaplar[soru_indexi])-1)
                if not harf_yeri in alınan_harf_indexi:
                    alınan_harf_indexi.append(harf_yeri)
                    uygun_harf = False 
                    alınan_harf_sayısı += 1
            if len(alınan_harf_indexi) == len(cevaplar[soru_indexi]):
                harf_alayım = False
                alınmayan_harf_sayısı = 0
        for i in alınan_harf_indexi:
            yazı = pg.font.Font(None, 100)
            yazı_yüzeyi = yazı.render(cevaplar[soru_indexi][i], True,(0,0,0))
            yazı_yüzeyleri.append(yazı_yüzeyi)
            harf_dörtgeni = yazı_yüzeyi.get_rect(center = (i*110+345,395))
            harf_dörtgenleri.append(harf_dörtgeni)    
        harf_alayım = False

    for j in range(len(harf_dörtgenleri)):
        ekran.blit(yazı_yüzeyleri[j],harf_dörtgenleri[j])
    

    skorrr = pg.font.Font(None, 75)
    skor_yüzeyi = skorrr.render(str(skor), True,(0,0,0))
    ekran.blit(skor_yüzeyi, (250,205))
    
    renk = (0,0,0)
    sayaç = pg.font.Font(None,65)
    if süreyi_durdur == True:
        durdurulan_süre_soruluk = gerçek_zaman - sürenin_durdurulduğu_an
        renk = (255,0,0)

    sayaç_yüzeyi = sayaç.render(str(int(0)), True,(0,0,0))
    sayaçtan_eksilen = gerçek_zaman-durdurulan_süre_soruluk - toplam_durdurulan_süre

    if sayaçtan_eksilen >= 0 and sayaçtan_eksilen < 60000:
        dakika = f'5:{59 - int((sayaçtan_eksilen)/1000)}'
        sayaç_yüzeyi = sayaç.render(str(dakika), True,renk)
    if sayaçtan_eksilen >= 60000 and sayaçtan_eksilen < 120000:
        dakika = f'4:{119 - int(sayaçtan_eksilen/1000)}'
        sayaç_yüzeyi = sayaç.render(str(dakika), True,renk)
    if sayaçtan_eksilen >= 120000 and sayaçtan_eksilen < 180000:
        dakika = f'3:{179 - int(sayaçtan_eksilen/1000)}'
        sayaç_yüzeyi = sayaç.render(str(dakika), True,renk)
    if sayaçtan_eksilen >= 180000 and sayaçtan_eksilen < 240000:
        dakika = f'2:{239 - int(sayaçtan_eksilen/1000)}'
        sayaç_yüzeyi = sayaç.render(str(dakika), True,renk)
    if sayaçtan_eksilen >= 240000 and int(sayaçtan_eksilen) < 300000:
        dakika = f'1:{299 - int(sayaçtan_eksilen/1000)}'
        sayaç_yüzeyi = sayaç.render(str(dakika), True,renk)
    if sayaçtan_eksilen >= 240000 and int(sayaçtan_eksilen) < 300000:
        dakika = f'0:{359 - int(sayaçtan_eksilen/1000)}'
        sayaç_yüzeyi = sayaç.render(str(dakika), True,renk)    
    
    if kelimeyi_göster == True:
        for i in range(len(cevaplar[soru_indexi])):
            yazı2 = pg.font.Font(None, 100)
            yazı_yüzeyi2 = yazı2.render(cevaplar[soru_indexi][i], True,(0,0,0))
            yazı_yüzeyleri2.append(yazı_yüzeyi2)
            harf_dörtgeni2 = yazı_yüzeyi2.get_rect(center = (i*110+345,395))
            harf_dörtgenleri2.append(harf_dörtgeni2) 

        for j in range(len(cevaplar[soru_indexi])):
            ekran.blit(yazı_yüzeyleri2[j],harf_dörtgenleri2[j])

    ekran.blit(sayaç_yüzeyi, (250,255))
            
    pg.display.update()
    zaman.tick(60)