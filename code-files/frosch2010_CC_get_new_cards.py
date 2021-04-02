import discord
import discord.member
import asyncio
from random import shuffle


import frosch2010_Discord_Utils as fDU
import frosch2010_Console_Utils as fCU
import frosch2010_CC_other_functions as fCCOF
import frosch2010_CC_send_new_cards as fCCSNC


async def get_new_card(msg, client, ccVars, ccSettings, ccLanguage):

    if not msg.author in ccVars.cc_player_list:

        await fDU.send_Message_To_Channel(ccLanguage.cc_user_not_part.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
        fCU.log_In_Console("{} tried to get a new card, but she/he is not a part of the game.".format(msg.author.name), "LAY-CARD", "war")
        return


    if ccVars.cc_current_player != ccVars.cc_player_list.index(msg.author):

        await fDU.send_Message_To_Channel(ccLanguage.cc_user_no_turn.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
        fCU.log_In_Console("{} tried to get a new card, but it is not her/his turn.".format(msg.author.name), "LAY-CARD", "war")
        return


    if ccVars.cc_plus_card_amount > 0:

        if ccVars.cc_plus_player_can_lay:

            await fDU.send_Message_To_Channel(ccLanguage.cc_plus_card_player_cant_get_new_cards.replace("[USER_ID]", "<@" + str(msg.author.id) + ">").replace("[USER_ID]", str(ccVars.cc_plus_card_amount)), [msg.channel], ccSettings.cc_message_auto_delete)
            fCU.log_In_Console("{} tried to get a new card, but she/he has to counter or take the plus cards.".format(msg.author.name), "LAY-CARD", "war")
            return

        else:

            await fDU.send_Message_To_Channel(ccLanguage.cc_plus_card_player_counter_cant_get_new_cards.replace("[USER_ID]", "<@" + str(msg.author.id) + ">").replace("[USER_ID]", str(ccVars.cc_plus_card_amount)), [msg.channel], ccSettings.cc_message_auto_delete)
            fCU.log_In_Console("{} tried to get a new card, but she/he has to counter or take the plus cards.".format(msg.author.name), "LAY-CARD", "war")
            return            

    
    if ccVars.cc_player_is_suspend:

        if ccVars.cc_suspended_player_can_lay:

            await fDU.send_Message_To_Channel(ccLanguage.cc_suspend_player_counter_cant_get_new_cards.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
            fCU.log_In_Console("{} tried to get a new card, but she/he has to sit out or counter sit out.".format(msg.author.name), "LAY-CARD", "war")
            return

        else:

            await fDU.send_Message_To_Channel(ccLanguage.cc_suspend_player_cant_get_new_cards.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
            fCU.log_In_Console("{} tried to get a new card, but she/he has to sit out or counter sit out.".format(msg.author.name), "LAY-CARD", "war")
            return            


    #Reset vars
    fCCOF.reset_lay_react_vars(ccVars)


    fCU.log_In_Console("{} got a new card...".format(msg.author.name), "LAY-CARD", "inf")


    await fCCSNC.send_new_cards(msg.author, client, ccVars, ccSettings, ccLanguage)