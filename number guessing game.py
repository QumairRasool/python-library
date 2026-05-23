import random
a= random.randint(1,100)
b=input("welcome to the number guessing game, do you want to play? (yes/no) ")
x=-1

if b=="yes" or b=="Yes" or b=="y" or b=="Y":
    while x!=a:
        x= int(input("enter a number "))
        if x==a:
            print ("you have guessed the number")
        elif x<a:
            print ("you have guessed a smaller number than the original number")
        elif x>a:
            print ("you have guessed a larger number than the original number")
else:
    print("Okay, maybe next time!")
