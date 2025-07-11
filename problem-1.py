class Calc:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
    def operate(self, operation):
        if operation == 'add':
            return self.a + self.b
        elif operation == 'sub':
            return self.a - self.b
        elif operation == 'mul':
            return self.a * self.b
        elif operation == 'div':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Cannot divide by zero!"
        else:
            return "Invalid operation."
a = input("enter 1st n.o:")
b = input("enter 2nd n.o:")
operation = input("enter operations(add/sub/mul/div):")
calc = Calc(a,b)
print("Result:", calc.operate(operation))