import random
user_input=input("Enter a choice: (rock,paper,scissors)")
possible_actions=["rock","paper","scissors"]
computer_action= random.choice(possible_actions)
#print user actions and computer actions
if user_input==computer_action:
    print("Its a tie try agian")
elif user_input=="rock":
    if computer_action=="scissors":
        print("you win!")
    else:
        print("you lose")
elif user_input=="paper":
    if computer_action=="rock":
        print("you win!")
    else:
        print("you lose!")
elif user_input=="scissors":
    if computer_action=="rock":
        print("you lose!") 
    else:
        print("you win!")               
    