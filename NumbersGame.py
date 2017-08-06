import random
number = random.randint(1,15)
print "you have to enter the number to start this amazing game."
input = int(raw_input("Enter a number of your choice : "))
if input < number :
    print " you loose because your number is less "
elif user == number :
    print "You won."
elif user > number :
    print "you loose becauseYour number is high. "