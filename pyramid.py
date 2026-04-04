# Pyramid using for loop
i = 0
for i in range(1,6):
    print("*" * i)


# Pyramid using while loop
i = 0
num = 5
while i <= num:
    print("*" * i)
    i += 1
    

# Pyramid using while loop user input 
i = 0
num = int(input("Enter Number :"))
while i <= num:
    print("*" * i)
    i += 1
    
    
# Number Pyramid 
i = 1
num = int(input("Enter Number :"))
for i in range(1, num + 1):
    for j in range(1, i+1):
        print(j, end="" *i)
    print("\n")
