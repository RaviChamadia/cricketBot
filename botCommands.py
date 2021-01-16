import cricketData

def commands(primaryCommand,secondaryCommand=None):
    cricket=cricketData.cricketData()
    if primaryCommand.lower()=="hello" or primaryCommand.lower()=="hi" or primaryCommand.lower()=="hey":
        msg="Hey I'm cricket Bot. Please Type !help for Help"
        return msg
    if primaryCommand[0]=='!':
        if primaryCommand[1::]=="help":
            msg="""A prefix for commands is '!'
Following are *Commands* :-
!help - Help for Commands.
!live - For Live Matches.
!schedule - For Upcomming matches.
!score @TeamName - For Live Score of paticular Match."""
            return msg
        elif primaryCommand[1::]=="live":
            return cricket.live()
        elif primaryCommand[1::]=="schedule":
            return cricket.cal()
        elif primaryCommand[1::]=="score":
            if secondaryCommand != None and secondaryCommand[0]=='@':
                msg=cricket.score(secondaryCommand[1::])
                if msg:
                    return msg
                else:
                    msg="No Live Match found of "+str(secondaryCommand[1::])+". Please Type !live for Live match"
                    return msg
            else:
                msg="For Score Please Type !score @TeamName"
                return msg
        else:
            msg="Invalid command Please type !help for Help."
            return msg
