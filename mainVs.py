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


class Vector:
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
print(Vector.__eq__(vector1,vector3))