import discord
import discord.member
import asyncio


import frosch2010_Discord_Utils as fDU
import frosch2010_Console_Utils as fCU


def timer_action_str(ccVars, ccLanguage):

    if ccVars.cc_plus_print:
        return ccLanguage.cc_timer_action_take_plus_cards
    else:
        return ccLanguage.cc_timer_action_sit_out


def player_can_counter_plus_card_str(ccVars, ccLanguage):

    if ccVars.cc_plus_player_can_lay:
        return ccLanguage.cc_plus_card_player_can_lay.replace("[PLUS_AMOUNT]", str(ccVars.cc_plus_card_amount))
    else:
        return ccLanguage.cc_plus_card_player_cant_lay.replace("[PLUS_AMOUNT]", str(ccVars.cc_plus_card_amount))


def check_if_player_can_counter_plus_two(ccVars):

    can_counter = False

    for card in ccVars.cc_player_hand[ccVars.cc_current_player]:

        split_card = str(card).split(":")

        if split_card[1] == "⏫":
            can_counter = True
            break

    return can_counter


def player_can_counter_suspend_str(ccVars, ccLanguage):

    if ccVars.cc_suspended_player_can_lay:
        return ccLanguage.cc_supend_player_cant_lay

    else:
        return ccLanguage.cc_suspend_player_must_counter


def check_if_player_can_counter_suspend(ccVars):

    can_counter = False

    for card in ccVars.cc_player_hand[ccVars.cc_current_player]:

        split_card = str(card).split(":")

        if split_card[1] == "🚫":
            can_counter = True
            break

    return can_counter


def generate_current_display(ccVars, ccSettings):

    #Generate current-display-list
    current_display_list = ccVars.cc_player_display_list[:]

    for player in ccVars.cc_player_list:
        if ccSettings.cc_show_player_card_count:
            current_display_list = current_display_list.replace(("[COUNTER-" + str(player.id) + "]"), (" **[" + str(len(ccVars.cc_player_hand[ccVars.cc_player_list.index(player)])) + "]**"))

        else:
            current_display_list = current_display_list.replace(("[COUNTER-" + str(player.id) + "]"), "")


    return current_display_list


async def send_player_msg(player, msg, ccVars):

    if len(msg) > 1400:

        is_first = True

        while True:

            if len(msg) > 1400:

                last_splitable = msg[:1400].rfind("|.|")

                if is_first:
                    card_msg = await player.send(msg[:(last_splitable + 3)].replace("|.|", ""))
                    is_first = False

                else:
                    card_msg = await player.send(("." + msg[:(last_splitable + 3)].replace("|.|", "")))

                msg = msg[(last_splitable + 4):]
                ccVars.cc_card_messages.append(card_msg)

            else:
                card_msg = await player.send(("." + msg.replace("|.|", "")))
                ccVars.cc_card_messages.append(card_msg)
                break

    else:
        card_msg = await player.send(msg.replace("|.|", ""))
        ccVars.cc_card_messages.append(card_msg)


async def delete_lay_react_message(ccVars):

    #Delete old reaction-message
    try:
        await ccVars.cc_lay_card_react_message.delete()
    except:
        pass


def reset_lay_react_vars(ccVars):

    ccVars.cc_player_wish_reacting = None
    ccVars.cc_is_wish_reacting = False
    ccVars.cc_next_react_is_number = False
    ccVars.cc_player_lay_card_reacting = None
    ccVars.cc_lay_card_react_message = None
    ccVars.cc_lay_card_possible_numbers = []
    ccVars.cc_lay_card_react_choosed_color = ""
    ccVars.cc_is_lay_card_reacting = False


def generate_extra_msg_str(playerID, ccSettings, ccLanguage):

    if ccSettings.cc_send_extra_msg_if_players_turn:
        return "\n<@" + str(playerID) + ">"

    else:
        return "\n**DU**"


