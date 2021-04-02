import discord
import discord.member
import asyncio
from random import shuffle


import frosch2010_Discord_Utils as fDU
import frosch2010_Console_Utils as fCU
import frosch2010_CC_other_functions as fCCOF
import frosch2010_CC_generate_Card_Strs as fCGCS
import frosch2010_CC_voice_module as fCCVM


async def send_new_cards(user, client, ccVars, ccSettings, ccLanguage):

    #cc EXTREME ZIEHEN EINBAUEN!

    while 10 > ((len(ccVars.cc_current_carddeck) - 1) / 2):

        ccVars.cc_current_carddeck += ccVars.cc_carddeck_template

        shuffle(ccVars.cc_current_carddeck)


    for i in range(1):

        ccVars.cc_player_hand[ccVars.cc_current_player].append(ccVars.cc_current_carddeck[0])

        del ccVars.cc_current_carddeck[0]


    ccVars.cc_player_hand[ccVars.cc_current_player].sort()


    ccVars.cc_player_is_suspend = False
    ccVars.cc_suspended_player_can_lay = False


    fCCOF.next_player(ccVars)


    #Generate mid card
    new_mid_card = fCGCS.generate_mid_card_str(ccVars.cc_current_mid_card, ccVars)


    #Get direction
    direction = fCCOF.get_direction_str(ccVars)


    #Get all old cards
    old_cards = ccVars.cc_card_messages[:]


    #Delete wish-reaction, if possible:
    if ccVars.cc_wish_react_message != None:
        try:
            await ccVars.cc_wish_react_message.delete()
        except:
            pass


    #Delete old reaction-message
    if ccSettings.cc_play_with_reactions:
        await fCCOF.delete_lay_react_message(ccVars)


    #Generate current-display-list
    current_display_list = fCCOF.generate_current_display(ccVars, ccSettings)


    #Send game to player
    for player in ccVars.cc_player_list:

        player_index = ccVars.cc_player_list.index(player)

        if player.name == user.name:

            #Generate new hand str
            player_str_hand = fCGCS.generate_player_str_hand(ccVars.cc_player_hand[player_index], player_index, ccVars, ccLanguage)
            ccVars.cc_player_card_str[player_index] = player_str_hand[:]


            player_msg = "**------------------------------------------------**\n\n__**Deine Karten:**__" + player_str_hand + "\n\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_current_mid_card + ":**__" + new_mid_card + "\n\n(**" + user.name + "** " + ccLanguage.cc_player_picked_up_card + ".)" + "\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_player_sequence + ":**__  " + str(direction) + "\n" + current_display_list + "\n**------------------------------------------------**|.|" + "\n**" + ccVars.cc_player_list[ccVars.cc_current_player].name + "** " + ccLanguage.cc_players_turn + "." + "\n**------------------------------------------------**"

            await fCCOF.send_player_msg(player, player_msg, ccVars)

        else:

            if player.name == ccVars.cc_player_list[ccVars.cc_current_player].name:

                player_msg = "**------------------------------------------------**\n\n__**" + ccLanguage.cc_your_cards + ":**__" + ccVars.cc_player_card_str[player_index] + "\n\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_current_mid_card + ":**__" + new_mid_card + "\n\n(**" + user.name + "** " + ccLanguage.cc_player_picked_up_card + ".)" + "\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_player_sequence + ":**__  " + str(direction) + "\n" + current_display_list + "\n**------------------------------------------------**|.|" + fCCOF.generate_extra_msg_str(player.id, ccSettings, ccLanguage) + fCCOF.player_can_lay_cards_str(ccVars.cc_player_hand[player_index], ccVars, ccLanguage) + "\n**------------------------------------------------**"

                await fCCOF.send_player_msg(player, player_msg, ccVars)


                if ccSettings.cc_play_with_reactions:
                    await fCCOF.send_player_hand_react_colors(ccVars, ccLanguage)

            else:

                player_msg = "**------------------------------------------------**\n\n__**" + ccLanguage.cc_your_cards + ":**__" + ccVars.cc_player_card_str[player_index] + "\n\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_current_mid_card + ":**__" + new_mid_card + "\n\n(**" + user.name + "** " + ccLanguage.cc_player_picked_up_card + ".)" + "\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_player_sequence + ":**__  " + str(direction) + "\n" + current_display_list + "\n**------------------------------------------------**|.|" + "\n**" + ccVars.cc_player_list[ccVars.cc_current_player].name + "** " + ccLanguage.cc_players_turn + "." + "\n**------------------------------------------------**"

                await fCCOF.send_player_msg(player, player_msg, ccVars)


    #Use spectate-channel?
    if ccSettings.cc_show_game_in_spectate:

        spectate_channel = client.get_channel(ccSettings.cc_channelID_spectate)

        spectate_msg = "**------------------------------------------------**\n\n__**" + ccLanguage.cc_current_mid_card + ":**__" + new_mid_card + "\n\n(**" + user.name + "** " + ccLanguage.cc_player_picked_up_card + ".)" + "\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_player_sequence + ":**__  " + str(direction) + "\n" + current_display_list + "\n**------------------------------------------------**|.|" + "\n**" + ccVars.cc_player_list[ccVars.cc_current_player].name + "** " + ccLanguage.cc_players_turn + "." + "\n**------------------------------------------------**"
        await fCCOF.send_player_msg(spectate_channel, spectate_msg, ccVars)


    #Audio-Module
    if ccSettings.cc_use_voice:
        await fCCVM.say_text(ccLanguage.cc_voice_players_turn.replace("[USER_NAME]", ccVars.cc_player_list[ccVars.cc_current_player].name), ccSettings, client)


    if ccSettings.cc_delete_old_messages:
    
        #Delete all old card-messages
        for card_msg in old_cards:
            try:
                await card_msg.delete()
            except:
                pass