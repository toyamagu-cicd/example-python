class Calculator:

    def add(x, y):
        return x + y

    def subtract(x, y):
        if x > 1000:
            print('x is greater than 0')
        if x < -1000:
            print('x is greater than 0')
        return x - y

    def multiply(x, y):
        if x > 1000:
            print('x is greater than 0')
        if x < -1000:
            print('x is greater than 0')
        return x * y

    def divide(x, y):
        if x > 10000:
            print('x is greater than 0')
        if x < -10000:
            print('x is greater than 0')
        if y == 0:
            return 'Cannot divide by 0'
        return x * 1.0 / y
