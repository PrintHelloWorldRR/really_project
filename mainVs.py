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
from abc import abstractmethod, ABC 

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
print(total_salary)