async def send_player_hand_react_colors(ccVars, ccLanguage):

    if ccVars.cc_player_is_suspend == True and ccVars.cc_suspended_player_can_lay == False:
        return


    color_red = False
    color_yellow = False
    color_green = False
    color_blue = False
    color_wish = False

    #Check which colors exist in player hand
    for card in ccVars.cc_player_hand[ccVars.cc_current_player]:

        if card.startswith("r"):
            color_red = True

        elif card.startswith("y"):
            color_yellow = True

        elif card.startswith("g"):
            color_green = True

        elif card.startswith("b"):
            color_blue = True

        elif card.startswith("wi"):
            color_wish = True


        if color_red and color_yellow and color_green and color_blue and color_wish:
            break


    react_message = await ccVars.cc_player_list[ccVars.cc_current_player].send(ccLanguage.cc_please_choose_card_color_react.replace("[USER_ID]", "<@" + str(ccVars.cc_player_list[ccVars.cc_current_player].id) + ">"))
    fCU.log_In_Console("Send color-reaction to {}.".format(ccVars.cc_player_list[ccVars.cc_current_player].name), "COLOR-REACT", "inf")


    #Set vars
    ccVars.cc_player_lay_card_reacting = ccVars.cc_player_list[ccVars.cc_current_player]
    ccVars.cc_lay_card_react_message = react_message
    ccVars.cc_next_react_is_number = False



    #Add reactions
    if color_red:
        try:
            await react_message.add_reaction("🟥")
        except:
            pass
        
        ccVars.cc_lay_card_possible_colors.append("🟥".encode('unicode-escape').decode('ASCII'))
    
    if color_yellow:
        try:
            await react_message.add_reaction("🟨")
        except:
            pass

        ccVars.cc_lay_card_possible_colors.append("🟨".encode('unicode-escape').decode('ASCII'))
    
    if color_green:
        try:
            await react_message.add_reaction("🟩")
        except:
            pass

        ccVars.cc_lay_card_possible_colors.append("🟩".encode('unicode-escape').decode('ASCII'))
    
    if color_blue:
        try:
            await react_message.add_reaction("🟦")
        except:
            pass

        ccVars.cc_lay_card_possible_colors.append("🟦".encode('unicode-escape').decode('ASCII'))
    
    if color_wish:
        try:
            await react_message.add_reaction("⬛")
        except:
            pass

        ccVars.cc_lay_card_possible_colors.append("⬛".encode('unicode-escape').decode('ASCII'))



    if ccVars.cc_player_is_suspend == True:

        try:
            await react_message.add_reaction("🚫")
        except:
            pass

        ccVars.cc_lay_card_possible_colors.append("🚫".encode('unicode-escape').decode('ASCII'))


    elif ccVars.cc_plus_card_amount > 0:
        
        try:
            await react_message.add_reaction("⤵️")
        except:
            pass

        ccVars.cc_lay_card_possible_colors.append("⤵️".encode('unicode-escape').decode('ASCII'))


    else:

        try:
            await react_message.add_reaction("➕")
        except:
            pass

        ccVars.cc_lay_card_possible_colors.append("➕".encode('unicode-escape').decode('ASCII'))




def player_can_lay_cards_str(player_hand, ccVars, ccLanguage):

    if ccVars.cc_plus_card_amount > 0:
        return player_can_counter_plus_card_str(ccVars, ccLanguage)

    if ccVars.cc_player_is_suspend and ccVars.cc_suspended_player_can_lay:
        return ccLanguage.cc_suspend_player_must_counter

    elif ccVars.cc_player_is_suspend and not ccVars.cc_suspended_player_can_lay:
        return ccLanguage.cc_suspend_player_cant_lay_direct_chat

    elif player_can_lay_cards(player_hand, ccVars):
        return ccLanguage.cc_game_player_can_lay

    else:
        return ccLanguage.cc_game_player_cant_lay


def player_can_lay_cards(player_hand, ccVars):

    can_lay = False

    mid_card = str(ccVars.cc_current_mid_card).split(":")

    for card in player_hand:

        split_card = str(card).split(":")

        if split_card[0] == mid_card[0] or split_card[1] == mid_card[1] or split_card[0] == "wi" or mid_card[0] == "wi" and split_card[0] == ccVars.cc_current_wish_color:

            can_lay = True
            
            break

    return can_lay


def reset_vars(ccVars):

    ccVars.cc_current_mid_card = ""

    ccVars.cc_current_wish_color = ""

    ccVars.cc_player_list = []
    ccVars.cc_player_display_list = ""
    ccVars.cc_player_hand = []
    ccVars.cc_player_str_hand = []

    ccVars.cc_current_player = 0

    ccVars.cc_is_running = False
    ccVars.cc_is_reversed = False


    ccVars.cc_is_lay_card_reacting = False
    ccVars.cc_next_react_is_number = False
    ccVars.cc_player_lay_card_reacting = None
    ccVars.cc_lay_card_react_message = None
    ccVars.cc_lay_card_possible_colors = []
    ccVars.cc_lay_card_possible_numbers = []
    ccVars.cc_lay_card_react_choosed_color = ""


    ccVars.cc_is_wish_reacting = False
    ccVars.cc_player_wish_reacting = None
    ccVars.cc_wish_react_message = None
    ccVars.cc_wish_react_card_num = None


    ccVars.cc_card_messages = []
    ccVars.cc_player_card_str = []


    ccVars.cc_rotate_player_hands = False


    ccVars.cc_player_is_suspend = False
    ccVars.cc_suspended_player_can_lay = False


    ccVars.cc_plus_card_amount = 0
    ccVars.cc_plus_player_can_lay = False
    ccVars.cc_plus_print = False

    ccVars.cc_wish_next_player_get_cards = False


