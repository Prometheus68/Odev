from re import split

Alfabe = ['a', 'b', 'c','ç','d', 'e', 'f', 'g','ğ' ,'h','ı', 'i', 'j', 'k', 'l', 'm', 'n','o','ö', 'p', 'r', 's','ş','t', 'u','ü', 'v', 'y', 'z']#Alfabe isimli dizi oluşturdum
key = list(input("Lütfen bir key girin"))#kullanıcının girdiği key'i key isimli diziye attım
sifre_uzunluk=[]#sifre_uzunluk isimli bir tane boş dizi oluşturdum
sifrelenmis=[]#sifrelenemis isimli bir tane boş dizi oluşturdum
Metin = input("Lütfen bir metin girin")#Kullanıcıdan bir metin girmesini istedim ve girdiği metini Metin isimli değişkenin içerisine attım
cozum_metin=[]


def sifrele (k):#sifrele isimli bir tane fonksiyon oluşturdum
    sayac = 0#key listesşni büyütmek için sayac
    sayac2 = 0#sayac2 ile girilen metin ile key indexlerini topladığımız while'ın
    sayac3 = 0#sayac3 ile toplanmış indexlerin olduğu verileri sifrelediğimiz while'ın


    while sayac < k:#Bir tane while döngüsü oluşturdum
        key.append(key[sayac])#Adım boyunca key içindeki verileri tek tek sona ekliyoruz
        sayac += 1#sayac'ı 1 artırdım
    while len(Metin) > sayac2:#Metin büyüklüğünde bir while döngüsü oluşturdum
        sifre_uzunluk.append(Alfabe.index(Metin[sayac2]) + Alfabe.index(key[sayac2]))#albabedeki değerleri index diyerek içindeki verinin kaçıncı indexe denk geldiklerine baktık bu işlemi hem metin hem key için yapıp diziye attık
        sayac2 += 1#sayac2 isimli değişkeni 1 artırdım
    while len(sifre_uzunluk) > sayac3:#sifre_uzunluk büyüklüğünde bir tane while döngüsü oluşturdum
        modlanmis = sifre_uzunluk[sayac3] % 29#sifre_uzunluk isimli dizinin içerisindeki değerlerin alfabeye göre modunu alıp modlanmis isimli değişkene attım
        sifrelenmis.append(Alfabe[modlanmis])#Sonra modlu değerlerin alfabeye göre değerini alıp sifrelenmis isimli değişkene attıjm
        sayac3 += 1#sayac3 isimli değişkeni 1 artırdım

def coz():#çöz fonksiyonu tanımlandı
    sayac = 0
    while len(sifrelenmis)>sayac:#şifrelenmis metin uzunluğunda çalışıcak

        cozum=abs(Alfabe.index(key[sayac])-Alfabe.index(sifrelenmis[sayac]))%29#her bir key harfinin indexinden şifrelnmiş metnin harfinin uzunluğu çıkarılıp modu alındı

        cozum_metin.append(Alfabe[cozum])
        sayac +=1



if(len(Metin)>len(key)):#Eğer metin key'den bğyükse
    uzunluk = len(Metin)-len(key)#metinin boyutundan keyin değerini çıkardım
   # print(uzunluk)
    sifrele(uzunluk)#Sonra bunu sifrele isimli fonksiyona gönderdim


elif(len(key)>len(Metin)):#Eğer key metin'den büyükse
    uzunluk = len(key)-len(Metin)#key'den Metin'i çıkardım
    key.reverse() # listeyi ters çevirdim
    sayac = 0#sayac isimli değişken oluşturup değerini 0 girdim
    while sayac < uzunluk: #ters çevirilmiş dizinin sırayla elemanını silicez
        key.pop(0)#her seferinde son indexi siliyoruz
        sayac += 1
    key.reverse()#key listesini eski haline getirdik
    sifrele(uzunluk)

else:
    sifrele(0) #key ile metin aynı boydaysa direkt şifrelicek

print("Şifreleyen Metin",key)
print("Şifrelenecek Metin",Metin)
print("Şifrelenmis Metin",sifrelenmis)
coz()
print("Çözülmüş Metin ",cozum_metin)