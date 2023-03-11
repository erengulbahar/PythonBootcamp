import csv
import datetime

#Klasik pizza sınıfımız
class Klasik_Pizza:
    def get_description(self):
        return "Klasik pizzamız tam 50 yıldır aşkla üretilip tüketiliyor!\nİçerisinde mantar, sosis ve sucuk bulunmaktadır.\nHamuru incedir."

    def get_cost(self):
        return 25

#Margarita pizza sınıfımız
class Margarita_Pizza:
    def get_description(self):
        return "En kıymetli pizzalarımızdan bir tanesi!\nİçerisinde mantar, sucuk ve domates bulunmaktadır.\nHamuru orta kalınlıktadır."

    def get_cost(self):
        return 30

#Türk pizzası sınıfımız
class Turk_Pizza:
    def get_description(self):
        return "Efsaneler efsanesi pizza türümüz: TÜRK PİZZASI!\nİçerisinde mantar, sosis, sucuk ve domates bulunmaktadır.\nHamuru orta kalınlıktadır."

    def get_cost(self):
        return 35

#Sade pizza sınıfımız
class Sade_Pizza:
    def get_description(self):
        return "Damak lezzetini bilenler için en uygunu budur! İçerisinde mantar ve sosis bulunmaktadır.\nHamuru incedir."

    def get_cost(self):
        return 30

class Pizza(Klasik_Pizza, Margarita_Pizza, Turk_Pizza, Sade_Pizza):
    def __init__(self, pizza_tabani):
        self.pizza_tabani = pizza_tabani

    #Burada her bir pizza için belirlenmiş olan fiyatları Decorator sınıfı için geri döndürüyoruz
    def get_cost(self):
        if (self.pizza_tabani == 1):
            return 2.0*Klasik_Pizza().get_cost()

        elif (self.pizza_tabani == 2):
            return 2.5*Margarita_Pizza().get_cost()

        elif (self.pizza_tabani == 3):
            return 3.0*Turk_Pizza().get_cost()

        elif (self.pizza_tabani == 4):
            return 2.5*Sade_Pizza().get_cost()

        else:
            return "Lütfen geçerli bir pizza tabanı seçin!"

    #Burada her bir pizza için belirlenmiş olan açıklamaları Decorator sınıfı için geri döndürüyoruz
    def get_description(self):
        if (self.pizza_tabani == 1):
            return Klasik_Pizza().get_description()

        elif (self.pizza_tabani == 2):
            return Margarita_Pizza().get_description()

        elif (self.pizza_tabani == 3):
            return Turk_Pizza().get_description()

        elif (self.pizza_tabani == 4):
            return Sade_Pizza().get_description()

