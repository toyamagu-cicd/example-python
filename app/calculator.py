class Calculator:

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        if x > 0:
            print 'okok'
        return x * y

    def divide(x, y):
        if y == 0:
            return 'Cannot divide by 0'
        return x * 1.0 / y
