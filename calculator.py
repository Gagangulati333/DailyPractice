number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

print "press 1 for addition"
print "press 2 for subtraction"
print "press 3 for multiplication"
print "press 4 for division"
choice = raw_input("enter you choice")

if choice=="1":
    print(number1 + number2)
if choice=="2":
    print(number1 - number2)
if choice=="3":
    print(number1 * number2)
if choice=="4":
    print(number1 / number2)
