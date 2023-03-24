'''
    1.The __init__ method is the Python equivalent of the C++ constructor in an object-oriented approach.
    2.The __init__ function is called every time an object is created from a class.
    3.The __init__ method lets the class initialize the object's attributes and serves no other purpose.
    4.It is only used within classes.
'''

class Mobile:
#class is created.

    def __init__(self, Brand, battery, ram, camera, price):
    #Constructor ( __init__() method ) task is to assign values to the data members of the class.
        #__init__() method will initialize the variables by using self.

        self.Brand=Brand
        self.battery=battery
        self.ram=ram
        self.camera=camera
        self.price=price
        #self is used to access variables that belongs to the class.
        
    def display(self):
        print("Brand: ",self.Brand,
              "Battery:",self.battery,
              "Ram:",self.ram,
              "Camera:",self.camera,
              "Price:",self.price)
        print(end=" \n ")
        #printing variables simple rytt.
        
        
for i in range(2):
#This is completely optional, if u want to print results as many times use for() loop.

    #inside the for() loop So it will print as range(2) specified
    
    obj=Mobile("Infinix\n","5000mAh\n","4gb\n","13mp\n",7000)
    #object created for class and arguments also passed as per mentioned in __init__() method.
    
    obj.display()
    #calling a function
    

obj1=Mobile("Redmi\n","6000mAh\n","6gb\n","16mp\n",9000)
obj1.display()
obj2=Mobile("RealMe\n","7000mAh\n","8gb\n","48mp\n",11000)
obj2.display()
#Multiple objects created for Single Class and
#Those are outside the loop So, prints one time only
