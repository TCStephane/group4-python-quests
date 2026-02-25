# Quest 29: The Code Breaker (Final Fun Version)
# Author : @gunnogere
# 25th February 2026

secret_code = 42
lives = 3
 
print("=== CODE BREAKER - Group 4  ===") 
print("INSTRUCTIONS:")
print("You have 3 lives (3 chances) to guess the secret code.")
print("Hint: The secret code is a 2-digit number.")
print("If you guess correctly, you win.")
print("If you lose all your lives, the game is over.\n")

while lives > 0:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)

        if guess == secret_code:
            print("\n BOOM! Access Granted! You cracked the code like a legend!")
            break
        else:
            lives -= 1 #decrement

            if lives > 0:
                print(f"\n You failed… but you almost nailed it!")
                print(f" {lives} live(s) remaining. Stay sharp!\n")
            else:
                print("\n You have exhausted all your lives.")
                print(" You Died. Game Over.")

    else:
        print("\n Invalid input. Please enter a valid number.\n")