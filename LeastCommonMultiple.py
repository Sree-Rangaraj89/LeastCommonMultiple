a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

number1 = a
number2 = b

while b:
    c = b
    b = a % b 
    a = c

hcf = a
lcm = (number1 * number2) // hcf

print("LCM is:", lcm)
