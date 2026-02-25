# Quest 28: The Adventure Begins (Absurd Life Edition)
# Author : @gunnogere
# 25th February 2026


def end_game(previous_function):
    print("\nWhat would you like to do?")
    print("1. Choose a different option from here")
    print("2. Restart the whole game")
    print("3. Exit")

    choice = input("Enter 1, 2 or 3: ")

    if choice == "1":
        previous_function()
    elif choice == "2":
        start()
    elif choice == "3":
        print("\nThanks for playing! 🎮")
    else:
        print("Invalid choice.")
        end_game(previous_function)


def start():
    print("\n=== Quest 28: The Adventure Begins - Group 4 ===") 
    print("\nWelcome to Life Simulator.")
    print("In this life, you are either:")
    print("1. Woman")
    print("2. Man")
    
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\n🕊️ You live a peaceful life.")
        print("✅ Safe. End Game.")
        end_game(start)
    elif choice == "2":
        man_path()
    else:
        print("Invalid choice.")
        start()


def man_path():
    print("\n👨 You are a man.")
    print("Choose your career path:")
    print("1. Government")
    print("2. Military")
    
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\n🏢 You work safely in a government office.")
        print("✅ Safe. End Game.")
        end_game(man_path)
    elif choice == "2":
        military_path()
    else:
        print("Invalid choice.")
        man_path()


def military_path():
    print("\n🎖️ You joined the military.")
    print("Where are you stationed?")
    print("1. War Front")
    print("2. HQ Bunker")
    
    choice = input("Enter 1 or 2: ")

    if choice == "2":
        print("\n🛡️ You stay in the HQ bunker.")
        print("✅ Safe. End Game.")
        end_game(military_path)
    elif choice == "1":
        war_front()
    else:
        print("Invalid choice.")
        military_path()


def war_front():
    print("\n⚔️ You are at the war front.")
    print("What happens?")
    print("1. You survive the battle")
    print("2. You fall in battle")
    
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\n🏆 You survive the battle.")
        print("✅ Safe. End Game.")
        end_game(war_front)
    elif choice == "2":
        afterlife()
    else:
        print("Invalid choice.")
        war_front()


def afterlife():
    print("\n☠️ You were defeated in battle.")
    print("Where are you laid to rest?")
    print("1. Back Home")
    print("2. In the Forest")
    
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\n🏡 You are remembered peacefully back home.")
        print("✅ Safe. End Game.")
        end_game(afterlife)
    elif choice == "2":
        forest_cycle()
    else:
        print("Invalid choice.")
        afterlife()


def forest_cycle():
    print("\n🌲 Nature takes its course.")
    print("The forest thrives.")
    print("What product is made from the harvested tree?")
    print("1. Books")
    print("2. Tissue Paper")
    
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\n📚 You become part of knowledge and stories.")
        print("✅ Safe. End Game.")
        end_game(forest_cycle)
    elif choice == "2":
        tissue_path()
    else:
        print("Invalid choice.")
        forest_cycle()


def tissue_path():
    print("\n🧻 You become soft tissue paper.")
    print("Who uses it?")
    print("1. A Man")
    print("2. A Woman")
    
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\n🙂 Routine day. Nothing dramatic.")
        print("✅ Safe. End Game.")
        end_game(tissue_path)
    elif choice == "2":
        final_choice()
    else:
        print("Invalid choice.")
        tissue_path()


def final_choice():
    print("\n⚠️ Final twist of fate.")
    print("1. Used from the back")
    print("2. Used from the front")
    
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\n😌 Peaceful conclusion.")
        print("✅ Safe. End Game.")
        end_game(final_choice)
    elif choice == "2":
        print("\n💀 Destiny had other plans.")
        print("You Died. Game Over.") 
    else:
        print("Invalid choice.")
        final_choice()

# Start the game
start()