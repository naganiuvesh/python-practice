# Positional Argument 
def add(a, b):
    print("first =", a)
    print("second =", b)
    return a + b

a = int(input("Enter first value :"))
b = int(input("Enter second value :"))
print("sum =", add(a, b))

# --- Student Info 
def S_info(name, roll, mark):
    print("Name :", name)
    print("Roll NO. :", roll)
    print("Marks :", mark)

S_info("uvesh", 4, 99)

# --- Simple Intrest
def S_intrest(p, r, t):
    return (p * r * t) / 100

print("Simple Intrest =", S_intrest(10000, 6, 2))
print("Simple Intrest =", S_intrest(120000, 8.1, 1))

# --- Area of Circle
def ar_circle(r):
    pi = 3.14 * r * r
    print(f"Area of Circle : {pi:.2f}")

ar_circle(90)
ar_circle(15)

# --- Check number position nagative or zero
def check_value(no):
    if(no > 0):
        print("Positive")
    elif(no < 0):
        print("Nagative")
    else:
        print("ZERO")

check_value(0)
check_value(90)
check_value(-15)

# --- ODD & EVEN
def odd_even(no):
    if(no % 2==0):
        print(f"value {no} is even")
    else:
        print(f"value {no} is odd")
        
odd_even(50)
odd_even(15)

# --- Arithmetic operation substraction
# --- Multiplication and division
    
def addition(a,b):
    add = a + b 
    print("addition of two values",add)
    
addition(50,10.5)
addition(100,200)
   

