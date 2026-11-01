import os
os.system('cls')


# begin
"""def check_password(password):
    if len(password)<8:
        raise ValueError("password should be more 8 symbols")
    elif " " in password:
        raise ValueError("password not should has space")
    elif not any(char.isdigit() for char in password):
            raise ValueError("password should has at least one digit")
    return "password was created!"
try:
    answer = check_password(input())
    print(answer)
except ValueError as er:
     print(F"{er}")"""""


"""my_list = [10,20,30];print(my_list)
index_user = input("input index element that you want take: ")
try:
    print(my_list[int(index_user)])
except IndexError:
    print("This index not exists")
except ValueError:
    print("index can't be letter")"""



"""def withdraw(balance,amount):
    if balance<amount:
        raise ValueError("amount more than balance")
    elif amount<=0:
        raise ValueError("amount for withdrawal should be more zero")
    else:
        return balance-amount

try:
    money_user = withdraw(int(input("input balance: ")),int(input("input amount for withdrawal: ")))
except ValueError as e:
    print(e)
else:
    print(f"all good, your remains {money_user}")
finally:
    print("thanks that use our ATM")"""



"""class Students:
    university = "ITMO"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"Student study in {self.university}, he is {self.age} years old and his name {self.name}")

    @classmethod
    def change_university(cls,new_name):
        cls.university = new_name
        print(f"Unviversity changed to {new_name}")

    def check_adult(self):
        return self.age>=18
    
Students.change_university("MGY")
student1 = Students("Ivan",22)
student2 = Students("VIKA",17)
student1.show_info()
print(student1.check_adult())"""

"""class BankAccount:

    def __init__(self):
        self.__balance = 0
    def deposit(self,amount):
        if amount>0:
            self.__balance +=amount
            print(f"Your account was replenished by {amount},you have {self.__balance}")
    def get_balance(self):
        return self.__balance

client1 = BankAccount()
client1.deposit(100)
client1.deposit(200)
print(client1.get_balance())
print(client1._balance)"""


"""class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        print(f"Vector: {self.x} , {self.y}")
    def __eq__(self,other):
        if isinstance(other,Vector):
            return self.x==other.x and self.y == other.y
        return False
vector1 = Vector(10,2)
vector2 = Vector(2,10)
vector3 = Vector(10,2)
vector1.__str__()
print(Vector.__eq__(vector1,vector2))
print(Vector.__eq__(vector1,vector3))"""

"""class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = False
    def read(self):
        self.is_read = True
    def info(self):
        return f"{self.title} - {self.author},{self.pages} pages, Read - {self.is_read}"
    def __str__(self):
        return self.info()
book1 = Book("War and peace","L.N.Tolstoy",320)
book2 = Book("Evgeniy Onegin","A.S.Pushkin",220)
book1.read()
print(book1)
print(book2.info())"""


"""class Shape:
    def area(self):
        raise NotImplementedError
    def perimeter(self):
        raise NotImplementedError
    def __str__(self):
        return f"is shape {self.__class__.__name__}, perimeter = {self.perimeter()},area = {self.area()}"
from math import pi
class Circle(Shape):
    def __init__(self,radius):
        if radius <=0:
            raise ValueError("Radius should be more zero")
        self.radius = radius      
    def area(self):
        return pi * (self.radius**2)
    def perimeter(self):
        return 2 * pi * self.radius
class Rectangle(Shape):
    def __init__(self,width,height):
        if width<=0 or height <=0:
            raise ValueError("widht and height should be more zero")
        self.width = width
        self.height = height
    def area(self):
        return self.height*self.width
    def perimeter(self):
        return 2 * (self.width + self.height)
shapes = [
    Circle(5),
    Rectangle(3, 4),
    Rectangle(10, 2),
]
for shape in shapes:
    print(shape)"""


