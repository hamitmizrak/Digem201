# Class
class ArabaConstructor:
    def __init__(self,marka="Bilinmiyor",model="bilinmiyor",yil=0,renk="bilinmiyor"):
        self.marka=marka
        self.model=model
        self.yil=yil
        self.renk=renk
        print("Araba için yeni bir sınıf oluşturdum")

    # Function name
    def bilgileri_goster(self):
        print(f"Marka: {self.marka}  model:{self.model} yıl:{self.yil} renk:{self.renk}")


    # SETTER AND GETTER
    def set_marka(self,marka):
        self.marka=marka

    def get_marka(self):
        return self.marka

    def set_model(self,model):
        self.model=model

    def get_model(self):
        return self.model


    def set_yil(self,yil):
        if yil>=2020:
            self.yil=yil
        else:
            print("2020 yılının altında olan arabalar alınmıyor")

    def get_yil(self):
        return self.yil


    def set_renk(self,renk):
        self.renk=renk

    def get_renk(self):
        return self.renk

# instance
araba_ornegi1=ArabaConstructor()
araba_ornegi1.bilgileri_goster()
print()


# instance
araba_ornegi2=ArabaConstructor()
araba_ornegi2.set_renk("Beyaz")
araba_ornegi2.set_marka("Audi")
araba_ornegi2.set_model("Q serisi")
#araba_ornegi2.set_yil(2022)
araba_ornegi2.set_yil(2015)
araba_ornegi2.bilgileri_goster()