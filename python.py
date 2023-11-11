import random

yazi= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345"

uzunluk = int(input("uzunluk kaç olsun"))

sifre = ""

for i in range(uzunluk):
    random_karakter = random.choice(yazi)
    sifre+= random_karakter


print(sifre)
