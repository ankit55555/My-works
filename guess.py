import random as r
num=r.randrange(100)
guess=5

while guess>=0:
    ur_guess=int(input("enter the guess:"))

    def check(x):
        if ur_guess == x:
            print("You win")
        elif ur_guess > x:
            print("keep lower:")
        else :
            print("keep higher:")

    if guess>1:
        check(num)
    elif guess==1:
        check(num)
        print(" you have last chance left")
    else:
        print("you lost")
    guess=guess-1
