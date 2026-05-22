import random
a= random.randint(1,100)
#random number which will be generated will be stored in this variable
x=-1
while x!=a:
        x= int(input("enter a number "))
        if x==a:
            print ("you have guessed the number")
        elif x<a:
            print ("you have guessed a smaller number than the original number")
        elif x>a:
            print ("you have guessed a larger number than the original number")


print ("the end of program")