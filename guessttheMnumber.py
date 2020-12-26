import random
print("="*42)
print("Welcome to the guess the M number minigame")
print("="*42)
myst = random.randint(1,100)
#print(myst)
guess_it=0
tries=0

while guess_it != myst and tries < 7:
    guess_it = input("please try guess: ")
    if guess_it > myst:
        print("it's bigger than")
    elif guess_it < myst:
        print ("it's smaller than")
    tries = tries + 1
if guess_it == myst:
    print("Congratulation, you've completed the guess the M. number mini game")
else:
    print("sorry, you didn't complet the guess the M. number mini game,try again")
    print("the number is ", myst)