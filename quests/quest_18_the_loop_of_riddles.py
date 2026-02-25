import random
b = int(input("Enter the range you want to guess(Highest number): "))
ans = random.randint(1, b)
guess = int(input(f"Guess the number I picked 1 - {b}\n"))
while guess != ans:
    print("Sorry wrong answer")
    guess = int(input(f"Guess the number I picked 1 - {b}\n"))
if guess == ans:
    print("Yes! correct")