class Decorator(Pizza):
    def __init__(self, sos, pizza_tabani):
        super().__init__(pizza_tabani)
        self.sos = sos
    
    def get_cost(self):
        if(self.sos == 1 and self.pizza_tabani == 1):
            return 1.5*Pizza(1).get_cost()

        elif(self.sos == 2 and self.pizza_tabani == 1):
            return 2.0*Pizza(1).get_cost()

        elif (self.sos == 3 and self.pizza_tabani == 1):
            return 3.0 * Pizza(1).get_cost()

        elif (self.sos == 4 and self.pizza_tabani == 1):
            return 3.0 * Pizza(1).get_cost()

        elif (self.sos == 5 and self.pizza_tabani == 1):
            return 2.0 * Pizza(1).get_cost()

        elif (self.sos == 6 and self.pizza_tabani == 1):
            return 2.0 * Pizza(1).get_cost()

        elif (self.sos == 1 and self.pizza_tabani == 2):
            return 1.5 * Pizza(2).get_cost()

        elif (self.sos == 2 and self.pizza_tabani == 2):
            return 2.0 * Pizza(2).get_cost()

        elif (self.sos == 3 and self.pizza_tabani == 2):
            return 3.0 * Pizza(2).get_cost()

        elif (self.sos == 4 and self.pizza_tabani == 2):
            return 3.0 * Pizza(2).get_cost()

        elif (self.sos == 5 and self.pizza_tabani == 2):
            return 2.0 * Pizza(2).get_cost()

        elif (self.sos == 6 and self.pizza_tabani == 2):
            return 2.0 * Pizza(2).get_cost()

        elif (self.sos == 1 and self.pizza_tabani == 3):
            return 1.5 * Pizza(3).get_cost()

        elif (self.sos == 2 and self.pizza_tabani == 3):
            return 2.0 * Pizza(3).get_cost()

        elif (self.sos == 3 and self.pizza_tabani == 3):
            return 3.0 * Pizza(3).get_cost()

        elif (self.sos == 4 and self.pizza_tabani == 3):
            return 3.0 * Pizza(3).get_cost()

        elif (self.sos == 5 and self.pizza_tabani == 3):
            return 2.0 * Pizza(3).get_cost()

        elif (self.sos == 6 and self.pizza_tabani == 3):
            return 2.0 * Pizza(3).get_cost()

        elif (self.sos == 1 and self.pizza_tabani == 4):
            return 1.5 * Pizza(4).get_cost()

        elif (self.sos == 2 and self.pizza_tabani == 4):
            return 2.0 * Pizza(4).get_cost()

        elif (self.sos == 3 and self.pizza_tabani == 4):
            return 3.0 * Pizza(4).get_cost()

        elif (self.sos == 4 and self.pizza_tabani == 4):
            return 3.0 * Pizza(4).get_cost()

        elif (self.sos == 5 and self.pizza_tabani == 4):
            return 2.0 * Pizza(4).get_cost()

        elif (self.sos == 6 and self.pizza_tabani == 4):
            return 2.0 * Pizza(4).get_cost()

        else:
            return "Lütfen geçerli bir pizza sosu seçin!"

    def get_description(self):
        if (self.sos == 1 and self.pizza_tabani == 1):
            return "Zeytin sosu" + " ve " +  Pizza(1).get_description()

        elif (self.sos == 2 and self.pizza_tabani == 1):
            return "Mantar sosu" + " ve " +  Pizza(1).get_description()

        elif (self.sos == 3 and self.pizza_tabani == 1):
            return "Keçi peyniri sosu" + " ve " +  Pizza(1).get_description()

        elif (self.sos == 4 and self.pizza_tabani == 1):
            return "Et sosu" + " ve " +  Pizza(1).get_description()

        elif (self.sos == 5 and self.pizza_tabani == 1):
            return "Soğan sosu" + " ve " +  Pizza(1).get_description()

        elif (self.sos == 6 and self.pizza_tabani == 1):
            return "Mısır sosu" + " ve " +  Pizza(1).get_description()

        elif (self.sos == 1 and self.pizza_tabani == 2):
            return "Zeytin sosu" + " ve " +  Pizza(2).get_description()

        elif (self.sos == 2 and self.pizza_tabani == 2):
            return "Mantar sosu" + " ve " +  Pizza(2).get_description()

        elif (self.sos == 3 and self.pizza_tabani == 2):
            return "Keçi peyniri sosu" + " ve " +  Pizza(2).get_description()

        elif (self.sos == 4 and self.pizza_tabani == 2):
            return "Et sosu" + " ve " +  Pizza(2).get_description()

        elif (self.sos == 5 and self.pizza_tabani == 2):
            return "Soğan sosu" + " ve " +  Pizza(2).get_description()

        elif (self.sos == 6 and self.pizza_tabani == 2):
            return "Mısır sosu" + " ve " +  Pizza(2).get_description()

        elif (self.sos == 1 and self.pizza_tabani == 3):
            return "Zeytin sosu" + " ve " +  Pizza(3).get_description()

        elif (self.sos == 2 and self.pizza_tabani == 3):
            return "Mantar sosu" + " ve " +  Pizza(3).get_description()

        elif (self.sos == 3 and self.pizza_tabani == 3):
            return "Keçi peyniri sosu" + " ve " +  Pizza(3).get_description()

        elif (self.sos == 4 and self.pizza_tabani == 3):
            return "Et sosu" + " ve " +  Pizza(3).get_description()

        elif (self.sos == 5 and self.pizza_tabani == 3):
            return "Soğan sosu" + " ve " +  Pizza(3).get_description()

        elif (self.sos == 6 and self.pizza_tabani == 3):
            return "Mısır sosu" + " ve " +  Pizza(3).get_description()

        elif (self.sos == 1 and self.pizza_tabani == 4):
            return "Zeytin sosu" + " ve " +  Pizza(4).get_description()

        elif (self.sos == 2 and self.pizza_tabani == 4):
            return "Mantar sosu" + " ve " +  Pizza(4).get_description()

        elif (self.sos == 3 and self.pizza_tabani == 4):
            return "Keçi peyniri sosu" + " ve " +  Pizza(4).get_description()

        elif (self.sos == 4 and self.pizza_tabani == 4):
            return "Et sosu" + " ve " +  Pizza(4).get_description()

        elif (self.sos == 5 and self.pizza_tabani == 4):
            return "Soğan sosu" + " ve " +  Pizza(4).get_description()

        elif (self.sos == 6 and self.pizza_tabani == 4):
            return "Mısır sosu" + " ve " +  Pizza(4).get_description()

with open("Menu.txt", "r", encoding="utf-8") as file:
    menu_text = file.read()

print(menu_text + "\n")

pizza_turu = int(input("Pizza Tabanı: "))
pizza_sosu = int(input("Pizza Sosu: "))

decorator_object = Decorator(pizza_sosu, pizza_turu)

print("\nPizza açıklaması: " + decorator_object.get_description() + "\n" + "\nFiyat: " + str(decorator_object.get_cost()) + " TL")