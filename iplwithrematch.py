import random
rm=1
while(rm==1):
    balloutcome=[0,1,2,3,4,5,6,'noball','out','wide','runout0','runout1','lbw','noball','out','wide','runout0','runout1','lbw'
    ,0,1,2,4,6,0,1,2,4,6,0,1,2,4,6,0,1,2,4,6,0,1,2,4,6,0,1,2,4,6,0,1,2,4,6,0,1,2,4,6,0,1,2,4,6,0,1,2,4,6,0,1,2,4,6,0,1,2,4,6,0
    ,1,2,4,6,0,1,2,4,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
    1,1,1,1,1,1,1,1,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]
    team1=['dummy','p1','p2','p3','p4','p5','p6','p7','p8b','p9b','p10b','p11b','extrpp1','extrpp2','extrpp3']
    team1ActualPlayers=team1[1:12]
    team2=['dummy','t2p1','t2p2','t2p3','t2p4','t2p5','t2p6','t2p7','t2p8b','t2p9b','t2p10b','t2p11b','t2extrp1','t2extrp2','t2extrpp3']
    team2ActualPlayers=team2[1:12]
    print ("Wellcome to digital IPL simulatiom")
    toss=random.randint(1,101)
    print('Initiating toss')
    if(toss%2==1):
        print('Team 1 won the toss,\n Enter "1" to choose Batting or "2" to choose Fielding')
        choiseOfTeam1=int(input())
        if(choiseOfTeam1==1):
            print ('Yay !!! Team 1 chose to Bat first.')
            x1=1
            runs=0
            runlistT1=[]
            over=0
            while(over<21):
                print("Choose the baller \n enter:\n '1' for t2p8b\n '2' for t2p9b\n '3' for t2p10b\n '4' for t2p11b" )
                bollerno=int(input())
                overlist=[]
                while(x1<11):
                    ball=1
                    if(bollerno==1):
                        print(team2[8],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x1]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x1+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1'):
                                x1+=1
                                runs+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs+=5
                                runs+=1
                            else:
                                runs+=overlist[ball-1]
                            runlistT1.append(overlist[ball-1])
                            ball+=1      
                    elif(bollerno==2):
                        print(team2[9],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x1]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x1+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x1+=1
                                runs+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs+=5
                                runs+=1
                                noBallCounter=6
                            else:
                                runs+=overlist[ball-1]
                            runlistT1.append(overlist[ball-1])
                            ball+=1
                    elif(bollerno==3):
                        print(team2[10],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x1]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x1+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x1+=1
                                runs+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs+=5
                                runs+=1
                            else:
                                runs+=overlist[ball-1]
                            runlistT1.append(overlist[ball-1])
                            ball+=1
                    elif(bollerno==4):
                        print(team2[11],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x1]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x1+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x1+=1
                                runs+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs+=5
                                runs+=1
                            else:
                                runs+=overlist[ball-1]
                            runlistT1.append(overlist[ball-1])
                            ball+=1
                    else :
                        print("*!!!Enter valid option!!!*")
                    break
                print(f"*{over} Over complete*\nWith total {runs} runs and {x1-1}wickets")
                over+=1
                if(x1>11):
                    print(f"!! All Out !!\n With score of {runs} for {x1} wickets \n Inning Break Team 1's Scorecard is as fllows: \n{runlistT1} \n Second Innings will commence shortly")
            print(f"Team 1's innings ended1\n With score of {runs} for {x1} wickets \n Inning Break Team 1's Scorecard is as fllows: \n{runlistT1} \n Second Innings will commence shortly")
            print("It's time for Team 2 to bat")
            x2=1
            runs2=0
            runlistT2=[]
            over=0
            while(over<21):
                print("Choose the baller \n enter:\n '1' for p8b\n '2' for p9b\n '3' for p10b\n '4' for p11b" )
                bollerno=int(input())
                overlist=[]
                while(x2<11):
                    ball=1
                    if(bollerno==1):
                        print(team1[8],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team2[x2]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1'):
                                x2+=1
                                runs2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs2+=5
                                runs2+=1
                            else:
                                runs2+=overlist[ball-1]
                            runlistT2.append(overlist[ball-1])
                            ball+=1      
                    elif(bollerno==2):
                        print(team2[9],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x2]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x2+=1
                                runs2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs2+=5
                                runs2+=1
                                noBallCounter=6
                            else:
                                runs2+=overlist[ball-1]
                            runlistT2.append(overlist[ball-1])
                            ball+=1
                    elif(bollerno==3):
                        print(team2[10],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x2]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x2+=1
                                runs2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs2+=5
                                runs2+=1
                            else:
                                runs2+=overlist[ball-1]
                            runlistT2.append(overlist[ball-1])
                            ball+=1
                    elif(bollerno==4):
                        print(team2[11],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x2]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x2+=1
                                runs2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs2+=5
                                runs2+=1
                            else:
                                runs2+=overlist[ball-1]
                            runlistT2.append(overlist[ball-1])
                            ball+=1
                    else :
                        print("*!!!Enter valid option!!!*")
                    break
                print(f"*{over} Over complete*\nWith total {runs2} runs and {x2-1}wickets")
                over+=1
                if(x2>11):
                    print(f"!! All Out !!\n With score of {runs2} for {x2} wickets \n End of second Innings Team 2's Scorecard is as fllows: \n{runlistT2} \n ")
            print(f"Team 2's innings ended1\n With score of {runs2} for {x1} wickets \n End of second Innings Team 2's Scorecard is as fllows: \n{runlistT2} \n ")
            if (runs<runs2):
                print(f"!!!!!!Hurray !!!!!!\nTeam 2 wins by {10-x2} wickets")
            else:
                print(f"!!!!!!Hurray !!!!!!\nTeam 1 wins by {runs-runs2} Runs")
        elif(choiseOfTeam1==2):
            print ('Yay !!! Team 1 chose to Bowl first.')
            x2=1
            runs2=0
            runlistT2=[]
            over=0
            while(over<21):
                print("Choose the baller \n enter:\n '1' for p8b\n '2' for p9b\n '3' for p10b\n '4' for p11b" )
                bollerno=int(input())
                overlist=[]
                while(x2<11):
                    ball=1
                    if(bollerno==1):
                        print(team1[8],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team2[x2]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1'):
                                x2+=1
                                runs2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs2+=5
                                runs2+=1
                            else:
                                runs2+=overlist[ball-1]
                            runlistT2.append(overlist[ball-1])
                            ball+=1      
                    elif(bollerno==2):
                        print(team2[9],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x2]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x2+=1
                                runs2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs2+=5
                                runs2+=1
                                noBallCounter=6
                            else:
                                runs2+=overlist[ball-1]
                            runlistT2.append(overlist[ball-1])
                            ball+=1
                    elif(bollerno==3):
                        print(team2[10],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x2]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x2+=1
                                runs2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs2+=5
                                runs2+=1
                            else:
                                runs2+=overlist[ball-1]
                            runlistT2.append(overlist[ball-1])
                            ball+=1
                    elif(bollerno==4):
                        print(team2[11],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x2]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x2+=1
                                runs2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs2+=5
                                runs2+=1
                            else:
                                runs2+=overlist[ball-1]
                            runlistT2.append(overlist[ball-1])
                            ball+=1
                    else :
                        print("*!!!Enter valid option!!!*")
                    break
                print(f"*{over} Over complete*\nWith total {runs2} runs and {x2-1}wickets")
                over+=1
                if(x2>11):
                    print(f"!! All Out !!\n With score of {runs2} for {x2} wickets \n Inning Break Team 2's Scorecard is as fllows: \n{runlistT2} \n Second Innings will commence shortly")
            print(f"Team 2's innings ended1\n With score of {runs2} for {x2} wickets \n Inning Break Team 2's Scorecard is as fllows: \n{runlistT2} \n Second Innings will commence shortly")
            print("It's time for Team 1 to bat")
            x1=1
            runs=0
            runlistT1=[]
            over=0
            while(over<21):
                print("Choose the baller \n enter:\n '1' for t2p8b\n '2' for t2p9b\n '3' for t2p10b\n '4' for t2p11b" )
                bollerno=int(input())
                overlist=[]
                while(x1<11):
                    ball=1
                    if(bollerno==1):
                        print(team2[8],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x1]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x1+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1'):
                                x1+=1
                                runs+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs+=5
                                runs+=1
                            else:
                                runs+=overlist[ball-1]
                            runlistT1.append(overlist[ball-1])
                            ball+=1      
                    elif(bollerno==2):
                        print(team2[9],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x1]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x1+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x1+=1
                                runs+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs+=5
                                runs+=1
                                noBallCounter=6
                            else:
                                runs+=overlist[ball-1]
                            runlistT1.append(overlist[ball-1])
                            ball+=1
                    elif(bollerno==3):
                        print(team2[10],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x1]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x1+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x1+=1
                                runs+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs+=5
                                runs+=1
                            else:
                                runs+=overlist[ball-1]
                            runlistT1.append(overlist[ball-1])
                            ball+=1
                    elif(bollerno==4):
                        print(team2[11],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x1]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x1+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x1+=1
                                runs+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs+=5
                                runs+=1
                            else:
                                runs+=overlist[ball-1]
                            runlistT1.append(overlist[ball-1])
                            ball+=1
                    else :
                        print("*!!!Enter valid option!!!*")
                    break
                print(f"*{over} Over complete*\nWith total {runs} runs and {x1-1}wickets")
                over+=1
                if(x1>11):
                    print(f"!! All Out !!\n With score of {runs} for {x1} wickets \n End of second Innings Team 2's Scorecard is as fllows: \n{runlistT1} \n ")
            print(f"Team 2's innings ended1\n With score of {runs} for {x2} wickets \n End of second Innings Team 2's Scorecard is as fllows: \n{runlistT1} \n ")
            if (runs2<runs):
                print(f"!!!!!!Hurray !!!!!!\nTeam 1 wins by {10-x1} wickets")
            else:
                print(f"!!!!!!Hurray !!!!!!\nTeam 2 wins by {runs2-runs} Runs")
        else:
            print("Enter a valid chouse!!")
    else:
        print('Team 2 won the toss,\n Enter "1" to choose Batting or "2" to choose Fielding')
        choiseOfTeam2=int(input())
        if(choiseOfTeam2==1):
            print ('Yay !!! Team 2 chose to Bat first.')
            x1=1
            runs=0
            runlistT1=[]
            over=0
            while(over<21):
                print("Choose the baller \n enter:\n '1' for p8b\n '2' for p9b\n '3' for p10b\n '4' for p11b" )
                bollerno=int(input())
                overlist=[]
                while(x1<11):
                    ball=1
                    if(bollerno==1):
                        print(team2[8],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x1]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x1+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1'):
                                x1+=1
                                runs+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs+=5
                                runs+=1
                            else:
                                runs+=overlist[ball-1]
                            runlistT1.append(overlist[ball-1])
                            ball+=1      
                    elif(bollerno==2):
                        print(team2[9],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x1]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x1+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x1+=1
                                runs+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs+=5
                                runs+=1
                                noBallCounter=6
                            else:
                                runs+=overlist[ball-1]
                            runlistT1.append(overlist[ball-1])
                            ball+=1
                    elif(bollerno==3):
                        print(team2[10],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x1]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x1+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x1+=1
                                runs+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs+=5
                                runs+=1
                            else:
                                runs+=overlist[ball-1]
                            runlistT1.append(overlist[ball-1])
                            ball+=1
                    elif(bollerno==4):
                        print(team2[11],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x1]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x1+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x1+=1
                                runs+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs+=5
                                runs+=1
                            else:
                                runs+=overlist[ball-1]
                            runlistT1.append(overlist[ball-1])
                            ball+=1
                    else :
                        print("*!!!Enter valid option!!!*")
                    break
                print(f"*{over} Over complete*\nWith total {runs} runs and {x1-1}wickets")
                over+=1
                if(x1>11):
                    print(f"!! All Out !!\n With score of {runs} for {x1} wickets \n Inning Break Team 1's Scorecard is as fllows: \n{runlistT1} \n Second Innings will commence shortly")
            print(f"Team 1's innings ended1\n With score of {runs} for {x1} wickets \n Inning Break Team 1's Scorecard is as fllows: \n{runlistT1} \n Second Innings will commence shortly")
            print("It's time for Team 2 to bat")
            x2=1
            runs2=0
            runlistT2=[]
            over=0
            while(over<21):
                print("Choose the baller \n enter:\n '1' for t2p8b\n '2' for t2p9b\n '3' for t2p10b\n '4' t2for p11b" )
                bollerno=int(input())
                overlist=[]
                while(x2<11):
                    ball=1
                    if(bollerno==1):
                        print(team1[8],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team2[x2]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1'):
                                x2+=1
                                runs2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs2+=5
                                runs2+=1
                            else:
                                runs2+=overlist[ball-1]
                            runlistT2.append(overlist[ball-1])
                            ball+=1      
                    elif(bollerno==2):
                        print(team2[9],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x2]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x2+=1
                                runs2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs2+=5
                                runs2+=1
                                noBallCounter=6
                            else:
                                runs2+=overlist[ball-1]
                            runlistT2.append(overlist[ball-1])
                            ball+=1
                    elif(bollerno==3):
                        print(team2[10],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x2]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x2+=1
                                runs2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs2+=5
                                runs2+=1
                            else:
                                runs2+=overlist[ball-1]
                            runlistT2.append(overlist[ball-1])
                            ball+=1
                    elif(bollerno==4):
                        print(team2[11],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x2]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x2+=1
                                runs2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs2+=5
                                runs2+=1
                            else:
                                runs2+=overlist[ball-1]
                            runlistT2.append(overlist[ball-1])
                            ball+=1
                    else :
                        print("*!!!Enter valid option!!!*")
                    break
                print(f"*{over} Over complete*\nWith total {runs2} runs and {x2-1}wickets")
                over+=1
                if(x2>11):
                    print(f"!! All Out !!\n With score of {runs2} for {x2} wickets \n End of second Innings Team 2's Scorecard is as fllows: \n{runlistT2} \n ")
            print(f"Team 2's innings ended1\n With score of {runs2} for {x1} wickets \n End of second Innings Team 2's Scorecard is as fllows: \n{runlistT2} \n ")
            if (runs<runs2):
                print(f"!!!!!!Hurray !!!!!!\nTeam 2 wins by {10-x2} wickets")
            else:
                print(f"!!!!!!Hurray !!!!!!\nTeam 1 wins by {runs-runs2} Runs")
        elif(choiseOfTeam2==2):
            print ('Yay !!! Team 2 chose to Bowl first.')
            x2=1
            runs2=0
            runlistT2=[]
            over=0
            while(over<21):
                print("Choose the baller \n enter:\n '1' for t2p8b\n '2' for t2p9b\n '3' for t2p10b\n '4' for t2p11b" )
                bollerno=int(input())
                overlist=[]
                while(x2<11):
                    ball=1
                    if(bollerno==1):
                        print(team2[8],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team2[x2]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1'):
                                x2+=1
                                runs2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs2+=5
                                runs2+=1
                            else:
                                runs2+=overlist[ball-1]
                            runlistT2.append(overlist[ball-1])
                            ball+=1      
                    elif(bollerno==2):
                        print(team2[9],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x2]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x2+=1
                                runs2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs2+=5
                                runs2+=1
                                noBallCounter=6
                            else:
                                runs2+=overlist[ball-1]
                            runlistT2.append(overlist[ball-1])
                            ball+=1
                    elif(bollerno==3):
                        print(team2[10],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x2]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x2+=1
                                runs2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs2+=5
                                runs2+=1
                            else:
                                runs2+=overlist[ball-1]
                            runlistT2.append(overlist[ball-1])
                            ball+=1
                    elif(bollerno==4):
                        print(team2[11],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x2]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x2+=1
                                runs2+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs2+=5
                                runs2+=1
                            else:
                                runs2+=overlist[ball-1]
                            runlistT2.append(overlist[ball-1])
                            ball+=1
                    else :
                        print("*!!!Enter valid option!!!*")
                    break
                print(f"*{over} Over complete*\nWith total {runs2} runs and {x2-1}wickets")
                over+=1
                if(x2>11):
                    print(f"!! All Out !!\n With score of {runs2} for {x2} wickets \n Inning Break Team 2's Scorecard is as fllows: \n{runlistT2} \n Second Innings will commence shortly")
            print(f"Team 2's innings ended1\n With score of {runs2} for {x2} wickets \n Inning Break Team 2's Scorecard is as fllows: \n{runlistT2} \n Second Innings will commence shortly")
            print("It's time for Team 1 to bat")
            x1=1
            runs=0
            runlistT1=[]
            over=0
            while(over<21):
                print("Choose the baller \n enter:\n '1' for t2p8b\n '2' for t2p9b\n '3' for t2p10b\n '4' for t2p11b" )
                bollerno=int(input())
                overlist=[]
                while(x1<11):
                    ball=1
                    if(bollerno==1):
                        print(team2[8],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x1]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x1+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1'):
                                x1+=1
                                runs+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs+=5
                                runs+=1
                            else:
                                runs+=overlist[ball-1]
                            runlistT1.append(overlist[ball-1])
                            ball+=1      
                    elif(bollerno==2):
                        print(team2[9],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x1]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x1+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x1+=1
                                runs+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs+=5
                                runs+=1
                                noBallCounter=6
                            else:
                                runs+=overlist[ball-1]
                            runlistT1.append(overlist[ball-1])
                            ball+=1
                    elif(bollerno==3):
                        print(team2[10],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x1]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x1+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x1+=1
                                runs+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs+=5
                                runs+=1
                            else:
                                runs+=overlist[ball-1]
                            runlistT1.append(overlist[ball-1])
                            ball+=1
                    elif(bollerno==4):
                        print(team2[11],' is bowling')
                        noBallCounter=6
                        while (ball<=noBallCounter):
                            overlist.append(random.choice(balloutcome))
                            print(f"{team1[x1]} : {over} . {ball} : {overlist[ball-1]}")
                            if(overlist[ball-1]=='out' or overlist[ball-1]=='lbw' or overlist[ball-1]=='runout0'):
                                x1+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='runout1') :
                                x1+=1
                                runs+=1
                                ball+=1
                                continue
                            elif(overlist[ball-1]=='wide' or overlist[ball-1]=='noball' or overlist[ball-1]==5):
                                noBallCounter+=1
                                if(overlist[ball-1]==5):
                                    runs+=5
                                runs+=1
                            else:
                                runs+=overlist[ball-1]
                            runlistT1.append(overlist[ball-1])
                            ball+=1
                    else :
                        print("*!!!Enter valid option!!!*")
                    break
                print(f"*{over} Over complete*\nWith total {runs} runs and {x1-1}wickets")
                over+=1
                if(x1>11):
                    print(f"!! All Out !!\n With score of {runs} for {x1} wickets \n End of second Innings Team 2's Scorecard is as fllows: \n{runlistT1} \n ")
            print(f"Team 2's innings ended1\n With score of {runs} for {x2} wickets \n End of second Innings Team 2's Scorecard is as fllows: \n{runlistT1} \n ")
            if (runs2<runs):
                print(f"!!!!!!Hurray !!!!!!\nTeam 1 wins by {10-x1} wickets")
            else:
                print(f"!!!!!!Hurray !!!!!!\nTeam 2 wins by {runs2-runs} Runs")
        else:
            print("Enter a valid chouse!!")
    print("Thank you for playing this game")
print("Enter '0' to exit '1' to have a rematch")
rm=int(input())
'''draw backs 
    code is very lenghthy
    did not use functions
    cannot track individual batters scores
    batter doesnot change after every single run 
    runs given by individual ballers are not recorded
    only single match can be simulated but not the whole tournament
    it would be better if file system were to be used
    real time team name , player name , batting order or bowlers cannot be altered'''