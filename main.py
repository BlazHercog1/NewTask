def add(a, b):
    return a + b

def power(a, b):
    return pow(a, b)

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Uporaba: python main.py <operacija> <a> <b>")
        print("Operacije: add, power, divide")
        sys.exit(1)

    operacija = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])

    if operacija == "add":
        print(add(a, b))
    elif operacija == "power":
        print(power(a, b))
    elif operacija == "divide":
        print(divide(a, b))
    else:
        print("Neznana operacija")
        sys.exit(1)
