class Numbers:

    def __init__(self, value):
        self.value = value
        
    def ChkPrime(self):
        if self.value <= 1:
            return False
        for i in range(2, int(self.value ** 0.5) + 1):
            if self.value % i == 0:
                return False
        return True
    
    def Factors(self):
        factor_list = []
        for i in range(1, self.value):
            if self.value % i == 0:
                factor_list.append(i)
        return factor_list

    def SumFactors(self):
        return sum(self.Factors())
    
    def ChkPerfect(self):
        return self.SumFactors() == self.value
    
numbers = [6,11,28]
objects = [Numbers(num) for num in numbers]
for obj in objects:
    
    print(f"Number Is Prime? : {obj.ChkPrime()}")
    
    #complete_factors = obj.Factors() + [obj]

    print(f"Factors :  {obj.Factors() + [obj]}")
    print(f"Sum of Proper Factors: {obj.SumFactors()}")
    print(f"Number is Perfect? : {obj.ChkPerfect()}")