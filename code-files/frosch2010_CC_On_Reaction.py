import asyncio
import discord

import frosch2010_Console_Utils as fCU
import frosch2010_CC_Wish_react as fCCWR

async def on_Reaction_Add(reaction, user, ccVars, ccSettings, ccLanguage, client):

    if user != ccVars.cc_player_wish_reacting and user != ccVars.cc_player_lay_card_reacting:
        return
        
    
    #Wish-React
    if user == ccVars.cc_player_wish_reacting and not ccVars.cc_is_wish_reacting:

        await fCCWR.wish_react(reaction, user, ccVars, ccSettings, ccLanguage, client)

    else:
       
       fCU.log_In_Console("This should not have happened. Sorry :(", "REACT-ADD", "err")