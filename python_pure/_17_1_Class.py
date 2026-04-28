class Araba:
    """
    Araba Field
    """
    marka = "marka yazılmadı"
    model = "model yazılmadı"
    yil = 0
    renk = "renk yazılmadı"

    # self: Python'da bir metot içinde o an ki nesneye erişmek istiyorsak
    def calistir(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Yıl: {self.yil}, Renk: {self.renk}")
        #print("Marka:" + self.marka + "Model:" + {self.model} + "Yıl:" + {self.yil} + "Renk:" + {self.renk})


# field'siz
araba_ornegi1 = Araba()
araba_ornegi1.calistir()
print()

# field'lı
araba_ornegi2 = Araba()
araba_ornegi2.renk = "Siyah"
araba_ornegi2.yil = 2025
araba_ornegi2.marka = "Audi"
araba_ornegi2.model = "A3"
araba_ornegi2.calistir()


