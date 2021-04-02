import asyncio
import discord

import frosch2010_Console_Utils as fCU
import frosch2010_Discord_Utils as fDU
import frosch2010_CC_other_functions as fCCOF
import frosch2010_CC_send_lay as fCCSL
import frosch2010_CC_generate_Card_Strs as fCGCS


async def wish_react(reaction, user, ccVars, ccSettings, ccLanguage, client):

    if reaction.emoji != "🟥" and reaction.emoji != "🟨" and reaction.emoji != "🟩" and reaction.emoji != "🟦":

        await fDU.send_Message_To_Channel(ccLanguage.cc_false_choose_color_react.replace("[USER_ID]", "<@" + str(user.id) + ">"), [user.dm_channel], 6)
        fCU.log_In_Console("{} reacted with an invalid color.".format(user.name), "WISH-REACT", "war")

        return
        

    ccVars.cc_is_wish_reacting = True


    #Set color
    if reaction.emoji == "🟥":
        ccVars.cc_current_wish_color = "r"

    elif reaction.emoji == "🟨":
        ccVars.cc_current_wish_color = "y"

    elif reaction.emoji == "🟩":
        ccVars.cc_current_wish_color = "g"

    else:
        ccVars.cc_current_wish_color = "b"

    #NEW MID-CARD
    new_mid_card = fCGCS.generate_mid_card_str("wi:" + ccVars.cc_wish_react_card_num, ccVars)
    ccVars.cc_current_mid_card = str("wi:" + ccVars.cc_wish_react_card_num)

    ccVars.cc_player_hand[ccVars.cc_current_player].remove("wi:" + ccVars.cc_wish_react_card_num)


    #Reset vars
    fCCOF.reset_lay_react_vars(ccVars)
    

    await fCCSL.send_lay(new_mid_card, user, client, ccVars, ccSettings, ccLanguage)