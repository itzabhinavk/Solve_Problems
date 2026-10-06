# Day 2 - 100 Days of Code Challenge
# Yeh file aapki daily coding journey ka hissa hai.
# Motivation: Har din chhota sa step leke bada result pao.
# Chhoti chhoti steps bhi bade sapne banati hain.

import random
randnum = random.randint(0, 12)
guess=int(input("guess the number between 0 to 12: "))
if randnum==guess:
    print("you win")
else:
    print("you are wrong bro ")
    print("The randomly generated number was  " + str(randnum))
