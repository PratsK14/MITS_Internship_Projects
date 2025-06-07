import re
print("WELCOME")
a = input("\n ")

def add(a, b):
    print(f"Adding {a} + {b} = {a + b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b} = {a - b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b} = {a * b}")
    return a * b

def divide(a, b):
    if b == 0:
        print("Division by zero error")
        return None
    print(f"Dividing {a} / {b} = {a / b}")
    return a / b

operation_map = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def evaluate_expression(s):
    # Extract numbers and symbols in order
    tokens = re.findall(r'\d+|[+\-*/]', s)
    
    # Convert first number to int
    result = int(tokens[0])
    
    # Loop through remaining tokens
    i = 1
    while i < len(tokens) - 1:
        op = tokens[i]
        num = int(tokens[i + 1])
        func = operation_map.get(op)
        if func:
            result = func(result, num)
        else:
            print(f"Ignoring unsupported operator: {op}")
        i += 2
    
    return result



