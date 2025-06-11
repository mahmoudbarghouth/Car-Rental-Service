
class CarCustomer:
    def __init__(self,name):
        self.name = name
        self.rentedcars=[]

rented_cars=[]
class Car :
    def __init__(self,model,rent_per_day):
        self.model = model
        self.rent_per_day = rent_per_day
        self.available=True

class RentService :
    def __init__(self):
        self.cars=[]
        self.carscustomers=[]
    def add_car(self,car):
        self.cars.append(car)
    def add_car_customer(self,carcustomer):
        self.carscustomers.append(carcustomer)
    def car_available(self,car,carcustomer):
        if car.available:
            print (f"car {car.model} is available and rented by {carcustomer.name}")
            rented_cars.append(car.model)
            carcustomer.rentedcars.append(car.model)
            car.available=False

        else:
            print("this car isn't available")
    def show_rented_cars(self):
        for car in rented_cars :
            print(car)
    def rental_cost(self,car,days):
        return car.rent_per_day*days

car1=Car("bmw",1000)
car2=Car("hd",300)
car3=Car("metsubishy",150)
customer1=CarCustomer("ahmed")
customer2=CarCustomer("ali")
customer3=CarCustomer("alex")

rental=RentService()
rental.car_available(car1,customer1)
print(f"the cost of {car1.model} for two days is {rental.rental_cost(car1,2)}. ")

rental.car_available(car1,customer2)
print(f"the cost of {car1.model} for two days is {rental.rental_cost(car1,2)}. ")
rental.car_available(car2,customer2)
print(f"the cost of {car2.model} for two days is {rental.rental_cost(car2,2)}. ")

rental.show_rented_cars()