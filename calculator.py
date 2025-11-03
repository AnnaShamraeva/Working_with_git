class Calculator: 

    def sum(self, a, b): # self указывает на то, что это методы класса
        return a+b
 
    def extract(self, a, b):
        # пример: разность a и b
        return self.sum(a, - b)

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b

    def __str__(self):
        return 'Hi, I am a calculator'