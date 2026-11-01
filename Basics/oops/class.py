class Car:
    total_car=0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car+=1
        
    def get_brand(self):
        return self.__brand + "!"
    
    def get_model(self):
        return self.__model + "!"
        
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of Transport"
    
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.__battery_size = battery_size
        
    def get_battery_size(self):
        return self.__battery_size + "!"
    
    def fuel_type(self):
        return "Electrical Charge"
        
my_car = Car("Tata", "Safari")
print(my_car.get_brand(), my_car.get_model(), my_car.full_name(), my_car.fuel_type())

my_electric_car = ElectricCar("Tesla", "Model S", "50kWh")
print(my_electric_car.get_brand(), my_electric_car.get_model(), my_electric_car.get_battery_size(), my_electric_car.full_name(), my_electric_car.fuel_type())

print(isinstance(my_electric_car, Car))
print(isinstance(my_electric_car, ElectricCar))

print(Car.total_car)
# print(my_car.general_description())
print(Car.general_description())

print(my_car.model)


class Battery:
    def battery_info(self):
        return "this is a battery"
    
class Engine:
    def engine_info(self):
        return "this is an engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model T")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())