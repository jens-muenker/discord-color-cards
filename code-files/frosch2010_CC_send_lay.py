import discord
import discord.member
import asyncio
from random import shuffle
from random import randrange



import frosch2010_Discord_Utils as fDU
import frosch2010_Console_Utils as fCU
import frosch2010_Class_Utils as fCLU
import frosch2010_CC_other_functions as fCCOF
import frosch2010_CC_manage_timer as fCMT
import frosch2010_CC_voice_module as fCCVM
import frosch2010_CC_generate_Card_Strs as fCGCS


async def send_lay(new_mid_card, user, client, ccVars, ccSettings, ccLanguage):


    #Generate new hand str
    player_str_hand = fCGCS.generate_player_str_hand(ccVars.cc_player_hand[ccVars.cc_current_player], ccVars.cc_current_player, ccVars, ccLanguage)
    ccVars.cc_player_card_str[ccVars.cc_current_player] = player_str_hand[:]


    #Check if rotate player hands
    if ccVars.cc_rotate_player_hands:

        #links
        if ccVars.cc_is_reversed:

            first_player_card_str = ccVars.cc_player_card_str[0][:]

            del ccVars.cc_player_card_str[0]

            ccVars.cc_player_card_str.append(first_player_card_str)


            first_player_hand = ccVars.cc_player_hand[0][:]

            del ccVars.cc_player_hand[0]

            ccVars.cc_player_hand.append(first_player_hand)


            first_player_str_hand = ccVars.cc_player_str_hand[0][:]

            del ccVars.cc_player_str_hand[0]

            ccVars.cc_player_str_hand.append(first_player_str_hand)


        #rechts
        else:

            last_player_card_str = ccVars.cc_player_card_str[(len(ccVars.cc_player_card_str) - 1)][:]

            del ccVars.cc_player_card_str[(len(ccVars.cc_player_card_str) - 1)]

            ccVars.cc_player_card_str.insert(0, last_player_card_str)


            last_player_hand = ccVars.cc_player_hand[(len(ccVars.cc_player_hand) - 1)][:]

            del ccVars.cc_player_hand[(len(ccVars.cc_player_hand) - 1)]

            ccVars.cc_player_hand.insert(0, last_player_hand)


            last_player_str_hand = ccVars.cc_player_str_hand[(len(ccVars.cc_player_str_hand) - 1)][:]

            del ccVars.cc_player_str_hand[(len(ccVars.cc_player_str_hand) - 1)]

            ccVars.cc_player_str_hand.insert(0, last_player_str_hand)


        ccVars.cc_rotate_player_hands = False


    #Check if cc
    player_has_cc = fCCOF.check_if_player_has_cc(ccVars)

    #Check if WON
    player_won = fCCOF.check_if_player_won(ccVars)


    #Set next player
    fCCOF.next_player(ccVars)



    #Wish next player get cards
    if ccVars.cc_wish_next_player_get_cards:

        ccVars.cc_wish_next_player_get_cards = False
        card_amount = randrange(ccSettings.cc_wish_next_get_cards_amount_min, ccSettings.cc_wish_next_get_cards_amount_max)

        while 10 > ((len(ccVars.cc_current_carddeck) - card_amount) / 2):

            ccVars.cc_current_carddeck += ccVars.cc_carddeck_template

            shuffle(ccVars.cc_current_carddeck)


        for i in range(card_amount):

            ccVars.cc_player_hand[ccVars.cc_current_player].append(ccVars.cc_current_carddeck[0])

            del ccVars.cc_current_carddeck[0]


        ccVars.cc_player_hand[ccVars.cc_current_player].sort()

        player_str_hand = fCGCS.generate_player_str_hand(ccVars.cc_player_hand[ccVars.cc_current_player], ccVars.cc_current_player, ccVars, ccLanguage)
        ccVars.cc_player_card_str[ccVars.cc_current_player] = player_str_hand[:]



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


    #Can player counter suspend
    if ccVars.cc_player_is_suspend:
        ccVars.cc_suspended_player_can_lay = fCCOF.check_if_player_can_counter_suspend(ccVars)


    #Can player counter plus card
    if ccVars.cc_plus_card_amount > 0:
        ccVars.cc_plus_player_can_lay = fCCOF.check_if_player_can_counter_plus_two(ccVars)


    #Send game to player
    for player in ccVars.cc_player_list:

        player_index = ccVars.cc_player_list.index(player)

        if player.name == user.name:

            player_msg = "**------------------------------------------------**\n\n__**" + ccLanguage.cc_your_cards + ":**__" + ccVars.cc_player_card_str[player_index] + "\n\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_current_mid_card + ":**__" + new_mid_card + "\n\n(**" + user.name + "** " + ccLanguage.cc_player_laid_card + ")" + "\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_player_sequence + ":**__  " + str(direction) + "\n" + current_display_list + "\n**------------------------------------------------**|.|" + "\n**" + ccVars.cc_player_list[ccVars.cc_current_player].name + "** " + ccLanguage.cc_players_turn + "." + "\n**------------------------------------------------**"

            await fCCOF.send_player_msg(player, player_msg, ccVars)         

        else:

            if player.name == ccVars.cc_player_list[ccVars.cc_current_player].name:

                player_msg = "**------------------------------------------------**\n\n__**" + ccLanguage.cc_your_cards + ":**__" + ccVars.cc_player_card_str[player_index] + "\n\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_current_mid_card + ":**__" + new_mid_card + "\n\n(**" + user.name + "** " + ccLanguage.cc_player_laid_card + ")" + "\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_player_sequence + ":**__  " + str(direction) + "\n" + current_display_list + "\n**------------------------------------------------**|.|" + fCCOF.generate_extra_msg_str(player.id, ccSettings, ccLanguage) + fCCOF.player_can_lay_cards_str(ccVars.cc_player_hand[player_index], ccVars, ccLanguage) + fCCOF.str_player_has_cc(player_has_cc, user.name, ccLanguage) + "\n**------------------------------------------------**"

                await fCCOF.send_player_msg(player, player_msg, ccVars)

                if ccSettings.cc_play_with_reactions:
                    await fCCOF.send_player_hand_react_colors(ccVars, ccLanguage)

            else:

                player_msg = "**------------------------------------------------**\n\n__**" + ccLanguage.cc_your_cards + ":**__" + ccVars.cc_player_card_str[player_index] + "\n\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_current_mid_card + ":**__" + new_mid_card + "\n\n(**" + user.name + "** " + ccLanguage.cc_player_laid_card + ")" + "\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_player_sequence + ":**__  " + str(direction) + "\n" + current_display_list + "\n**------------------------------------------------**|.|" + "\n**" + ccVars.cc_player_list[ccVars.cc_current_player].name + "** " + ccLanguage.cc_players_turn + "." + fCCOF.str_player_has_cc(player_has_cc, user.name, ccLanguage) + "\n**------------------------------------------------**"

                await fCCOF.send_player_msg(player, player_msg, ccVars)

        
        if player_won:
            await fDU.send_Message_To_Channel(ccLanguage.cc_player_won.replace("[USER_NAME]", user.name), [player.dm_channel])



    #Can player counter suspend
    if ccVars.cc_player_is_suspend:
        if ccVars.cc_suspended_player_can_lay == False:
            fCLU.Timer(10, fCMT.manage_timer, [ccVars, ccSettings, ccLanguage, client])


    #Can player counter plus card
    if ccVars.cc_plus_card_amount > 0 and ccVars.cc_plus_player_can_lay == False:
        fCLU.Timer(10, fCMT.manage_timer, [ccVars, ccSettings, ccLanguage, client])


    #Use spectate-channel?
    if ccSettings.cc_show_game_in_spectate:

        spectate_channel = client.get_channel(ccSettings.cc_channelID_spectate)

        spectate_msg = "**------------------------------------------------**\n\n__**" + ccLanguage.cc_current_mid_card + ":**__" + new_mid_card + "\n\n(**" + user.name + "** " + ccLanguage.cc_player_laid_card + ".)" + "\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_player_sequence + ":**__  " + str(direction) + "\n" + current_display_list + "\n**------------------------------------------------**|.|" + "\n**" + ccVars.cc_player_list[ccVars.cc_current_player].name + "** " + ccLanguage.cc_players_turn + "." + fCCOF.str_player_has_cc(player_has_cc, user.name, ccLanguage) + "\n**------------------------------------------------**"
        await fCCOF.send_player_msg(spectate_channel, spectate_msg, ccVars)

        if player_won:
            await spectate_channel.send(ccLanguage.cc_player_won.replace("[USER_NAME]", user.name))


    #Reset Game, if player won
    if player_won:
        if ccSettings.cc_use_voice:
            if ccVars.cc_player_is_suspend and ccVars.cc_suspended_player_can_lay == False:
                await fCCVM.say_text(ccLanguage.cc_voice_player_sit_out.replace("[USER_NAME]", user.name), ccSettings, client)
            else:
                await fCCVM.say_text(ccLanguage.cc_voice_player_won.replace("[USER_NAME]", user.name), ccSettings, client)

        fCU.log_In_Console("{} won the game.".format(user.name), "SEND-LAY", "inf")
        fCCOF.reset_vars(ccVars)

        #Audio-Module
        await fCCVM.disconnect_when_possible(ccSettings, client)


    else:

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