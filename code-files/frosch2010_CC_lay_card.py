import discord
import discord.member
import asyncio
from random import shuffle
from random import randrange


import frosch2010_Discord_Utils as fDU
import frosch2010_Console_Utils as fCU
import frosch2010_CC_other_functions as fCCOF
import frosch2010_CC_send_lay as fCCSL
import frosch2010_CC_Wish_choose_color as fCCWCC
import frosch2010_CC_generate_Card_Strs as fCGCS


async def lay_card(msg, client, ccVars, ccSettings, ccLanguage):

    if not msg.author in ccVars.cc_player_list:

        await fDU.send_Message_To_Channel(ccLanguage.cc_user_not_part.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
        fCU.log_In_Console("{} tried to lay a card, but he is not a part of the game.".format(msg.author.name), "LAY-CARD", "war")
        return


    if ccVars.cc_current_player != ccVars.cc_player_list.index(msg.author):

        await fDU.send_Message_To_Channel(ccLanguage.cc_user_no_turn.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
        fCU.log_In_Console("{} tried to lay a card, but it is not his turn.".format(msg.author.name), "LAY-CARD", "war")
        return


    args = msg.content.split(" ")


    if len(args) < 2:

        await fDU.send_Message_To_Channel(ccLanguage.cc_input_no_number_arg.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
        fCU.log_In_Console("{} tried to lay a card without a card-number.".format(msg.author.name), "LAY-CARD", "war")
        return


    if not args[1].isdigit():

        await fDU.send_Message_To_Channel(ccLanguage.cc_input_only_numbers.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
        fCU.log_In_Console("{} tried to lay a card without a card-number.".format(msg.author.name), "LAY-CARD", "war")
        return


    if int(args[1]) > len(ccVars.cc_player_hand[ccVars.cc_current_player]):

        await fDU.send_Message_To_Channel(ccLanguage.cc_card_not_exist.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
        fCU.log_In_Console("{} tried to lay a card with a card-number which does not exist.".format(msg.author.name), "LAY-CARD", "war")
        return


    #Suspend
    if ccVars.cc_player_is_suspend == True and ccVars.cc_suspended_player_can_lay == False:

        await fDU.send_Message_To_Channel(ccLanguage.cc_suspend_player_cant_lay_direct_chat.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
        fCU.log_In_Console("{} tried to lay a card, but he has to sit out.".format(msg.author.name), "LAY-CARD", "war")
        return


    #Choosed card    
    card_color = str(ccVars.cc_player_str_hand[ccVars.cc_current_player][(int(args[1]) - 1)]).split("*")[1].split(":")[0]
    card_number = str(ccVars.cc_player_str_hand[ccVars.cc_current_player][(int(args[1]) - 1)]).split("*")[1].split(":")[1]

    #Mid card
    mid_color = ccVars.cc_current_mid_card.split(":")[0]
    mid_number = ccVars.cc_current_mid_card.split(":")[1]


    #Suspend
    if ccVars.cc_player_is_suspend and card_number != "🚫":

        await fDU.send_Message_To_Channel(ccLanguage.cc_suspend_player_false_card.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
        fCU.log_In_Console("{} tried to lay a card that he cannot lay. She/He has to counter a suspend.".format(msg.author.name), "LAY-CARD", "war")
        return


    ccVars.cc_player_is_suspend = False
    ccVars.cc_suspended_player_can_lay = False

    
    if card_color != mid_color and card_number != mid_number and card_color != "wi" and card_color != ccVars.cc_current_wish_color:

        await fDU.send_Message_To_Channel(ccLanguage.cc_user_cant_lay_card.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
        fCU.log_In_Console("{} tried to lay a card that he cannot lay.".format(msg.author.name), "LAY-CARD", "war")
        return


    #Check if last mid was wish
    if ccVars.cc_current_wish_color != "":
        ccVars.cc_current_wish_color = ""


    #Check if plus two card
    if ccVars.cc_plus_card_amount > 0:
        if ccVars.cc_plus_player_can_lay:
            if card_number != "⏫":
            
                await fDU.send_Message_To_Channel(ccLanguage.cc_plus_card_player_lay_false_card.replace("[USER_ID]", "<@" + str(msg.author.id) + ">").replace("[PLUS_AMOUNT]", str(ccVars.cc_plus_card_amount)), [msg.channel], ccSettings.cc_message_auto_delete)
                fCU.log_In_Console("{} tried to lay a card that he cannot lay.".format(msg.author.name), "LAY-CARD", "war")
                return

        else:
            await fDU.send_Message_To_Channel(ccLanguage.cc_plus_card_player_cant_lay_false_card.replace("[USER_ID]", "<@" + str(msg.author.id) + ">").replace("[PLUS_AMOUNT]", str(ccVars.cc_plus_card_amount)), [msg.channel], ccSettings.cc_message_auto_delete)
            fCU.log_In_Console("{} tried to lay a card that he cannot lay. She/He must pick up the plus cards".format(msg.author.name), "LAY-CARD", "war")
            return


    #WISH - CARD    
    if card_color == "wi":


        #Wish next player get cards
        if card_number == "❓":
            ccVars.cc_wish_next_player_get_cards = True

        if card_number == "👨‍👨‍👧‍👦":
            
            card_amount = randrange(ccSettings.cc_wish_all_get_cards_amount_min, ccSettings.cc_wish_all_get_cards_amount_max)

            for player in ccVars.cc_player_list:

                player_index = ccVars.cc_player_list.index(player)


                if player_index == ccVars.cc_current_player:
                    continue


                while 10 > ((len(ccVars.cc_current_carddeck) - card_amount) / 2):

                    ccVars.cc_current_carddeck += ccVars.cc_carddeck_template

                    shuffle(ccVars.cc_current_carddeck)


                for i in range(card_amount):

                    ccVars.cc_player_hand[player_index].append(ccVars.cc_current_carddeck[0])

                    del ccVars.cc_current_carddeck[0]


                ccVars.cc_player_hand[player_index].sort()

                player_str_hand = fCGCS.generate_player_str_hand(ccVars.cc_player_hand[player_index], player_index, ccVars, ccLanguage)
                ccVars.cc_player_card_str[player_index] = player_str_hand[:]

        #---------------------------------------------------------------------------------------------------------------------


        ccVars.cc_player_wish_reacting = msg.author
        ccVars.cc_wish_react_card_num = ccVars.cc_player_str_hand[ccVars.cc_current_player][(int(args[1]) - 1)].split(":")[1]

        await fCCWCC.wish_choose_color(msg.author, ccVars, ccSettings, ccLanguage)


        fCU.log_In_Console("{} has laid a wish card.".format(msg.author.name), "LAY-CARD", "inf")


        await fCCOF.delete_lay_react_message(ccVars)

        return



    #Reverse Game
    if card_number == "🔄":

        #Toogle bool
        ccVars.cc_is_reversed = not ccVars.cc_is_reversed

    #Suspend card
    if card_number == "🚫":
        ccVars.cc_player_is_suspend = True


    #Plus card
    if card_number == "⏫":
        ccVars.cc_plus_card_amount += ccSettings.cc_plus_card_amount


    #Rotate Player cards
    if card_number == "🔂":
        ccVars.cc_rotate_player_hands = True


    if card_number != "❌":

        ccVars.cc_player_hand[ccVars.cc_current_player].remove(card_color + ":" + card_number)

    #Remove all cards with same color
    else:

        del_Card_Indexes = []

        for card in ccVars.cc_player_hand[ccVars.cc_current_player]:
            if card_color in card:
                del_Card_Indexes.append(card)


        for card in del_Card_Indexes:
            try:
                ccVars.cc_player_hand[ccVars.cc_current_player].remove(card)
            except:
                fCU.log_In_Console("One card could not be deleted!", "LAY-CARD", "war")
        

    #NEW MID-CARD
    new_mid_card = fCGCS.generate_mid_card_str(str(ccVars.cc_player_str_hand[ccVars.cc_current_player][(int(args[1]) - 1)]).split("*")[1], ccVars)
    ccVars.cc_current_mid_card = str(ccVars.cc_player_str_hand[ccVars.cc_current_player][(int(args[1]) - 1)]).split("*")[1]

    del ccVars.cc_player_str_hand[ccVars.cc_current_player][(int(args[1]) - 1)]


    #Reset vars
    fCCOF.reset_lay_react_vars(ccVars)


    fCU.log_In_Console("{} has laid a card...".format(msg.author.name), "LAY-CARD", "inf")


    await fCCSL.send_lay(new_mid_card, msg.author, client, ccVars, ccSettings, ccLanguage)