###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
digits = "".join(str(x) for x in digits[:3])
print(digits)

# Another hint:
gameover = False

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
while not gameover:
    guess = input("What is your guess? ")
    if len(guess) != 3:
        print("Wrong input, three digits expected")
        continue
    correct_input = True
    for chr in guess:
        if not chr in "0123456789":
            correct_input = False
    if not correct_input:
        print("Wrong input, only digits accepted")
        continue
    if guess == digits:
        print("You won! Computer guessed {}".format(digits))
        gameover = True
        continue
    is_nope = True
    for chr in guess:
        if chr in digits:
            is_nope = False
    if is_nope:
        print("Nope")
        continue
    is_match = False
    for i, chr in enumerate(guess):
        if chr == digits[i]:
            is_match = True
    if is_match:
        print("Match")
        continue
    print("Close")
