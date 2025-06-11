
from CarCustormerclass import *
rented_cars=[]
class Car :
    def __init__(self,model,rent_per_day):
        self.model = model
        self.rent_per_day = rent_per_day
        self.available=True
