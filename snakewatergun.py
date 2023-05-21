import random
print("""1.Snake 
2.Water 
3.Gun""")
userin = int(input("Enter the following option in 1 2 3: \n"))
comp = random.randint(1, 3)

def check(comp, userin):
    if(comp == userin):
        return 0
    if comp ==  2 and userin == 1:
        return -1
    if comp == 3 and userin == 1:
        return -1
    if comp == 2 and userin == 3:
        return -1
    elif comp == 2 and userin == 1:
        return 1
    else:
        return 1

print("You", userin)
print("computer", comp)    

score = check(comp, userin)
if (score == 0):
    print("It's a draw")
elif(score == -1):
    print("You lose")
elif(score == 1):
    print("You win")
else:
    print("You won")