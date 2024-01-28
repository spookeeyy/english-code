from time import sleep
from random import randint

lives = 10
coins = 0
win_amount = 150
danger = False

print("Forest Adventures.       -a story game by spooky")

name = input("Enter your name: ").strip()
if name == "":
    name = "FireInTheHole"

print()
print("There was a man named " + name + """ who was just exploring around his town, and he stumbled upon a forest. Maybe he's paranoid of this place? He decided to go and explore the forest.

Upon entering the forest, he found a poisonous mushroom. He didn't know that it was poisonous, but hunger got the best of him, so he decided to eat it. (He lost 1 life)

He kept on walking, randomly damaging himself. Then he found a bear who was friendly enough to spare him 5 gold coins.

He kept on exploring the forest, but he heard branches crack behind him. He decided to check his left and right, and his shoulder one more time. He thought, "Maybe I'm a schizophrenic; I be fearing for my life." After checking, there was no one. Maybe he really is a schizophrenic. Then he decided to check one last time, and there was an angry bear behind him, which damaged him. (He lost 1 life)

After that, he keeps on walking. (What did you expect, bruh?) He keeps randomly damaging himself. (Which took 2 of his lives)""")
print()
print("You are the man in the story. You have 10 lives.")
print("Press enter each time to advance into the story.")
print("Type 'exit' or 'quit' to exit the game.")
print()

while lives > 0:
    print("You walked into the forest and saw ", end="")
    who_what = randint(1, 4)
    
    if danger:
        print("danger, and lost two lives.")
        lives -= 2
        danger = False
        print("You have " + str(lives) + " lives left.")
    
    elif who_what == 1:
        print("a mushroom", end="")
        if randint(1, 3) == 1:
           print(" which unfortunately was poisonous, you lost one life.")
           lives -= 1
           print("You have " + str(lives) + " lives left.")
        else:
           print(" which was an edible mushroom and got a coin from selling it.")
           coins += 1
    
    elif who_what == 2:
        print("a bear", end="")
        if randint(1, 3) == 1:
           print(" who was unfortunately angry and lost one life.")
           lives -= 1
           print("You have " + str(lives) + " lives left.")
        else:
           print(" who was happy and gave you 5 coins.")
           coins += 5
    
    elif who_what == 3:
        print("a gold coin, and you got it.")
        coins += 1
       
    else:
        print("a treasure chest, and found 10 coins there.")
        coins += 10
    
    if coins >= win_amount:
        # win
        print("He collected " + str(coins) + " and found his way out of the forest, luckily surviving. You won the game!")
        break
    
    if randint(1, 10) == 1:
        print("You are in danger!")
        danger = True
    
    if randint(1, 15) == 1:
        if danger:
            danger = False
        print("You found a golden apple, you gained two lives and are protected from any danger!")
        print("You have " + str(lives) + " lives left.")
    
    print("You now have " + str(coins) + " gold coins.")

    text = input("> ")
    if text == "quit":
        lives = 0

if coins < win_amount:
    # lose
    print("""He died.
His body was later found by a passerby in the forest, he was killed by either a bear or by eating mushrooms or getting randomly damaged - we don't know.
But what we do know, is that you lost the game lol.""")

print()
input("Press enter to exit the game.")