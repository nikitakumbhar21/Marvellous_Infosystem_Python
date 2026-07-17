class Arithmetic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
        
    def Accept(self):
        self.value1 = int(input("Enter first number: "))
        self.value2 = int(input("Enter second number: "))

    def Addition(self):
        Add = self.value1 + self.value2
        return Add
    
    def Substraction(self):
        Sub = self.value1 - self.value2
        return Sub

    def Multiplication(self):
        Mult = self.value1 * self.value2
        return Mult
    
    def Division(self):
        if self.value2 == 0:
            return "Error: Division by zero is not allowed"
        Div = self.value1 / self.value2
        return Div

obj1 = Arithmetic()
obj2 = Arithmetic()

print("\n--- Object 1 ---")
obj1.Accept()
print("Addition:", obj1.Addition())
print("Substraction:", obj1.Substraction())
print("Multiplication:", obj1.Multiplication())
print("Division:", obj1.Division())

print("\n--- Object 2 ---")
obj2.Accept()
print("Addition:", obj2.Addition())
print("Substraction:", obj2.Substraction())
print("Multiplication:", obj2.Multiplication())
print("Division:", obj2.Division())

