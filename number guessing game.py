import random

b = input("welcome to the number guessing game, do you want to play? (yes/no) ")

if b == "yes" or b == "Yes" or b == "y" or b == "Y":
    while b == "yes" or b == "Yes" or b == "y" or b == "Y":
        a = random.randint(1, 100)
        x = -1
        c = 0
        won = False                 

        while x != a:
            if c < 7:
                x = int(input("enter a number "))
                c += 1
                if x == a:
                    print("you have guessed the number!")
                    won = True      
                elif x < a:
                    print("you have guessed a smaller number than the random number")
                elif x > a:
                    print("you have guessed a larger number than the random number")
                if c >= 7 and x != a:
                    print(f"you have used all your attempts! the number was {a}")
                    break

        if won:                   
            print(f"you guessed the number in {c} attempts!")

        b = input("do you want to play again? (yes/no) ")

else:
    print("Okay, maybe next time!")