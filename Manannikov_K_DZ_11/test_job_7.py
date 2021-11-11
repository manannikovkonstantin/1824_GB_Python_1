class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма c1 и c2 равна:')
        return f'C = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение c1 на c2 равно:')
        return f'C = {self.a * other.a - (self.b * other.b)} + {(self.a * other.b) + (self.b * other.a)} * i'


c_1 = ComplexNumber(1, -2)
c_2 = ComplexNumber(3, 4)

print(c_1 + c_2)
print(c_1 * c_2)