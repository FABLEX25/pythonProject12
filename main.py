from tkinter import *
def zadacha1():
    class Restaurant:
        def __init__(self,restaurant_name):
            self.restaurant_name = restaurant_name
        def describe_restaurant(self):
            print("Название ресторана: ",self.restaurant_name)
    class IceCreamStand(Restaurant):
        def __init__(self,restaurant_name,flavors):
            super().__init__(restaurant_name)
            self.flavors = flavors
        def vivod_sortov(self):
            print("Сорта мороженного: ")
            print(self.flavors)
    newIceCreamStand = IceCreamStand("Кафе-мороженное",["Ванильное", "Шоколадное","Фисташковое","Клубничное"])
    newIceCreamStand.describe_restaurant()
    newIceCreamStand.vivod_sortov()


def zadacha2():
    class Restaurant:
        def __init__(self,restaurant_name):
            self.restaurant_name = restaurant_name
        def describe_restaurant(self):
            print("Название ресторана: ",self.restaurant_name)
    class IceCreamStand(Restaurant):
        def __init__(self,restaurant_name,adress,vremya_raboti):
            self.restaurant_name = restaurant_name
            self.flavors = []
            self.adress = adress
            self.vremya_raboti = vremya_raboti
        def opisanie(self):
            print("Местоположение: ", self.adress,"\nВремя работы: ", self.vremya_raboti)
        def vivod_sortov(self):
            print("Вкусы мороженного: ")
            for flavor in self.flavors:
                print(f"-{flavor}")
        def add_flovor(self,flavor):
            self.flavors.append(flavor)
            print(f"{flavor} добавлено!")
        def remove_flavor(self,flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"{flavor} удалено!")
            else:
                print(f"{flavor} - такого вкуса нет в списке!")
        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f"{flavor} имеется в списке вкусов.")
            else:
                print(f"{flavor} Не имеется в списке вкусов.")
    newIceCreamStand = IceCreamStand("Кафе-мороженное","Ул.Большая Морская 20", "Пн-Пт с 8:00 до 21:00")
    newIceCreamStand.describe_restaurant()
    newIceCreamStand.opisanie()
    newIceCreamStand.vivod_sortov()
    newIceCreamStand.add_flovor("Ванильное")
    newIceCreamStand.add_flovor("Шоколадное")
    newIceCreamStand.add_flovor(input("Какое ещё добавить? "))
    newIceCreamStand.vivod_sortov()
    newIceCreamStand.remove_flavor(input("Какое удалить? "))
    newIceCreamStand.vivod_sortov()
    newIceCreamStand.check_flavor(input("Какое мороженное проверить в наличии? "))
def zadacha3():
    class Restaurant:
        def __init__(self,restaurant_name):
            self.restaurant_name = restaurant_name
        def describe_restaurant(self):
            print("Название ресторана: ",self.restaurant_name)
    class IceCreamStand(Restaurant):
        def __init__(self,restaurant_name,adress,vremya_raboti):
            self.restaurant_name = restaurant_name
            self.flavors = []
            self.adress = adress
            self.vremya_raboti = vremya_raboti
        def opisanie(self):
            print("Местоположение: ", self.adress,"\nВремя работы: ", self.vremya_raboti)
        def vivod_sortov(self):
            print("Вкусы мороженного: ")
            for flavor in self.flavors:
                print(f"-{flavor}")
        def add_flovor(self,flavor):
            self.flavors.append(flavor)
            print(f"{flavor} добавлено!")
        def remove_flavor(self,flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"{flavor} удалено!")
            else:
                print(f"{flavor} - такого вкуса нет в списке!")
        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f"{flavor} имеется в списке вкусов.")
            else:
                print(f"{flavor} Не имеется в списке вкусов.")
    class Palochka(IceCreamStand):
        def __init__(self, restaurant_name, adress, vremya_raboti):
            self.restaurant_name = restaurant_name
            self.flavors = []
            self.adress = adress
            self.vremya_raboti = vremya_raboti
            self.type = "Мороженное на палочке"
        def describe_type(self):
            print(f"Вид: {self.type}")
    class Rozhok(IceCreamStand):
        def __init__(self, restaurant_name, adress, vremya_raboti):
            self.restaurant_name = restaurant_name
            self.flavors = []
            self.adress = adress
            self.vremya_raboti = vremya_raboti
            self.type = "Мороженное в рожке"
        def describe_type(self):
            print(f"Вид: {self.type}")

    newIceCreamStand = IceCreamStand("Кафе-мороженное","Большая Морская 20", "Пн-Пт с 8:00 до 21:00")
    newIceCreamStand.describe_restaurant()
    newIceCreamStand.opisanie()
    newIceCreamStand = Palochka("", "", "")
    new2IceCreamStand = Rozhok("", "","")

    newIceCreamStand.add_flovor("Ванильное")
    newIceCreamStand.add_flovor("Шоколадное")

    new2IceCreamStand.add_flovor("Ягодное")
    new2IceCreamStand.add_flovor("Пломбир")

    newIceCreamStand.describe_type()
    newIceCreamStand.vivod_sortov()

    new2IceCreamStand.describe_type()
    new2IceCreamStand.vivod_sortov()

def zadacha4():
    class IceCreamStand:
        def __init__(self, flavors):
            self.flavors = ["Ванильное", "Шоколадное", "Фисташковое", "Клубничное"]
        def vivod_sortov(self):
            window = Tk()
            window.title("Доступные вкусы: ")
            window.geometry("500x250")
            p = 1
            for i in self.flavors:
                l = Label(window, text=i, font=("Arial", 20))
                l.grid(row=p)
                p += 1
            window.mainloop()
    newIceCreamStand = IceCreamStand(["Ванильное", "Шоколадное", "Фисташковое", "Клубничное"])
    newIceCreamStand.vivod_sortov()
zadacha4()
