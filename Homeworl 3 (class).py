import datetime


class Car:
    __id = 0
    __mark = ""
    __model = ""
    __year = 0
    __color = ""
    __price = 0
    __regnumber = 0
    def __init__(self, id0, mark0, model0, year0, color0, price0, regnumber0):
        self.__id = id0
        self.__mark = mark0
        self.__model = model0
        self.__year = year0
        self.__color = color0
        self.__price = price0
        self.__regnumber = regnumber0

    def get_id (self):
        return self.__id
    def get_mark (self):
        return self.__mark
    def get_model (self):
        return self.__model
    def get_year (self):
        return self.__year
    def get_color (self):
        return self.__color
    def get_price (self):
        return self.__price
    def get_regnumber (self):
        return self.__regnumber
    def age(self):
        return datetime.date.today().year - self.__year
    def __str__(self):
        return str(self.__mark) + " " + str(self.__model) + " " + str(self.__year)
newCars = [
    Car (0,"porsche", "cayenne", 2015, "black", 76500, 12345),
    Car (1,"bmw", "x5", 2020, "blue", 69400, 12345),
    Car (2,"bmw", "x3", 2017, "black", 55000, 12345),
    Car (3,"porsche", "911", 2018, "black", 120000, 12345),
    Car (4,"bmw", "790", 2019, "black", 32000, 12345),
    Car (5,"porsche", "macan", 2019, "black", 90000, 12345),
    Car (6,"lamborgini", "huracan", 2020, "yellow", 150000, 12345),
]
m=input("введите марку")
for car in newCars:
    if car.get_mark() == m:
        print(car)

model=input("введите модель")
age=int(input("введите возраст"))
for car in newCars:
    if car.get_model() == model and car.age()==age:
        print (car)










