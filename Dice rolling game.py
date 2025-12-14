import random
print("wanna roll the dice Φ >>>")
while True:
    choice=input("select your choice(yes//No):")
    choice.lower()

    if choice=="yes" :
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(">>>>",end=" ")
        print("The result-->",(die1,die2),end=" ")
        print("<<<<<")
    if choice=="no" :
        print(".....Thank you....")
        break


else:
    print("...............")
    print("Invalid input")
    print("...............")

    
