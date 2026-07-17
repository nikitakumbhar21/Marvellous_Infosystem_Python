class Demo:
    value1 = 51
    value2 = 101

    def __init__(self):
        self.no1 = no1
        self.no2 = no2
        
    def Fun(self):
        print("Display values of instance variables from Fun():")
        print(self.no1)
        print(self.no2)

    def Gun(self):
        print("Display values of instance variables from Gun():")
        print(self.no1)
        print(self.no2)

obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()
