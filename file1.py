class Cars(object):
    def __init__(self,fabrication_year,color,fuel_capacity,size):
      self.fabrication_year = fabrication_year 
      self.color = color
      self.fuel_capacity = fuel_capacity
      self.size = size

    def startCar(self):
        print("the car just started to move")
    
    def stopCar(self):
        print("the car just stopped moving")
Whitecar1=Cars(2021,"white","100ml","1m^3")
print(Whitecar1.fuel_capacity)
print(Whitecar1.startCar())