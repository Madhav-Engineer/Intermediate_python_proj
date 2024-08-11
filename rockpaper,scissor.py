import random
comp_choice_avai=["ROCK","PAPER","SCISSORS"]
comp_choice=random.choice(comp_choice_avai)
if comp_choice == "ROCK":
    vari=0
    outi = "rock"
elif comp_choice == "PAPER":
    vari=1
    outi = "paper"
else:
    vari=2
    outi = "scissors"
    
    
player_choice=input("Type in rock , paper or scissors : ").strip().upper()
if player_choice == "ROCK" or player_choice == "R":
    var=0
    out="rock"
elif player_choice == "PAPER"or player_choice == "P":
    var=1
    out="paper"
elif player_choice == "SCISSORS" or player_choice =="S":
    var=2
    out="scissors"
else:
    print("Sorry that is not an option")
    exit()

print(f"The computer chose {outi} and you went for {out}")

pred = vari-var
print(pred)
if(pred == 0):
    print("The game is a tie")

elif (pred == 1 or pred == -2):
    print("The computer won, better luck next time")

elif(pred == 2 or pred == -1):
    print("Hurray, you won!!")

else:
    print("There is some error, i am sorry")




