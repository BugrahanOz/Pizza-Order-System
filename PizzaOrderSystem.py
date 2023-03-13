import csv
import datetime

class Pizza:
    def __init__(self):
        self.description = "Bilinmeyen pizza"
        self.cost = 0.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class KlasikPizza(Pizza):
    def __init__(self):
        self.description = "Klasik pizza"
        self.cost = 20.0

class MargheritaPizza(Pizza):
    def __init__(self):
        self.description = "Margarita pizza"
        self.cost = 22.0

class TurkPizza(Pizza):
    def __init__(self):
        self.description = "Türk pizza"
        self.cost = 25.0

class SadePizza(Pizza):
    def __init__(self):
        self.description = "Sade pizza"
        self.cost = 18.0

class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)

class Zeytin(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Zeytin sos"
        self.cost = 2.0

class Mantarlar(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Mantar sos"
        self.cost = 3.0

class KeciPeyniri(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Keçi peyniri sos"
        self.cost = 4.0

class Et(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Et sos"
        self.cost = 5.0

class Sogan(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Soğan sos"
        self.cost = 1.0

class Misir(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Mısır sos"
        self.cost = 2.0

menu_file = open("Menu.txt", "r")
menu = menu_file.read()
print(menu)
pizza_choice = input("Pizza seçiniz: ")
sos_choice = input("Sos seçiniz: ")
pizza = None

#Pizza Seçimi
if pizza_choice == "1":
    pizza = KlasikPizza()
elif pizza_choice == "2":
    pizza = MargheritaPizza()
elif pizza_choice == "3":
    pizza = TurkPizza()
elif pizza_choice == "4":
    pizza = SadePizza()
else:
    print("Geçersiz pizza seçimi")

#Sos Seçimi
if sos_choice == "11":
    pizza = Zeytin(pizza)
elif sos_choice == "12":
    pizza = Mantarlar(pizza)
elif sos_choice == "13":
    pizza = KeciPeyniri(pizza)
elif sos_choice == "14":
    pizza = Et(pizza)
elif sos_choice == "15":
    pizza = Sogan(pizza)
elif sos_choice == "16":
    pizza = Misir(pizza)

#Toplam Fiyatı alma
total=pizza.get_cost()

 # Müşteri bilgilerini alma
name = input("Lütfen adınızı giriniz: ")
id_number = input("Lütfen TC kimlik numaranızı giriniz: ")
credit_card_number = input("Lütfen kredi kartı numaranızı giriniz: ")
credit_card_password = input("Lütfen kredi kartı şifrenizi giriniz: ")

# Sipariş verilerini kaydetme
order_time = datetime.datetime.now()
with open("Orders_Database.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow([pizza.get_description()] +
                    [name, id_number, credit_card_number,credit_card_password, order_time, total])

print("Siparişiniz başarıyla alındı. Toplam tutar: ", total)
