def notlar(ogrenci):
    ogrenci = ogrenci[:-1]
    liste = ogrenci.split(",")
    isim = liste[0]
    vize1 = int(liste[1])
    vize2 = int(liste[2])
    final = int(liste[3])
    ortalama = vize1 * (3/10) + vize2 * (3/10) + final*(4/10)


# Bunları elif yapcaksın ki hepsine ayrı ayrı bakmasın
# Öbür türlü ilk kabul ettiği ifi alır okler ben bunu çalıştırınca farkettim
# Herkesin notu DD çıkıyo
#Şu an iyi
#31
    if(ortalama >= 90):
        harf = "AA"
    elif(ortalama >= 85):
        harf = "BA"
    elif(ortalama >= 80):
        harf = "BB"
    elif(ortalama >= 75):
        harf = "CB"
    elif(ortalama >= 70):
        harf = "CC"
    elif(ortalama >= 65):
        harf = "DC"
    elif(ortalama >= 60):
        harf = "DD"
    else:
        harf = "FF"
    return isim + " ------> " + harf + " \n"

notlar_listesi = list()
with open("dosya.txt","r",encoding="utf-8") as file:
    for i in file.readlines():
        notlar_listesi.append(notlar(i))
with open("notlar.txt","w",encoding="utf-8") as file2:
    for i in notlar_listesi:
        file2.write(i)
        print(i)
kalanlar = []
geçenler = []
tumu = [] # Bunu beraber yapmıştık zaten
with open("notlar.txt","r",encoding="utf-8") as file3:
    for i in file3.readlines():
        # Readlines kullanınca listeye atıyor daha kolay oluyo bizim için
        new_notes = i[:-2].split("\n")
        tumu.append(new_notes)
        
    for j in tumu:
        #j[0] olmasının nedeni de listeye normal j dersek ['Mehmet Babacan --> FF'] diye alır ve FF yok bunda
        # Alabilmesi için j[0] yapıp ilk indeksin içini yani bi stringin içini arıyoruz
        # Eğer FF diye bi liste öğesi olsa doğru olurdu.
        if("FF" in j[0]):
            kalanlar.append(j[0])
        else:
            geçenler.append(j[0])
with open("geçenler.txt","w",encoding="utf-8") as file4:
    for i in geçenler:
        file4.write(i + "\n")
#burayı yapmadan önce for i in geçenlerdi düzelttim
with open("kalanlar.txt","w",encoding="utf-8") as file5:
    for i in kalanlar:
        file5.write(i + "\n") # \n le n leri silmiştik geri atıyoz dosyaya