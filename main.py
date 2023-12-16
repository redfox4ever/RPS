import random as random
def convert_response(x):
    if x == 1 :
        return "rock"
    elif x == 2:
        return "paper"
    elif x == 3:
        return "scissors"

options = {
"rock" : ["scissors","paper"],
"paper" : ["rock","scissors"],
"scissors" : ["paper","rock"],
}
x,y = 0,0
rounds = 3
while x <= rounds/2 and y <= rounds/2:
    print("You: ",x," : ",y," :Bot")
    print("Choose 1,2 or 3\n","1)rock","2)paper","3)scissors",sep="\n")
    player_response = int(input("\n"))
    if player_response in {1,2,3} :
        player_response = convert_response(player_response)
    else:
        while True :
            print("Choose again",sep="\n")
            player_response = int(input("\n"))
            if player_response in {1,2,3} :
                break
        player_response = convert_response(player_response)
    bot_response = convert_response(random.randrange(1,4))
    
    print("You chose :",player_response,"\ncomputer chooses ",bot_response,end="\n\n")
    if player_response == bot_response :
        print("the round is a draw ",end="\n\n")
    elif options[player_response][0] == bot_response:
        print("you win the round!",end="\n\n")
        x+=1
    else:
        print("the bot wins the round!",end="\n\n")
        y+=1    
if x > y :
    print("you won against the bot")
else:
    print("you lost against the bot")
