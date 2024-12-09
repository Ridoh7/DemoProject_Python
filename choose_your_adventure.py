name= input("Type your name: ")
print("Welcome", name, "to this adventure, it is going to be fun")

answer= input(
    "You are on dirt road, it has come to an end and you can go left or right, which way will you like to go? ").lower()

if answer== "left":
    answer=input("You come to a river, you can walk around it or swim across? Type walk to walk around or swim to swim across: ").lower()
    
    if answer=="swim":
        print("You swim across and were eaten by aligator, you lose.")
    elif answer=="walk":
        print("You walked of many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer== "right": 
    answer=input("You come to a bridge, it looks wobbly, do you want to cross it or head back? Type (cross/back): ")

    if answer=="back":
        print("You go back to lose.")
    elif answer=="cross":
        answer= input("You crossed the bridge and meet a strangers, do you talk to them (yes/no)? ").lower()

        if answer== "yes":
            print("You talked to the strangers and gave you gold, you won!")
        elif answer=="no":
            print("You ignored the strangers and they are offended and you lose.")

        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for playing", name+".")