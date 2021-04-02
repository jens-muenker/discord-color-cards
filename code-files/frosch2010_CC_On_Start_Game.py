import discord
import asyncio
from random import shuffle
import random

import frosch2010_Console_Utils as fCU
import frosch2010_Discord_Utils as fDU
import frosch2010_CC_other_functions as fCCOF
import frosch2010_CC_voice_module as fCCVM
import frosch2010_CC_generate_Card_Strs as fCGCS

async def on_Start_Game(msg, cards_per_player, ccVars, ccSettings, ccLanguage, client):

    ccVars.cc_is_running = True

    #Print-Start
    fCU.log_In_Console("{} started game...".format(msg.author.name), "ON-START", "inf")
    await fDU.send_Message_To_Channel(ccLanguage.cc_user_started_game.replace("[USER_NAME]", str(msg.author.name)), [msg.channel])


    #Change card per player?
    args = msg.content.split(" ")

    if len(args) >= 3:

        try:

            cards_per_player = int(args[2])

            await fDU.send_Message_To_Channel(ccLanguage.cc_cards_per_player_set_to.replace("[COUNTER]", str(cards_per_player)), [msg.channel])
            fCU.log_In_Console("{} set cards per player to: {}".format(msg.author.name, str(cards_per_player)), "ON-START", "inf")

        except:
            
            fCU.log_In_Console("{} cant set cards per player. Cant parse card-count from arguments.".format(msg.author.name), "ON-START", "err")


    if ccSettings.cc_delete_old_messages:
    
        #Loesche Nachrichten in allen Privat-Channels der Spieler mit dem Bot
        fCU.log_In_Console("Delete messages for all players...", "ON-START", "inf")

        channels = []

        for player in ccVars.cc_player_list:

            await player.create_dm()

            channels.append(client.get_channel(player.dm_channel.id))

        await fDU.delete_Messages_From_Channel(channels, 4)


    #Add increase carddeck for players
    while cards_per_player * len(ccVars.cc_player_list) > (len(ccVars.cc_current_carddeck) / 2):
        ccVars.cc_current_carddeck += ccVars.cc_carddeck_template

    
    #Shuffel carddeck and playerlist
    shuffle(ccVars.cc_player_list)
    shuffle(ccVars.cc_current_carddeck)


    #Get mid card
    while True:

        random_card = random.randrange(0, len(ccVars.cc_current_carddeck) - 1)
        ccVars.cc_current_mid_card = ccVars.cc_current_carddeck[random_card]

        del ccVars.cc_current_carddeck[random_card]

        if not ccVars.cc_current_mid_card.startswith("wi"):
            break


    mid_card_str = fCGCS.generate_mid_card_str(ccVars.cc_current_mid_card, ccVars)
    direction = fCCOF.get_direction_str(ccVars)


    #Generate player-display-list-temp
    for player in ccVars.cc_player_list:
        ccVars.cc_player_display_list += player.name + "[COUNTER-" + str(player.id) + "]" + ", "

    ccVars.cc_player_display_list = ccVars.cc_player_display_list[:-2]


    #Generate current-display-list
    current_display_list = ccVars.cc_player_display_list[:]

    for player in ccVars.cc_player_list:
        if ccSettings.cc_show_player_card_count:
            current_display_list = current_display_list.replace(("[COUNTER-" + str(player.id) + "]"), (" **[" + str(cards_per_player) + "]**"))
        else:
            current_display_list = current_display_list.replace(("[COUNTER-" + str(player.id) + "]"), "")


    #Generate player hands
    for player in ccVars.cc_player_list:

        ccVars.cc_player_hand.append([])
        ccVars.cc_player_str_hand.append([])

        player_index = ccVars.cc_player_list.index(player)

        for i in range(cards_per_player):

            current_card = ccVars.cc_current_carddeck[random.randrange(0, len(ccVars.cc_current_carddeck) - 1)]

            ccVars.cc_current_carddeck.remove(current_card)

            ccVars.cc_player_hand[player_index].append(current_card)
            ccVars.cc_player_hand[player_index].sort()


        #Send hand to player
        player_str_hand = fCGCS.generate_player_str_hand(ccVars.cc_player_hand[player_index], player_index, ccVars, ccLanguage)
        ccVars.cc_player_card_str.append(player_str_hand)

        
        if ccVars.cc_player_list.index(player) == ccVars.cc_current_player:

            player_msg = "**------------------------------------------------**\n\n__**" + ccLanguage.cc_your_cards + ":**__" + ccVars.cc_player_card_str[player_index] + "\n\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_current_mid_card + ":**__" + mid_card_str + "\n\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_player_sequence + ":**__  " + str(direction) + "\n" + current_display_list + "\n**------------------------------------------------**|.|" + fCCOF.generate_extra_msg_str(player.id, ccSettings, ccLanguage) + fCCOF.player_can_lay_cards_str(ccVars.cc_player_hand[player_index], ccVars, ccLanguage) + "\n**------------------------------------------------**"

            await fCCOF.send_player_msg(player, player_msg, ccVars)


            if ccSettings.cc_play_with_reactions:
                await fCCOF.send_player_hand_react_colors(ccVars, ccLanguage)

        else:

            player_msg = "**------------------------------------------------**\n\n__**" + ccLanguage.cc_your_cards + ":**__" + ccVars.cc_player_card_str[player_index] + "\n\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_current_mid_card + ":**__" + mid_card_str + "\n\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_player_sequence + ":**__  " + str(direction) + "\n" + current_display_list + "\n**------------------------------------------------**|.|" + "\n**" + ccVars.cc_player_list[ccVars.cc_current_player].name + "** " + ccLanguage.cc_players_turn + "." + "\n**------------------------------------------------**"

            await fCCOF.send_player_msg(player, player_msg, ccVars)


    #Audio-Module
    if ccSettings.cc_use_voice:
        await fCCVM.say_text(ccLanguage.cc_voice_players_turn.replace("[USER_NAME]", ccVars.cc_player_list[ccVars.cc_current_player].name), ccSettings, client)


    #Use spectate-channel?
    if ccSettings.cc_show_game_in_spectate:

        spectate_channel = client.get_channel(ccSettings.cc_channelID_spectate)

        await spectate_channel.send(ccLanguage.cc_user_started_game.replace("[USER_NAME]", str(msg.author.name)) + "\n" + ccLanguage.cc_cards_per_player_set_to.replace("[COUNTER]", str(cards_per_player)))

        spectate_msg = "**------------------------------------------------**\n\n__**" + ccLanguage.cc_current_mid_card + ":**__" + mid_card_str + "\n**------------------------------------------------**|.|\n__**" + ccLanguage.cc_player_sequence + ":**__  " + str(direction) + "\n" + current_display_list + "\n**------------------------------------------------**|.|" + "\n**" + ccVars.cc_player_list[ccVars.cc_current_player].name + "** " + ccLanguage.cc_players_turn + "." + "\n**------------------------------------------------**"
        await fCCOF.send_player_msg(spectate_channel, spectate_msg, ccVars)