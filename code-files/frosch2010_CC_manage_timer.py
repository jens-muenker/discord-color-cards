import discord
import asyncio
from random import shuffle

import frosch2010_Console_Utils as fCU
import frosch2010_Class_Utils as fCLU
import frosch2010_CC_other_functions as fCCOF
import frosch2010_CC_voice_module as fCCVM
import frosch2010_CC_generate_Card_Strs as fCGCS


async def manage_timer(ccVars, ccSettings, ccLanguage, client):

    previous_player_name = ccVars.cc_player_list[ccVars.cc_current_player].name[:]


    #Suspend-Card-Code
    if ccVars.cc_player_is_suspend:
        fCU.log_In_Console("{} siting out.".format(previous_player_name), "MAN-TIME", "inf")

    #Plus-Card-Code
    else:

        fCU.log_In_Console("{} had to take plus cards.".format(previous_player_name), "MAN-TIME", "inf")


        #Add cards to the deck if necessary
        while 10 > ((len(ccVars.cc_current_carddeck) - ccVars.cc_plus_card_amount) / 2):

            ccVars.cc_current_carddeck += ccVars.cc_carddeck_template
            shuffle(ccVars.cc_current_carddeck)


        #Add cards to player hand
        for i in range(ccVars.cc_plus_card_amount):

            ccVars.cc_player_hand[ccVars.cc_current_player].append(ccVars.cc_current_carddeck[0])
            del ccVars.cc_current_carddeck[0]


        ccVars.cc_player_hand[ccVars.cc_current_player].sort()

        #Generate new hand str
        player_str_hand = fCGCS.generate_player_str_hand(ccVars.cc_player_hand[ccVars.cc_current_player], ccVars.cc_current_player, ccVars, ccLanguage)
        ccVars.cc_player_card_str[ccVars.cc_current_player] = player_str_hand[:]



    fCCOF.next_player(ccVars)

    if ccVars.cc_player_is_suspend:
        ccVars.cc_player_is_suspend = False
        ccVars.cc_suspended_player_can_lay = False


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


    if ccVars.cc_plus_card_amount > 0:
        ccVars.cc_plus_card_amount = 0
        ccVars.cc_plus_player_can_lay = False
        ccVars.cc_plus_print = True


    #Send game to player
    for player in ccVars.cc_player_list:

        player_index = ccVars.cc_player_list.index(player)

        if player.name == ccVars.cc_player_list[ccVars.cc_current_player].name:

            player_msg = "**------------------------------------------------**\n\n__**Deine Karten:**__" + ccVars.cc_player_card_str[player_index] + "\n\n**------------------------------------------------**|.|\n__**Aktueller Kartenstapel:**__" + new_mid_card + "\n\n(**" + previous_player_name + "**" + fCCOF.timer_action_str(ccVars, ccLanguage) + ")" + "\n**------------------------------------------------**|.|\n__**Rundenfolge:**__  " + str(direction) + "\n" + current_display_list + "\n**------------------------------------------------**|.|" + fCCOF.generate_extra_msg_str(player.id, ccSettings, ccLanguage) + fCCOF.player_can_lay_cards_str(ccVars.cc_player_hand[player_index], ccVars, ccLanguage, ) + "\n**------------------------------------------------**"

            await fCCOF.send_player_msg(player, player_msg, ccVars)


            if ccSettings.cc_play_with_reactions:
                await fCCOF.send_player_hand_react_colors(ccVars, ccLanguage)

        else:

            player_msg = "**------------------------------------------------**\n\n__**Deine Karten:**__" + ccVars.cc_player_card_str[player_index] + "\n\n**------------------------------------------------**|.|\n__**Aktueller Kartenstapel:**__" + new_mid_card + "\n\n(**" + previous_player_name + "**" + fCCOF.timer_action_str(ccVars, ccLanguage) + ")" + "\n**------------------------------------------------**|.|\n__**Rundenfolge:**__  " + str(direction) + "\n" + current_display_list + "\n**------------------------------------------------**|.|" + "\n**" + ccVars.cc_player_list[ccVars.cc_current_player].name + "** ist an der Reihe." + "\n**------------------------------------------------**"

            await fCCOF.send_player_msg(player, player_msg, ccVars)


    if ccVars.cc_plus_print:
        ccVars.cc_plus_print = False


    if ccSettings.cc_use_voice:
        if ccVars.cc_player_is_suspend and ccVars.cc_suspended_player_can_lay == False:
            await fCCVM.say_text(ccLanguage.cc_voice_player_sit_out.replace("[USER_NAME]", ccVars.cc_player_list[ccVars.cc_current_player].name), ccSettings, client)
        else:
            await fCCVM.say_text(ccLanguage.cc_voice_players_turn.replace("[USER_NAME]", ccVars.cc_player_list[ccVars.cc_current_player].name), ccSettings, client)


    if ccSettings.cc_delete_old_messages:

        #Delete all old card-messages
        for card_msg in old_cards:
            try:
                await card_msg.delete()
            except:
                pass