"""class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y )
    def __sub__(self,other):
        if not isinstance(other,Vector2D):
            return NotImplemented
        return Vector2D(self.x - other.x , self.y - other.y)
    def __mul__(self,number):
        if not isinstance(number, (int , float)):
            return NotImplemented
        return Vector2D(self.x * number,self.y * number)
    def __rmul__(self,number):
        return self * number
    def __eq__(self,other):
        if not isinstance(other,Vector2D):
            return NotImplemented
        return (self.x == other.x and self.y == other.y)
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)

print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(2 * v1)
print(abs(v1))
print(v1 == Vector2D(1, 2))"""

"""class Money:
    def __init__(self,amount,currency):
        self.amount = amount
        self.currency = currency
    @property
    def currency(self):
        return self._currency
    @currency.setter
    def currency(self,currency_user):
        if not self.is_valid_currency(currency_user):
            raise ValueError("incorrect input! currecncy should have 3 uppercase letters")
        self._currency = currency_user
    @staticmethod
    def is_valid_currency(currency_user):
        return (isinstance(currency_user , str )) and (len(currency_user) == 3) and (currency_user.isupper())
    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"
    def __str__(self):
        return f"{self.amount} {self.currency}"
    def __eq__(self,other):
        if not isinstance(other , Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency
    def __add__(self,other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("This values different")
        return Money(self.amount + other.amount , self.currency)
    def __sub__(self,other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("This values different")
        return Money(self.amount - other.amount, self.currency)
    def __mul__(self,factor):
        if not isinstance(factor , (int,float)):
            return NotImplemented
        return Money(self.amount * factor , self.currency)
    def __len__(self):
        return len(str(int(abs(self.amount))))
    @classmethod
    def from_string(cls,amount_AND_currency_user):
        amount , currency = amount_AND_currency_user.split()
        return cls(float(amount) , currency )
    
m1 = Money(100, "RUB")
m2 = Money(50, "RUB")
m3 = Money(100, "USD")

print(repr(m1))          # Money(100, 'RUB')
print(str(m1))           # 100 RUB
print(m1 == Money(100, "RUB"))  # True
print(m1 == m3)          # False
print((m1 + m2))         # 150 RUB
print((m1 - m2))         # 50 RUB
print((m1 * 2))          # 200 RUB
print(len(Money(1234.5, "RUB")))  # 4

# 1. Проверка @property и @staticmethod
try:
    m = Money(100, "rub")  # маленькие буквы
except ValueError as e:
    print("Ошибка поймана:", e) # Ошибка поймана: Неверный формат валюты

# 2. Проверка @classmethod
m1 = Money.from_string("250 USD")
print(repr(m1)) # Money(250, 'USD') (или Money(250.0, 'USD'))
print(m1 + Money(50, "USD")) # 300 USD

m2 = Money(10, "EUR")
print(m1 == m2) # False
"""
"""from abc import abstractmethod, ABC 

class Employee(ABC):
    
    def __init__(self , name , base_salary):
        self.name = name
        self.base_salary = base_salary
    @abstractmethod
    def calculate_salary(self):
        pass
    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.calculate_salary()}"

class Manager(Employee):
    def __init__(self, name , base_salary , bonus):
        super().__init__(name , base_salary)
        
        self.bonus = bonus
    def calculate_salary(self):
        return self.base_salary + self.bonus

class Developer(Employee):
    def __init__(self , name , base_salary , language):
        super().__init__(name , base_salary)
        self.language = language
    def calculate_salary(self):
        if self.language == "Python":
            return self.base_salary * 1.5
        return self.base_salary
try:
    ob1 = Employee("Ivan" , 50_000)
except TypeError as e:
    print(f"Error : {e}")
maneger1 = Manager("Petya", 70_000, 2_000)
developer1 = Developer("Misha", 100_000 , "Python")
developer2 = Developer("Sasha", 80_000 , "Java")

print(maneger1)
print(developer1)
print(developer2)
Employees = [maneger1 , developer1 , developer2]

total_salary = 0
for emp in Employees:
    print(emp)
    total_salary += emp.calculate_salary()
print(total_salary)"""

