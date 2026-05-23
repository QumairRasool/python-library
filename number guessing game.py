import random

b = input("welcome to the number guessing game, do you want to play? (yes/no) ")

if b == "yes" or b == "Yes" or b == "y" or b == "Y":
    while b == "yes" or b == "Yes" or b == "y" or b == "Y":
        a = random.randint(1, 100)
        x = -1                       
        c = 0
        while x != a: 
                        
            x = int(input("enter a number "))
            if x == a:
                print("you have guessed the number!")
            elif x < a:
                print("you have guessed a smaller number than the random number")
            elif x > a:
                print("you have guessed a larger number than the random number")
            c += 1

        print("you guessed the number in {} attempts!".format(c))
        b = input("do you want to play again? (yes/no) ")  
else:
    print("Okay, maybe next time!")