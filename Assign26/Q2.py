class Circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0
        self.area = 0
        self.circumference = 0
        
    def Accept(self):
        self.radius = int(input("Enter radius of circle: "))

    def CalculateArea(self):
        self.area = Circle.PI * (self.radius ** 2)
    
    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius

    def Display(self):
        print(f"Radius: {self.radius}")
        print(f"Area: {self.area}")
        print(f"Circumference: {self.circumference}\n")

obj1 = Circle()
obj2 = Circle()

obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()

