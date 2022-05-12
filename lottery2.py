from asyncio.windows_events import NULL
import random
lotteryList=[]
ll=0
l=0
z=0
availableLotterylist=[]
boughtlist=[[],]
playerlist=[]
winner=random.randint(100,1000)
for i in range(100,1000):
    lotteryList.append(i)
    availableLotterylist.append(i)
print("Welcome \nThis is a lottery game \nTest your luck here\nBetter be luckey\nHere are the lottery numbers offered:\n",lotteryList)
numberOfPlayers=int(input("This game can be played by atmost 10 players\nEnter the number of players :"))
while(True):
    if(numberOfPlayers<1 or numberOfPlayers>10):
        print("Enter valid number\n")
        numberOfPlayers=int(input("This game can be played by atmost 10 players\n Enter the number of players(1-10) :"))
    else:
        break
for zz in range(0,numberOfPlayers):
    playerlist.append(f"player {zz}")
while(z<numberOfPlayers):
    boughtlist[z]=[]
    print(f"It's player {z+1}'s turn:")
    numberOfTickets=int(input("Enter the number of tickets you want to buy (you can buy upto 15 tickets) :"))
    if (numberOfTickets<16 and numberOfTickets>0):
        for j in range(0,numberOfTickets):
            if (j==0):
                while(True):
                    numberentered=int(input("Enter the number you want to choose and press 'Enter': "))
                    if numberentered in availableLotterylist:
                        #if(z==0):
                        boughtlist.append(NULL)
                        boughtlist[z].append(numberentered)
                        break
                    else:
                        print("Enter number from available ticket numbers")
                        while(True):
                            showList=int(input("Enter '1' to show available Ticket numbers and '0' to continue:"))
                            if(showList==1):
                                print(availableLotterylist)
                                break
                            elif(showList<0 or showList>1):
                                print("Please enter valid choise")
                            else:
                                break
                        continue
            else:
                while(True):
                    numberentered=int(input("Enter the next number you want to choose and press 'Enter': "))
                    if numberentered in availableLotterylist:
                        #if(z==0):
                        boughtlist.append(NULL)
                        boughtlist[z].append(numberentered)
                        break
                    else:
                        print("Enter number from available ticket numbers")
                        while(True):
                            showList=int(input("Enter '1' to show available Ticket numbers and '0' to continue:"))
                            if(showList==1):
                                print(availableLotterylist)
                                break
                            elif(showList<0 or showList>1):
                                print("Please enter valid choise")
                            else:
                                break
                        continue
            availableLotterylist.remove(boughtlist[z][j])
            while(True):
                showList=int(input("Enter '1' to show available Ticket numbers and '0' to continue:"))
                if(showList==1):
                    print(availableLotterylist)
                    break
                elif(showList<0 or showList>1):
                    print("Please enter valid choise")
                else:
                    break
        print(f"Player {z+1} bought {boughtlist[z]} tickets")
        for k in range (0,len(boughtlist[z])):
            if(boughtlist[z][k]==winner):
                print(f"******Hurray!!******\nYou are lucky {winner} is the winner of this contest")
                print(f"As lottery ticket is picked once player {z+1} wins the Game\nThank you for playing")
                exit
            ll+=1
        if(ll>=len(boughtlist[z])):
            print(f"******Better luck next time******\n")
    else:
        print("You have entered wrong number Try re-Entering the number of tickets you wanna buy")
        continue
    z+=1
if(z>=numberOfPlayers):
    while(0 in boughtlist):
        boughtlist.remove(0)
    print(f"List of total ticket numbers bought:\n{boughtlist}")
    print(f"!!!!! Alas! no one was lucky enough to win\nThank you for playing\nBetter luck next time\n{winner} was the winning no")