from abc import ABC, abstractmethod
import math


class Student:
    def get_data(self):
        name = input("Enter your name: ")
        rollNo = int(input("Enter your rollNo: "))
        print("Marks out of 100")
        m1 = int(input("Enter marks of subject 1: "))
        m2 = int(input("Enter marks of subject 2: "))
        m3 = int(input("Enter marks of subject 3: "))

        self.name = name
        self.rollNo = rollNo
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def display_data(self):
        print(
            f"Name: {self.name}\nRollNo: {self.rollNo}\nMarks in subject1:{self.m1}\nMarks in subject2:{self.m2}\nMarks in subject3:{self.m3}"
        )

    def calculate_percentage(self):
        total = self.m1 + self.m2 + self.m3
        per = total / 300
        print(f"Your Percentage is: {per:.2f}%")


class Account:
    def __init__(self, accHolderName, accNumber, balance):
        self.accHolderName = accHolderName
        self.accNumber = accNumber
        self.balance = balance

    def deposit(self):
        amt = float(input("Enter the amount to deposit: "))
        if amt < 0:
            print("can not have negative value.")
            return
        self.balance += amt
        print(
            f"{amt} deposited successfully, your current balance is {self.balance:.2f}"
        )

    def withdraw(self):
        amt = float(input("Enter the amount to withdraw: "))
        if amt > self.balance:
            print("Insufficient Balance")
            return
        self.balance -= amt
        print(f"{amt} withdrawn successfully")
        print(f"your current balance is {self.balance}")

    def displayBalance(self):
        print(f"Your current balance is: {self.balance:.2f}")



class Employee:

    def __init__(self, empID, name, basicSalary):
        self.empID = empID
        self.name = name
        self.basicSalary = basicSalary

    def CalcHRA(self):
        return 0.2 * self.basicSalary

    def CalcDA(self):
        return 0.1 * self.basicSalary

    def GrossSalary(self):
        grossSal = self.CalcDA() + self.CalcHRA() + self.basicSalary
        return grossSal




class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"Area of the Rectangel is: {self.length*self.breadth}")

    def perimeter(self):
        print(f"Perimeter of the Rectangle is {2*(self.length+self.breadth)}")

    def checkSquare(self):
        if self.length != self.breadth:
            return
        print("Rectangle is a Square.")


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}\nModel: {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, fuelType):
        super().__init__(brand, model)
        self.fuelType = fuelType

    def display(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nFuel Type: {self.fuelType}")


class Bike(Vehicle):
    def __init__(self, brand, model, engineClass):
        super().__init__(brand, model)
        self.engineClass = engineClass

    def display(self):
        print(
            f"Brand: {self.brand}\nModel: {self.model}\nEngine Class: {self.engineClass}"
        )



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


class Principal(Teacher):
    def __init__(self, name, age, subject, schoolName):
        super().__init__(name, age, subject)
        self.schoolName = schoolName

    def display(self):
        print(f"{self.name}, {self.age}, {self.subject}, {self.schoolName}")




class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius * self.radius
        print(f"area of the circle is : {area:.2f}")


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print(f"Area of the Square is: {self.side*self.side}")


class Triangle(Shape):
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def area(self):
        s = (self.s1 + self.s2 + self.s3) / 2
        area = math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))

        print(f"Area of the triangle is: {area:.2f}")