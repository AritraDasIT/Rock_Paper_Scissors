import random

USER_CHOICE=int(input("ENTER YOUR CHOICE: Enter-1 for ROCK || Enter-2 for PAPER || Enter-3 for SCISSOR : "))
print("USER CHOICE: ")
print(USER_CHOICE)

if(USER_CHOICE>=4 or USER_CHOICE<1):
    print("YOU ENTER INVALID NUMBER AND YOU LOSE")

else:
    COMPUTER_CHOICE=random.randint(1,3)
    print("The Computer choice: ")
    print(COMPUTER_CHOICE)

    if(COMPUTER_CHOICE==USER_CHOICE):
        print("IT IS A DRAW")
    elif(COMPUTER_CHOICE==1 and USER_CHOICE==3):
        print("YOU LOSE")
    elif(USER_CHOICE==1 and COMPUTER_CHOICE==3):
        print("YOU WIN")
    elif(COMPUTER_CHOICE>USER_CHOICE):
        print("YOU LOSE")
    elif(USER_CHOICE>COMPUTER_CHOICE):
        print("YOU WIN ")


