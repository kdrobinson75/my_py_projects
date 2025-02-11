name = input("Hi, type your name: ")
print("Hello", name, "welcome to my game!")

should_we_play = input("Do you want to play? Enter (yes or no)").lower()

if should_we_play == "y" or should_we_play == "yes":
    print("Great! Let's play!")
    weapons = input("Select your weapon (axe/stick/hammer): ").lower()
    while weapons not in ["axe", "stick", "hammer"]:
        print("Sorry, invalid response! Try again!!")
        weapons = input("Select a valid weapon (axe/stick/hammer): ").lower()

    if weapons == "axe" or weapons == "hammer":
        print("Nice, you chose a great and mighty weapon!")
    elif weapons == "stick":
        print("Good Luck, you chose a stick as your weapon!")

    direction = input("Do you want to go left or right? Enter (left or right): ").lower()
    if direction == "left":
        print("Okay, you went left, and just fell off a cliff! GAME OVER! Try again...")
    elif direction == "right":
        choice = input("Okay, you went right, now you see a bridge. Do you want to swim under it or cross it? Enter (swim or cross): ").lower()
        if choice == "swim":
            print("Oops, you just spotted an alligator in the water. The alligator is very angry and hungry!")
            should_you_fight_or_flight = input("Enter (fight or swim away): ").lower()
            if (weapons == "axe" or weapons == "hammer") and should_you_fight_or_flight == "fight":
                print("Great! You slayed the alligator with your weapon!")
                next_move = input("Time to cross the bridge. Type (cross): ").lower()
                if next_move == "cross":
                    print("Congrats! You just won the simple game!")
                else:
                    print("Sorry, you were eaten by the alligator! Game Over...")
            else:
                print("Sorry, you were eaten by the alligator! Game Over...")
        elif choice == "cross":
            print("Congrats! You just won the simple game!")
        else:
            print("Sorry, not a valid response, you LOSE!!")
    else:
        print("Sorry, not a valid response, you LOSE!!")
else:
    print("Guess you're NOT playing...")