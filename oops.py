'''class Bank_Account:
	customer_name = ""
	balance = 0
	account_number = 0

Alzam = Bank_Account()
Alzam.customer_name = "Alzam Ahamed"    
Alzam.account_number = 123456
Alzam.balance = 1111111111



print(Alzam.customer_name)
print(Alzam.account_number) 
print(Alzam.balance)

class car:
    def __init__(self):
        print("This is a constructor!")
        self.no_of_wheels = 4
        self.mileage = 10
        self.no_of_airbags = 2

    def moveforwards(self):
        print("The car is moving forward")

    def movebackwards(self):
        print("The car is moving backwards")

car1 = car() #Insantiation
print(car1.mileage)

car2 = car()
print("Mileage:", car2.mileage)
car2.mileage = 25.0
print("Mileage:", car2.mileage)
print(car1.mileage)

car3 = car()
car3.moveforwards()'''

class Car:
    def __init__(aself, no_of_wheels, no_of_airbags, mileage):
        print("This is a constructor!")
        aself.no_of_wheels = no_of_wheels
        aself.no_of_airbags = no_of_airbags
        aself.mileage = mileage

    def moveforwards(self, speed):
        print(f"The {self.no_of_wheels}-wheeled car is moving forward at", speed, "km/h")

    def movebackwards(self):
        print("The car is moving backward")

car1 = Car(4, 2, 10)
print(car1.mileage, car1.no_of_airbags, car1.no_of_wheels)


car2 = Car(7, 4, 15)
car2.moveforwards(60)
print(car2.mileage, car2.no_of_airbags, car2.no_of_wheels)


car3 = Car(8, 6, 20)    
car3.movebackwards()
print(car3.mileage, car3.no_of_airbags, car3.no_of_wheels)