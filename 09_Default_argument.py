# Default Argument 
# 1. 
def greet (name = "Guest") :
    print("Hello", name)
    
greet("Alice")
greet()

# 2. 
def add (a, b = 5) :
    print("Sum :", a + b)

add(10, 20)
add(10)

# 3. 
def sqr(num, exp = 2):
    return num ** exp
print(sqr(3))
print(sqr(3, 3))
print(sqr(3, 4))