"""class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def __str__(self):
        return f"Brand - {self.brand}"

class Car(Vehicle):
    def __init__(self , brand , wheels):
        super().__init__(brand)
        self.wheels = wheels
    def __str__(self):
        return f"{super().__str__()}, quantity wheels - {self.wheels}"

class ElectricCar(Car):
    def __init__(self, brand , wheels , battery_capacity):
        super().__init__(brand , wheels)
        self.battery_capacity = battery_capacity
    def __str__(self):
        return f"{super().__str__()}, battery capacity - {self.battery_capacity}"

car_1 = ElectricCar("Tesla", 4, 100)
print(car_1)"""

"""class LogMixin:
    def log(self , message):
        print(f"[LOG]: {message}")

class User:
    def __init__(self, name , email):
        self.name = name
        self.email = email

class AdminUser(User , LogMixin):
    def ban_user(self, target_user_name):
        self.log(f"User {target_user_name} was banned by {self.name}")

admin = AdminUser("Ivan", "ivan@mail.ru")
admin.ban_user("Petr")"""

"""from dataclasses import dataclass

@dataclass
class Product:
    name : str
    _price : float

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self , value):
        if value < 0:
            raise ValueError("We can't change your balance , because amount should be more zero ")
        self._price = value

    @property
    def price_with_tax(self):
        return self._price * 1.2

# Проверка
p = Product("Ноутбук", 1000)
print(p) # Автоматически сгенерированный dataclass __repr__: Product(name='Ноутбук', _price=1000)
print(f"Цена с налогом: {p.price_with_tax}") # 1200.0

try:
    p.price = -50
except ValueError as e:
    print("Ошибка:", e)""" # Ошибка: Цена не может быть отрицательной!

"""from dataclasses import dataclass

@dataclass
class UserProfile:
    username : str
    _age : int
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self , value ):
        if value < 0 or value > 150:
            raise ValueError("Unacceptable age!")
        self._age = value
    @property
    def is_adult(self):
        return self._age >= 18"""

"""from dataclasses import dataclass

@dataclass
class PlayerStats:
    name : str
    _health : int = 100
    _mana : int = 50

    @property
    def health(self):
        return self._health
    @health.setter
    def health(self , value):
        if value < 0 or value > 100:
            raise ValueError("Meaning should be greater than zero and less than 100")
        self._health = value

    @property
    def mana(self):
        return self._mana
    @mana.setter
    def mana(self , value):
        if value < 0 or value > 100:
            raise ValueError("Meaning should be greater than zero and less than 100")
        self._mana = value

    @property
    def is_alive(self):
        return self._health > 0

    def __post_init__(self):
        if self._health < 0 or self._health > 100:
            raise ValueError("Health should be between 0 and 100")
        if self._mana < 0 or self._mana > 100:
            raise ValueError("Mana hould be between 0 and 100")"""


"""class Duck:
    def quack(self):
        return f"kria-kria"

class Person:
    def quack(self):
        return f"I am a human , but i quacking!"
def make_it_quack(duck_like_object):
    print(duck_like_object.quack())

d = Duck()
p = Person()

make_it_quack(d) # Кря-кря!
make_it_quack(p)""" # Я человек, но крякаю!

"""class Car:
    __slots__ = ('brand', 'model')

    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
    def __str__(self):
        return f"brand - {self.brand} , model - {self.model}"
    
my_car = Car("Toyota", "Camry")
print(my_car)
try:
    my_car.color = "red"
except Exception as e:
    print(f"Error : {e}")"""

class Playlist:
    def __init__(self):
        self._songs = []
    def add_song(self , song):
        self._songs.append(song)
    def __len__(self):
        return len(self._songs)
    def __getitem__(self, index):
        return self._songs[index]
    def __iter__(self):
        return iter(self._songs)

# --- Проверка ---
my_music = Playlist()
my_music.add_song("Bohemian Rhapsody")
my_music.add_song("Hotel California")
my_music.add_song("Stairway to Heaven")

# Проверка __len__
print(f"Всего песен: {len(my_music)}") # Выведет: 3

# Проверка __getitem__
print(f"Вторая песня: {my_music[1]}") # Выведет: Hotel California

# Проверка __iter__
print("Список воспроизведения:")
for song in my_music:
    print(f" - {song}")

        