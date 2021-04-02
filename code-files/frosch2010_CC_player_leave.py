import discord
import discord.member
import asyncio


import frosch2010_Discord_Utils as fDU
import frosch2010_Console_Utils as fCU
import frosch2010_CC_other_functions as fCCOF


async def player_leave(msg, ccVars, ccSettings, ccLanguage):

    if not msg.author in ccVars.cc_player_list:

        await fDU.send_Message_To_Channel(ccLanguage.cc_user_leave_no_part.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], 4)
        fCU.log_In_Console("{} tried to leave the game, but he is not a part of the game.".format(msg.author.name), "LEAVE-COM", "war")
        return


    if (len(ccVars.cc_player_list) - 1) <= ccSettings.cc_min_players:

        ccVars.cc_player_list.remove(msg.author)


        #Print stop to all players
        player_channels = []

        for player in ccVars.cc_player_list:
            player_channels.append(player.dm_channel)

        await fDU.send_Message_To_Channel(ccLanguage.cc_game_end_because_user_left.replace("[USER_NAME]", msg.author.name), player_channels, 10)
        fCU.log_In_Console("The game is ended because {} has left the game and now there are not enough players.".format(msg.author.name), "LEAVE-COM", "war")


        fCU.log_In_Console("Delete reaction-messages...", "STOP-COM", "inf")

        #Delete wish-reaction, if possible:
        if ccVars.cc_wish_react_message != None:
            try:
                await ccVars.cc_wish_react_message.delete()
            except:
                pass


        #Delete old reaction-message
        if ccSettings.cc_play_with_reactions:
            try:
                await fCCOF.delete_lay_react_message(ccVars)
            except:
                pass


        fCU.log_In_Console("Delete card-messages...", "STOP-COM", "inf")

        #Delete card-messages
        for card_msg in ccVars.cc_card_messages:
            try:
                await card_msg.delete()
            except:
                pass


        fCU.log_In_Console("Reset variables...", "STOP-COM", "inf")

        fCCOF.reset_vars(ccVars)


        fCU.log_In_Console("cc stopped.".format(msg.author.name), "STOP-COM", "inf")

        return


    if msg.author.id == ccVars.cc_player_list[ccVars.cc_current_player].id:

        await fDU.send_Message_To_Channel(ccLanguage.cc_user_cant_leave_his_turn.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], 4)
        fCU.log_In_Console("{} tried to leave the game, but it is his turn.".format(msg.author.name), "LEAVE-COM", "war")
        return

    else:

        ccVars.cc_player_display_list = fCCOF.generate_current_display(ccVars, ccSettings)
        ccVars.cc_player_hand.remove(ccVars.cc_player_hand[ccVars.cc_player_list.index(msg.author)])
        ccVars.cc_player_str_hand.remove(ccVars.cc_player_str_hand[ccVars.cc_player_list.index(msg.author)])
        ccVars.cc_player_list.remove(msg.author)


        #Generate player-display-list-temp
        for player in ccVars.cc_player_list:
            ccVars.cc_player_display_list += player.name + "[COUNTER-" + str(player.id) + "]" + ", "

        ccVars.cc_player_display_list = ccVars.cc_player_display_list[:-2]


        #Generate current-display-list
        #current_display_list = fCCOF.generate_current_display(ccVars, ccSettings)

        fCU.log_In_Console("{} left the game.".format(msg.author.name), "LEAVE-COM", "inf")


        """
        #Delete wish-reaction, if possible:
        if ccVars.cc_wish_react_message != None:
            try:
                await ccVars.cc_wish_react_message.delete()
            except:
                pass


        #Delete old reaction-message
        if ccSettings.cc_play_with_reactions:
            try:
                await fCCOF.delete_lay_react_message(ccVars)
            except:
                pass



        #Generate player hands
        for player in ccVars.cc_player_list:

            player_index = ccVars.cc_player_list.index(player)
            
            if ccVars.cc_player_list.index(player) == ccVars.cc_current_player:

                player_msg = "##### **DU** bist dran #####\n\n**Deine Karten:**" + ccVars.cc_player_card_str[player_index] + "\n\n\n**Aktueller Kartenstapel:** (**" + msg.author.name + "** legte diese Karte)" + mid_card_str + "\n\n(Rundenfolge " + str(direction) + " : " + current_display_list + ")\n------------------------------------------" + fCCOF.generate_extra_msg_str(player.id, ccSettings, ccLanguage) + fCCOF.player_can_lay_cards_str(ccVars.cc_player_hand[player_index], ccVars, ccLanguage) + "\n------------------------------------------"

                await fCCOF.send_player_msg(player, player_msg, ccVars)


                if ccSettings.cc_play_with_reactions:
                    await fCCOF.send_player_hand_react_colors(ccVars, ccLanguage)

            else:

                player_msg = "#########################\n\n**Deine Karten:**" + ccVars.cc_player_card_str[player_index] + "\n\n\n**Aktueller Kartenstapel:**" + mid_card_str + "\n\n(Rundenfolge " + str(direction) + " : " + current_display_list + ")\n------------------------------------------" + "\n**" + ccVars.cc_player_list[ccVars.cc_current_player].name + "** ist an der Reihe." + "\n------------------------------------------"

                await fCCOF.send_player_msg(player, player_msg, ccVars)


        await fDU.send_Message_To_Channel(ccLanguage.cc_user_left("[USER_NAME]", msg.author.name), player_channels, 10)
        fCU.log_In_Console(" {} has left the game.".format(msg.author.name), "LEAVE-COM", "inf")


        #Delete card-messages
        for card_msg in ccVars.cc_card_messages:
            try:
                await card_msg.delete()
            except:
                pass"""