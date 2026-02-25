user_choice1=input("Choose a way to go: left or right? ")
if user_choice1=="left":
    print("You have chose left. Do you want to swim or wait?")
    user_choice2=input("Enter your choice: swim or wait? ")
    if user_choice2=="swim":
        print("You have chose to swim. Find the treasure chest.")
    elif user_choice2=="wait":
        print("You have chose to wait. A boat will come and take you to the island.")
    else:
        print("You have entered an invalid choice. Please try again.")
elif user_choice1=="right":
    print("You have chose right. Do you want to climb the mountain or go through the cave?")
    user_choice3=input("Enter your choice: climb or cave? ")
    if user_choice3=="climb":
        print("You have chose to climb. You will climb a mountain and find nothing.")
    elif user_choice3=="cave":
        print("You have chose to go through the cave. You will find a secret passage that leads to the treasure.")
    else:
        print("You have entered an invalid choice. Please try again.")
else:
    print("You have entered an invalid choice. Please try again.")

print("Congratulations! You have completed the quest and found the treasure!")