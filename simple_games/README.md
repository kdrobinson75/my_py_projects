# Simple Game

Welcome to the Simple Game! This is a text-based adventure game where you make choices to navigate through the game and try to win.

## How to Play

1. **Start the Game**: Run the `simple_game.py` script.
2. **Enter Your Name**: You will be prompted to enter your name.
3. **Choose to Play**: Decide if you want to play the game by entering "yes" or "no".
4. **Select a Weapon**: Choose your weapon from the options: axe, stick, or hammer.
5. **Make Choices**: Navigate through the game by making choices such as going left or right, swimming or crossing a bridge, and fighting or fleeing from an alligator.

## Game Flow

1. **Introduction**: The game greets you and asks if you want to play.
2. **Weapon Selection**: You select a weapon. If you choose an invalid weapon, you will be prompted to choose again.
3. **Direction Choice**: You choose to go left or right.
   - If you go left, you fall off a cliff and the game ends.
   - If you go right, you encounter a bridge.
4. **Bridge Choice**: You choose to swim under the bridge or cross it.
   - If you choose to swim, you encounter an alligator.
     - If you have an axe or hammer and choose to fight, you slay the alligator and win the game.
     - If you choose to swim away or have a stick, you are eaten by the alligator and the game ends.
   - If you choose to cross the bridge, you win the game.

## Example

```sh
$ python simple_game.py
Hi, type your name: John
Hello John, welcome to my game!
Do you want to play? Enter (yes or no) yes
Great! Let's play!
Select your weapon (axe/stick/hammer): axe
Nice, you chose a great and mighty weapon!
Do you want to go left or right? Enter (left or right): right
Okay, you went right, now you see a bridge. Do you want to swim under it or cross it? Enter (swim or cross): cross
Congrats! You just won the simple game!