def str_player_has_cc(player_has_cc, previous_player_name, ccLanguage):

    if player_has_cc:
        return ccLanguage.cc_game_player_has_cc.replace("[PLAYER_NAME]", previous_player_name)

    else:
        return ""


def next_player(ccVars):

    if ccVars.cc_is_reversed:

        if ccVars.cc_current_player == 0:
            ccVars.cc_current_player = (len(ccVars.cc_player_list) - 1)

        else:
            ccVars.cc_current_player -= 1

    else:

        if ccVars.cc_current_player == (len(ccVars.cc_player_list) - 1):
            ccVars.cc_current_player = 0

        else:
            ccVars.cc_current_player += 1


def check_if_player_won(ccVars):

    if len(ccVars.cc_player_hand[ccVars.cc_current_player]) == 0:
        return True

    else:
        return False


def check_if_player_has_cc(ccVars):

    if len(ccVars.cc_player_hand[ccVars.cc_current_player]) == 1:
        return True

    else:
        return False


def get_str_player_list(cc_player_list):

    cc_str_player_list = ""

    for player in cc_player_list:
        cc_str_player_list += player.name + ", "

    cc_str_player_list = cc_str_player_list[:-2]


def get_direction_str(ccVars):

    if ccVars.cc_is_reversed == True:

        out = "◀️"

    else:

        out = "▶️"

    return out


def emoji_to_color(emoji):

    if emoji == "🟥":
        return "r"

    elif emoji == "🟦":
        return "b"

    elif emoji == "🟩":
        return "g"

    elif emoji == "🟨":
        return "y"

    elif emoji == "⬛":
        return "wi"

    else:
        fCU.log_In_Console("A emoji could not be converted into a color!", "EMOJI-COLOR", "err")
        return ""


def emoji_to_number(emoji):

    if emoji == "1️⃣":
        return "1"

    elif emoji == "2️⃣":
        return "2"

    elif emoji == "3️⃣":
        return "3"

    elif emoji == "4️⃣":
        return "4"

    elif emoji == "5️⃣":
        return "5"

    elif emoji == "6️⃣":
        return "6"

    elif emoji == "7️⃣":
        return "7"

    elif emoji == "8️⃣":
        return "8"

    elif emoji == "9️⃣": 
        return "9"

    elif emoji == "🔄":
        return "🔄"

    elif emoji == "🔂":
        return "🔂"    

    elif emoji == "🚫":
        return "🚫"  

    elif emoji == "❌":
        return "❌"  

    elif emoji == "⏫":
        return "⏫"  

    elif emoji == "🔳":
        return "🔳"

    elif emoji == "❓":
        return "❓"

    elif emoji == "👨‍👨‍👧‍👦":
        return "👨‍👨‍👧‍👦"

    elif emoji == "⤵️":
        return "⤵️"

    elif emoji == "🔙":
        return "🔙"

    else:
        fCU.log_In_Console("A emoji could not be converted into a number!", "COLOR-EMOJI", "err")
        return ""


def number_to_emoji(number):

    if number == "1":
        return "1️⃣"

    elif number == "2":
        return "2️⃣"

    elif number == "3":
        return "3️⃣"

    elif number == "4":
        return "4️⃣"

    elif number == "5":
        return "5️⃣"

    elif number == "6":
        return "6️⃣"

    elif number == "7":
        return "7️⃣"

    elif number == "8":
        return "8️⃣"

    elif number == "9": 
        return "9️⃣"

    elif number == "🔄":
        return "🔄"

    elif number == "🔂":
        return "🔂"    

    elif number == "🚫":
        return "🚫"  

    elif number == "❌":
        return "❌"  

    elif number == "⏫":
        return "⏫"  

    elif number == "🔳":
        return "🔳"

    elif number == "❓":
        return "❓"

    elif number == "👨‍👨‍👧‍👦":
        return "👨‍👨‍👧‍👦"

    elif number == "⤵️":
        return "⤵️"

    elif number == "🔙":
        return "🔙"

    else:
        print(number)
        fCU.log_In_Console("A number could not be converted into an emoji!", "COLOR-EMOJI", "err")
        return ""