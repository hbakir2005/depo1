#Oyuncunun aynı anda 2 desteden kart çektiği ve aynı kartları çekene kadar hamlelere devam ettiği bir oyundur.Kartlar her çekmeden sonra tekrar desteye konur.En az hamlede aynı iki kartı çeken oyuncu oyunu kazanır. 
import random

kart_sayilari = tuple(range(2,11))
kart_türleri = ("As", "Joker", "Vale", "Papaz")
kart_simgeleri = ("Sinek", "Kupa", "Karo", "Maça")
deste1 = kart_sayilari+kart_türleri
deste2 = kart_sayilari+kart_türleri
while True:
    deste_cek1 = random.choice(deste1)
    simge_cek1 = random.choice(kart_simgeleri)
    deste_cek2 = random.choice(deste2)
    simge_cek2 = random.choice(kart_simgeleri)
    deste_cek1 = str(deste_cek1)
    deste_cek2 = str (deste_cek2)
    oyuncu1_kart =deste_cek1+simge_cek1
    oyuncu2_kart = deste_cek2 + simge_cek2
    print(oyuncu1_kart,oyuncu2_kart)

    if oyuncu1_kart==oyuncu2_kart:
        print("Kazandınız, Tebrikler. Oyun bitti")
        quit()

    else:
        print("Devam etmek için enter'a basınız.")

    input()


