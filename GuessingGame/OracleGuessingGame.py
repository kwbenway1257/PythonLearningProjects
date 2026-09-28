###PLAY THE HIGH-LOW GAME###

import random

#Intro Text
print("""You awake with a metallic taste in your mouth, 
your vision returning slowly as you blink away duplicates.  
A figure in red flowing robes stands before you.  Their hand is 
already outstretched and offering to you a message.  
It reads simply: \n""")
print("Guess...")
print("The...")
print("NUMBER.")
input("Press Enter to continue...")
#Establish a valid guessing range
upper_bound = int(input("Enter a number to act as an upper boundary: \n"))
print("Hooded Figure: \"Not what I would've chosen, but alright.\"")
lower_bound = int(input("Enter a number to act as a lower boundary: \n"))

#loop until player picks valid range
while upper_bound <= lower_bound + 1:
    print("Hooded Figure: \"God, you really suck at this.  Upper boundary must be at least two integers greater than lower boundary, genius\"")
    upper_bound = int(input("Enter a number to act as an upper boundary: \n"))
    print("Hooded Figure: \"Not what I would've chosen, but alright.\"")
    lower_bound = int(input("Enter a number to act as a lower boundary: \n"))
print("Hooded Figure: \"I guess that'll do\"")    
input("Press Enter to continue...\n")

#Establish target number
target_num = random.randint(lower_bound + 1, upper_bound - 1)
print("""The message burns away and the figure 
chants in a foreign tongue, establishing...something...before 
turning back to you, as if in wait...\n""")

#Guessing Game Begins
guess_num = int(input("Hooded Figure: \"Hazard a guess\"\n"))
guess_count = 0
while guess_num != target_num:
    while guess_num not in range(lower_bound + 1, upper_bound):
        print("Invalid Guess: entry is stupid and you should try again...\n")
        guess_num = int(input("Hooded Figure: \"Hazard a guess\"\n"))
    guess_count += 1

    if guess_num < target_num:
        print("Hooded Figure: \"You're far beneath the oracle's prophetic integer.  Once more...\"")
    elif guess_num > target_num:
        print("Hooded Figure: \"You believe yourself to be above the oracle.  Pathetic.  Once more...\"")
    guess_num = int(input("Hooded Figure: \"Hazard a guess\"\n"))
guess_count += 1

#handle single or plural guess count
if guess_count == 1:
    print("The Hooded Figure kneels...\n")
    print()
    print("Hooded Figure: \"Chosen One, my life is yours, as your coming was written by the oracle before my birth.  Take from me all and leave with me nothing...\"")
elif guess_count > 1:
    print(f"Hooded Figure: \"If you are not chosen, then you are not welcome.  Only a heretic would take...{guess_count} attempts to cite the prophetic integer\"")     
    print()
    print("""The Hooded Figure uncloaks, revealing an almagamation of twisting, writhing organisms that begin 
    to grow and pulsate.  They double and then triple as he stumbles toward you, emitting an inhuman yelp.  
    The mass of intertwined creatures tower over above and before you can think of escape, they're enclosing you, 
    cutting you off from the outside word.  You hear the chants of many deep, echoing voices as you draw a final breath...""")       

               
