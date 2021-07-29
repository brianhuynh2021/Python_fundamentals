#unittesting
def add(x, y):
    return x+y

def subtract(x, y):
    """Subtract Function"""
    return x -y

def multiply(x, y):
    """Multiply Function"""
    return x*y

def divide(x, y):
    """Divide Function"""
    try:
        return x/y
    except:
        y == 0
        return f'Error with y equal to 0'
print(add(3,5))
print(subtract(3,5))
print(multiply(3,5))
print(divide(3,0))
