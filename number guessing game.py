import random

b = input("welcome to the number guessing game, do you want to play? (yes/no) ")

if b == "yes" or b == "Yes" or b == "y" or b == "Y":
    while b == "yes" or b == "Yes" or b == "y" or b == "Y":
        a = random.randint(1, 100)
        x = -1                         # ← inside outer loop

        while x != a:                  # ← inside outer loop
            x = int(input("enter a number "))
            if x == a:
                print("you have guessed the number!")
            elif x < a:
                print("you have guessed a smaller number than the original number")
            elif x > a:
                print("you have guessed a larger number than the original number")

        b = input("do you want to play again? (yes/no) ")  # ← outside inner loop, inside outer loop

else:
    print("Okay, maybe next time!")