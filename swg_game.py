import random

def gamewin(Comps,you):
    if Comps==you:
        return None
    elif Comps=="s":
        if you=='w':
            return False
        elif you=='g':
            return True
    elif Comps=="w":
        if you=="g":
            return False
        elif you=="s":
            return True
    elif Comps=="g":
        if you=="s":
            return False
        elif you=="w":
            return True



print("Comps Turn:Snake(s) Water(w) Gun(g)?")
randno=random.randint(1,3)
if randno==1:
    Comps='s'
elif randno==2:
    Comps='w'
elif randno=='3':
    Comps='g'

you=input("Your turn: Snake(s) Water(w) Gun(g)")
a=gamewin(Comps,you)

print(f"Computer chose:{Comps}")
print(f"You Chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You win!")

else:
    print("You lose !hehe")