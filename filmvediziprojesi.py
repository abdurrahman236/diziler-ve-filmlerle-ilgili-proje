import requests
from bs4 import BeautifulSoup

class Diziler:
    def __init__(self) -> None:
        self.url = "https://dizimag.org/trendler"
        self.html = requests.get(self.url).content
        self.soup = BeautifulSoup(self.html, "html.parser")
        
        
    def haftanintrendDizileri(self):
        trenddiziler = (self.soup).find_all('div', {"class": "trends-col w-full md:w-1/3"})[0]
        trenddiziler = trenddiziler.ul.find_all('li')        
        count = 1           
        for dizi in trenddiziler:
            diziler_ = dizi.div.find('h5').text
            puanlar = dizi.div.find('p').text
            print(f"{count}- {diziler_} - {puanlar}")
            count += 1
    
    def haftanintrendFilmleri(self):
        trendfilmler = (self.soup).find_all('div', {"class": "trends-col w-full md:w-1/3"})[1]
        trendfilmler = trendfilmler.ul.find_all('li')
        count = 1
        for film in trendfilmler:
            filmler_ = film.div.find('h5').text 
            puanlar = film.div.find('p').text
            print(f"{count} - {filmler_} - {puanlar}")
            count += 1
           
    def haftanintrendKullanicilari(self):
        trendkullanicilar = (self.soup).find_all('div', {"class": "trends-col w-full md:w-1/3"})[2]
        trendkullanicilar = trendkullanicilar.ul.find_all('li')
        count = 1
        for kullanici in trendkullanicilar:
            kullanicilar_ = kullanici.div.find('h5').text
            puanlar = kullanici.div.find('p').text
            print(f"{count} - {kullanicilar_} - {puanlar}")
            count += 1
    
    def tumzamanlarıntrendleri(self):
        tumtrendler = (self.soup).find('ul', {"class": "w-full table"}).find('li').findNextSiblings()
        count = 1
        for trend in tumtrendler:
            trendler = trend.find_all('div',{"class": "all-time-trends-box table-cell align-middle"})[1].div.div.a
            kategori = trend.find_all('div',{"class": "all-time-trends-box table-cell align-middle"})[1].div.div.p
            print(f"{count} - {trendler.text} - {kategori.text}")
            count += 1
            
diziler = Diziler()

while True:
    secim = input("1-Haftanın trend dizileri\n2-Haftanın trend filmleri\n3-Haftanın trend kullanıcıları\n4-Tüm zamanların trendleri\n5-Çıkış\nSeçiminiz: ")
    
    if secim == '5':
        break
    elif secim == '1':
        diziler.haftanintrendDizileri()
    elif secim == '2':
        diziler.haftanintrendFilmleri()
    elif secim == '3':
        diziler.haftanintrendKullanicilari()
    elif secim == '4':
        diziler.tumzamanlarıntrendleri()
    else:
        print("yanlış seçim")
    

        










