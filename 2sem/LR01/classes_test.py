class Calc():

    def __init__(self) -> None:
        self.values = []
    
    def calculate(self, val=-1) -> None:
        self.values.append(val + 1)

    def get_info(self) -> list:
        self.calculate()
        for i in self.values:
            print(i)
        return self.values

class Rec():
    
    def __init__(self, obj) -> None:
        self.data = []
        self.obj = obj
    
    def get_data(self) -> None:
        self.data = self.obj.get_info()
        

a = Calc()
b = Rec(a)


b.get_data()