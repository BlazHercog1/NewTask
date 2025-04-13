def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def power(a, b):
    return pow(a, b)

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

if __name__ == "__main__":
    while True:
        print("Success")
