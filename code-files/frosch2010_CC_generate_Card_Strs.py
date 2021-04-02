import frosch2010_Console_Utils as fCU



def color_to_emoji(color):

    if color == "r":
        return "🟥"

    elif color == "b":
        return "🟦"

    elif color == "g":
        return "🟩"

    elif color == "y":
        return "🟨"

    else:
        fCU.log_In_Console("A color could not be converted into an emoji!", "COLOR-EMOJI", "err")
        return ""



def generate_mid_card_str(card, ccVars):

    str_cc_Mid_Card = ""

    if card.startswith("wi"):

        wish_card_template = ccVars.cc_wish_card_template.split("|")

        str_cc_Mid_Card += "\n\n" + wish_card_template[0]

        str_cc_Mid_Card += "\n" + wish_card_template[1].replace("  **NUM**  ", card.split(":")[1]).replace("COUNT", color_to_emoji(ccVars.cc_current_wish_color) + " ist gewünscht worden.")

        str_cc_Mid_Card += "\n" + wish_card_template[2]

    else:

        #ROT
        if card.startswith("r"):

            red_card_template = ccVars.cc_red_card_template.split("|")

            str_cc_Mid_Card += "\n\n" + red_card_template[0]

            if card.split(":")[1] == "🔄" or card.split(":")[1] == "🔂" or card.split(":")[1] == "🚫" or card.split(":")[1] == "❌":

                str_cc_Mid_Card += "\n" + red_card_template[1].replace("  **NUM**  ", card.split(":")[1]).replace("COUNT", "")

            elif card.split(":")[1] == "⏫":

                str_cc_Mid_Card += "\n" + red_card_template[1].replace("  **NUM**  ", card.split(":")[1]).replace("COUNT", "+" + str(ccVars.cc_plus_card_amount))

            else:

                str_cc_Mid_Card += "\n" + red_card_template[1].replace("NUM", card.split(":")[1]).replace("COUNT", "")

            str_cc_Mid_Card += "\n" + red_card_template[2]

        #Blau
        elif card.startswith("b"):
            
            blue_card_template = ccVars.cc_blue_card_template.split("|")

            str_cc_Mid_Card += "\n\n" + blue_card_template[0]

            if card.split(":")[1] == "🔄" or card.split(":")[1] == "🔂" or card.split(":")[1] == "🚫" or card.split(":")[1] == "❌":

                str_cc_Mid_Card += "\n" + blue_card_template[1].replace("  **NUM**  ", card.split(":")[1]).replace("COUNT", "")

            elif card.split(":")[1] == "⏫":

                str_cc_Mid_Card += "\n" + blue_card_template[1].replace("  **NUM**  ", card.split(":")[1]).replace("COUNT", "+" + str(ccVars.cc_plus_card_amount))

            else:

                str_cc_Mid_Card += "\n" + blue_card_template[1].replace("NUM", card.split(":")[1]).replace("COUNT", "")

            str_cc_Mid_Card += "\n" + blue_card_template[2]

        #Gruen
        elif card.startswith("g"):

            green_card_template = ccVars.cc_green_card_template.split("|")

            str_cc_Mid_Card += "\n\n"+ green_card_template[0]

            if card.split(":")[1] == "🔄" or card.split(":")[1] == "🔂" or card.split(":")[1] == "🚫" or card.split(":")[1] == "❌":

                str_cc_Mid_Card += "\n" + green_card_template[1].replace("  **NUM**  ", card.split(":")[1]).replace("COUNT", "")

            elif card.split(":")[1] == "⏫":

                str_cc_Mid_Card += "\n" + green_card_template[1].replace("  **NUM**  ", card.split(":")[1]).replace("COUNT", "+" + str(ccVars.cc_plus_card_amount))

            else:

                str_cc_Mid_Card += "\n" + green_card_template[1].replace("NUM", card.split(":")[1]).replace("COUNT", "")

            str_cc_Mid_Card += "\n" + green_card_template[2]

        #Gelb
        elif card.startswith("y"):

            yellow_card_template = ccVars.cc_yellow_card_template.split("|")

            str_cc_Mid_Card += "\n\n" + yellow_card_template[0]

            if card.split(":")[1] == "🔄" or card.split(":")[1] == "🔂" or card.split(":")[1] == "🚫" or card.split(":")[1] == "❌":

                str_cc_Mid_Card += "\n" + yellow_card_template[1].replace("  **NUM**  ", card.split(":")[1]).replace("COUNT", "")

            elif card.split(":")[1] == "⏫":

                str_cc_Mid_Card += "\n" + yellow_card_template[1].replace("  **NUM**  ", card.split(":")[1]).replace("COUNT", "+" + str(ccVars.cc_plus_card_amount))

            else:

                str_cc_Mid_Card += "\n" + yellow_card_template[1].replace("NUM", card.split(":")[1]).replace("COUNT", "")

            str_cc_Mid_Card += "\n" + yellow_card_template[2]

        else:

            str_cc_Mid_Card = "Sorry, das hätte nicht passieren dürfen! - Fehler: send_cc_player_karten"

    return str_cc_Mid_Card



def get_card_index_str(card_index):

    if card_index >= 12 or card_index == 10:
        return str(card_index) + ":**  "

    elif card_index == 11:
        return str(card_index) + ":**   "
        
    elif card_index == 1:
        return str(card_index) + ":**     "
            
    else:
        return str(card_index) + ":**    "



def generate_card_amount_str(amount):

    try:
        card_amount = int(amount)

    except:
        fCU.log_In_Console("Failed convert card amount to int.", "GENERATE-AMOUNT", "err")
        return "x " + amount


    if card_amount > 1:
        return "**x " + amount + "**"
    else:
        return "x " + amount



def generate_player_str_hand(player_hand, player_index, ccVars, ccLanguage):

    added_player_output_cards = []
    str_player_cards_output = ""    

    player_card_output = []

    for card in player_hand:

        if card in added_player_output_cards:
            continue

        if player_hand.count(card) > 1:

            player_card_output.append(str(player_hand.count(card)) + "*" + card)

            added_player_output_cards.append(card)

        else:

            player_card_output.append("1*" + card)
            

    if len(player_card_output) == 1:

        split_card = str(player_card_output[0]).split("*")
        split_card_mid_field = split_card[1].split(":")[1]

        #Rot
        if split_card[1].startswith("r"):

            red_card_template = ccVars.cc_red_card_template.split("|")

            str_player_cards_output += "\n\n" + "        " + red_card_template[0]

            if split_card_mid_field == "⏫" or split_card_mid_field == "🔄" or split_card_mid_field == "🔂" or split_card_mid_field == "🚫" or split_card =="❌":

                str_player_cards_output += "\n**1:**    " + red_card_template[1].replace("  **NUM**  ", split_card_mid_field).replace("COUNT", generate_card_amount_str(split_card[0]))

            else:

                str_player_cards_output += "\n**1:**     " + red_card_template[1].replace("NUM", split_card_mid_field).replace("COUNT", generate_card_amount_str(split_card[0]))

            str_player_cards_output += "\n        " + red_card_template[2]

        #Blau
        elif split_card[1].startswith("b"):
            
            blue_card_template = ccVars.cc_blue_card_template.split("|")

            str_player_cards_output += "\n\n" + "        " + blue_card_template[0]

            if split_card_mid_field == "⏫" or split_card_mid_field == "🔄" or split_card_mid_field == "🔂" or split_card_mid_field == "🚫" or split_card =="❌":

                str_player_cards_output += "\n**1:**    " + blue_card_template[1].replace("  **NUM**  ", split_card_mid_field).replace("COUNT", generate_card_amount_str(split_card[0]))

            else:

                str_player_cards_output += "\n**1:**     " + blue_card_template[1].replace("NUM", split_card_mid_field).replace("COUNT", generate_card_amount_str(split_card[0]))

            str_player_cards_output += "\n        " + blue_card_template[2]

        #Gruen
        elif split_card[1].startswith("g"):

            green_card_template = ccVars.cc_green_card_template.split("|")

            str_player_cards_output += "\n\n" + "        " + green_card_template[0]

            if split_card_mid_field == "⏫" or split_card_mid_field == "🔄" or split_card_mid_field == "🔂" or split_card_mid_field == "🚫" or split_card =="❌":

                str_player_cards_output += "\n**1:**    " + green_card_template[1].replace("  **NUM**  ", split_card_mid_field).replace("COUNT", generate_card_amount_str(split_card[0]))

            else:

                str_player_cards_output += "\n**1:**     " + green_card_template[1].replace("NUM", split_card_mid_field).replace("COUNT", generate_card_amount_str(split_card[0]))

            str_player_cards_output += "\n        " + green_card_template[2]

        #Gelb
        elif split_card[1].startswith("y"):

            yellow_card_template = ccVars.cc_yellow_card_template.split("|")

            str_player_cards_output += "\n\n" + "        " + yellow_card_template[0]

            if split_card_mid_field == "⏫" or split_card_mid_field == "🔄" or split_card_mid_field == "🔂" or split_card_mid_field == "🚫" or split_card =="❌":

                str_player_cards_output += "\n**1:**    " + yellow_card_template[1].replace("  **NUM**  ", split_card_mid_field).replace("COUNT", generate_card_amount_str(split_card[0]))

            else:

                str_player_cards_output += "\n**1:**     " + yellow_card_template[1].replace("NUM", split_card_mid_field).replace("COUNT", generate_card_amount_str(split_card[0]))

            str_player_cards_output += "\n        " + yellow_card_template[2]

        #Wunsch
        elif split_card[1].startswith("wi"):

            wish_card_template = ccVars.cc_wish_card_template.split("|")

            str_player_cards_output += "\n\n" + "        " + wish_card_template[0]

            if split_card_mid_field == "❓" or split_card_mid_field == "👨‍👨‍👧‍👦" or split_card_mid_field == "🔳":

                str_player_cards_output += "\n**1:**    " + wish_card_template[1].replace("  **NUM**  ", split_card_mid_field).replace("COUNT", generate_card_amount_str(split_card[0]))

            else:

                str_player_cards_output += "\n**1:**    " + wish_card_template[1].replace("NUM", split_card_mid_field).replace("COUNT", generate_card_amount_str(split_card[0]))

            str_player_cards_output += "\n        " + wish_card_template[2]

        else:

            str_player_cards_output = "An error occurred while generating a player hand."
            fCU.log_In_Console("An error occurred while generating a player hand.", "GENERATE-HAND", "err")

            return str_player_cards_output


    else:

        for card_index in range(0, len(player_card_output), 2):

            isLastCard = False

            if card_index == (len(player_card_output) - 1):

                isLastCard = True


            split_player_output_card_one = str(player_card_output[card_index]).split("*")
            split_player_output_card_one_mid_field = split_player_output_card_one[1].split(":")[1]

            if isLastCard == True:

                #Rot
                if split_player_output_card_one[1].startswith("r"):

                    red_card_template = ccVars.cc_red_card_template.split("|")

                    str_player_cards_output += "\n\n" + "        " + red_card_template[0]

                    if split_player_output_card_one_mid_field == "⏫" or split_player_output_card_one_mid_field == "🔄" or split_player_output_card_one_mid_field == "🔂" or split_player_output_card_one_mid_field == "🚫" or split_player_output_card_one_mid_field =="❌":

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + red_card_template[1].replace("  **NUM**  ", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    else:

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + red_card_template[1].replace("NUM", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    str_player_cards_output += "\n        " + red_card_template[2]

                #Blau
                elif split_player_output_card_one[1].startswith("b"):
                    
                    blue_card_template = ccVars.cc_blue_card_template.split("|")

                    str_player_cards_output += "\n\n" + "        " + blue_card_template[0]

                    if split_player_output_card_one_mid_field == "⏫" or split_player_output_card_one_mid_field == "🔄" or split_player_output_card_one_mid_field == "🔂" or split_player_output_card_one_mid_field == "🚫" or split_player_output_card_one_mid_field =="❌":

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + blue_card_template[1].replace("  **NUM**  ", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    else:

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + blue_card_template[1].replace("NUM", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    str_player_cards_output += "\n        " + blue_card_template[2]

                #Gruen
                elif split_player_output_card_one[1].startswith("g"):

                    green_card_template = ccVars.cc_green_card_template.split("|")

                    str_player_cards_output += "\n\n" + "        " + green_card_template[0]

                    if split_player_output_card_one_mid_field == "⏫" or split_player_output_card_one_mid_field == "🔄" or split_player_output_card_one_mid_field == "🔂" or split_player_output_card_one_mid_field == "🚫" or split_player_output_card_one_mid_field =="❌":

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + green_card_template[1].replace("  **NUM**  ", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    else:

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + green_card_template[1].replace("NUM", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    str_player_cards_output += "\n        " + green_card_template[2]

                #Gelb
                elif split_player_output_card_one[1].startswith("y"):

                    yellow_card_template = ccVars.cc_yellow_card_template.split("|")

                    str_player_cards_output += "\n\n" + "        " + yellow_card_template[0]

                    if split_player_output_card_one_mid_field == "⏫" or split_player_output_card_one_mid_field == "🔄" or split_player_output_card_one_mid_field == "🔂" or split_player_output_card_one_mid_field == "🚫" or split_player_output_card_one_mid_field =="❌":

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + yellow_card_template[1].replace("  **NUM**  ", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    else:

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + yellow_card_template[1].replace("NUM", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    str_player_cards_output += "\n        " + yellow_card_template[2]

                #Wunsch
                elif split_player_output_card_one[1].startswith("wi"):

                    wish_card_template = ccVars.cc_wish_card_template.split("|")

                    str_player_cards_output += "\n\n" + "        " + wish_card_template[0]

                    if split_player_output_card_one_mid_field == "👨‍👨‍👧‍👦" or split_player_output_card_one_mid_field == "🔳" or split_player_output_card_one_mid_field == "❓":

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + wish_card_template[1].replace("  **NUM**  ", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    else:

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + wish_card_template[1].replace("NUM", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    str_player_cards_output += "\n        " + wish_card_template[2]

                else:

                    str_player_cards_output = "An error occurred while generating a player hand."
                    fCU.log_In_Console("An error occurred while generating a player hand.", "GENERATE-HAND", "err")

                    return str_player_cards_output

            else:

                split_player_output_card_two = str(player_card_output[card_index + 1]).split("*")
                split_player_output_card_two_mid_field = split_player_output_card_two[1].split(":")[1]

                #Oben Karte Links
                if split_player_output_card_one[1].startswith("r"):

                    str_player_cards_output += "\n\n" + "        " + ccVars.cc_red_card_template.split("|")[0]

                elif split_player_output_card_one[1].startswith("b"):
                    
                    str_player_cards_output += "\n\n" + "        " + ccVars.cc_blue_card_template.split("|")[0]

                elif split_player_output_card_one[1].startswith("g"):

                    str_player_cards_output += "\n\n" + "        " + ccVars.cc_green_card_template.split("|")[0]

                elif split_player_output_card_one[1].startswith("y"):

                    str_player_cards_output += "\n\n" + "        " + ccVars.cc_yellow_card_template.split("|")[0]

                elif split_player_output_card_one[1].startswith("wi"):

                    str_player_cards_output += "\n\n" + "        " + ccVars.cc_wish_card_template.split("|")[0]

                else:

                    str_player_cards_output = "An error occurred while generating a player hand."
                    fCU.log_In_Console("An error occurred while generating a player hand.", "GENERATE-HAND", "err")

                    return str_player_cards_output

                #Oben Karte Rechts
                if split_player_output_card_two[1].startswith("r"):

                    str_player_cards_output += "                        " + ccVars.cc_red_card_template.split("|")[0]

                elif split_player_output_card_two[1].startswith("b"):
                    
                    str_player_cards_output += "                        " + ccVars.cc_blue_card_template.split("|")[0]

                elif split_player_output_card_two[1].startswith("g"):

                    str_player_cards_output += "                        " + ccVars.cc_green_card_template.split("|")[0]

                elif split_player_output_card_two[1].startswith("y"):

                    str_player_cards_output += "                        " + ccVars.cc_yellow_card_template.split("|")[0]

                elif split_player_output_card_two[1].startswith("wi"):

                    str_player_cards_output += "                        " + ccVars.cc_wish_card_template.split("|")[0]

                else:

                    str_player_cards_output = "An error occurred while generating a player hand."
                    fCU.log_In_Console("An error occurred while generating a player hand.", "GENERATE-HAND", "err")

                    return str_player_cards_output


                #Mitte Karte Links
                if split_player_output_card_one_mid_field == "⏫" or split_player_output_card_one_mid_field == "🔄" or split_player_output_card_one_mid_field == "🔂" or split_player_output_card_one_mid_field == "🔳" or split_player_output_card_one_mid_field == "❓" or split_player_output_card_one_mid_field == "👨‍👨‍👧‍👦" or split_player_output_card_one_mid_field == "🚫" or split_player_output_card_one_mid_field =="❌":
                    
                    if split_player_output_card_one[1].startswith("r"):

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + ccVars.cc_red_card_template.split("|")[1].replace("  **NUM**  ", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    elif split_player_output_card_one[1].startswith("b"):
                        
                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + ccVars.cc_blue_card_template.split("|")[1].replace("  **NUM**  ", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    elif split_player_output_card_one[1].startswith("g"):

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + ccVars.cc_green_card_template.split("|")[1].replace("  **NUM**  ", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    elif split_player_output_card_one[1].startswith("y"):

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + ccVars.cc_yellow_card_template.split("|")[1].replace("  **NUM**  ", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    elif split_player_output_card_one[1].startswith("wi"):

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + ccVars.cc_wish_card_template.split("|")[1].replace("  **NUM**  ", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    else:

                        str_player_cards_output = "An error occurred while generating a player hand."
                        fCU.log_In_Console("An error occurred while generating a player hand.", "GENERATE-HAND", "err")

                        return str_player_cards_output

                else:

                    if split_player_output_card_one[1].startswith("r"):

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + ccVars.cc_red_card_template.split("|")[1].replace("NUM", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    elif split_player_output_card_one[1].startswith("b"):
                        
                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + ccVars.cc_blue_card_template.split("|")[1].replace("NUM", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    elif split_player_output_card_one[1].startswith("g"):

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + ccVars.cc_green_card_template.split("|")[1].replace("NUM", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    elif split_player_output_card_one[1].startswith("y"):

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + ccVars.cc_yellow_card_template.split("|")[1].replace("NUM", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    elif split_player_output_card_one[1].startswith("wi"):

                        str_player_cards_output += "\n**" + get_card_index_str((card_index + 1)) + ccVars.cc_wish_card_template.split("|")[1].replace("NUM", split_player_output_card_one_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_one[0]))

                    else:

                        str_player_cards_output = "An error occurred while generating a player hand."
                        fCU.log_In_Console("An error occurred while generating a player hand.", "GENERATE-HAND", "err")

                        return str_player_cards_output

                #Mitte Karte Rechts
                if split_player_output_card_two_mid_field == "⏫" or split_player_output_card_two_mid_field == "🔄" or split_player_output_card_two_mid_field == "🔂" or split_player_output_card_two_mid_field == "🔳" or split_player_output_card_two_mid_field == "❓" or split_player_output_card_two_mid_field == "👨‍👨‍👧‍👦" or split_player_output_card_two_mid_field == "🚫"  or split_player_output_card_two_mid_field =="❌":
                    
                    if split_player_output_card_two[1].startswith("r"):

                        str_player_cards_output += "        **" + get_card_index_str((card_index + 2)) + ccVars.cc_red_card_template.split("|")[1].replace("  **NUM**  ", split_player_output_card_two_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_two[0]))

                    elif split_player_output_card_two[1].startswith("b"):
                        
                        str_player_cards_output += "        **" + get_card_index_str((card_index + 2)) + ccVars.cc_blue_card_template.split("|")[1].replace("  **NUM**  ", split_player_output_card_two_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_two[0]))

                    elif split_player_output_card_two[1].startswith("g"):

                        str_player_cards_output += "        **" + get_card_index_str((card_index + 2)) + ccVars.cc_green_card_template.split("|")[1].replace("  **NUM**  ", split_player_output_card_two_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_two[0]))

                    elif split_player_output_card_two[1].startswith("y"):

                        str_player_cards_output += "        **" + get_card_index_str((card_index + 2)) + ccVars.cc_yellow_card_template.split("|")[1].replace("  **NUM**  ", split_player_output_card_two_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_two[0]))

                    elif split_player_output_card_two[1].startswith("wi"):

                        str_player_cards_output += "        **" + get_card_index_str((card_index + 2)) + ccVars.cc_wish_card_template.split("|")[1].replace("  **NUM**  ", split_player_output_card_two_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_two[0]))

                    else:

                        str_player_cards_output = "An error occurred while generating a player hand."
                        fCU.log_In_Console("An error occurred while generating a player hand.", "GENERATE-HAND", "err")

                        return str_player_cards_output

                else:

                    if split_player_output_card_two[1].startswith("r"):

                        str_player_cards_output += "        **" + get_card_index_str((card_index + 2)) + ccVars.cc_red_card_template.split("|")[1].replace("NUM", split_player_output_card_two_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_two[0]))

                    elif split_player_output_card_two[1].startswith("b"):
                        
                        str_player_cards_output += "        **" + get_card_index_str((card_index + 2)) + ccVars.cc_blue_card_template.split("|")[1].replace("NUM", split_player_output_card_two_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_two[0]))

                    elif split_player_output_card_two[1].startswith("g"):

                        str_player_cards_output += "        **" + get_card_index_str((card_index + 2)) + ccVars.cc_green_card_template.split("|")[1].replace("NUM", split_player_output_card_two_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_two[0]))

                    elif split_player_output_card_two[1].startswith("y"):

                        str_player_cards_output += "        **" + get_card_index_str((card_index + 2)) + ccVars.cc_yellow_card_template.split("|")[1].replace("NUM", split_player_output_card_two_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_two[0]))

                    elif split_player_output_card_two[1].startswith("wi"):

                        str_player_cards_output += "        **" + get_card_index_str((card_index + 2)) + ccVars.cc_wish_card_template.split("|")[1].replace("NUM", split_player_output_card_two_mid_field).replace("COUNT", generate_card_amount_str(split_player_output_card_two[0]))

                    else:

                        str_player_cards_output = "An error occurred while generating a player hand."
                        fCU.log_In_Console("An error occurred while generating a player hand.", "GENERATE-HAND", "err")

                        return str_player_cards_output


                #Unten Karte Links
                if split_player_output_card_one[1].startswith("r"):

                    str_player_cards_output += "\n        " + ccVars.cc_red_card_template.split("|")[2]

                elif split_player_output_card_one[1].startswith("b"):
                    
                    str_player_cards_output += "\n        " + ccVars.cc_blue_card_template.split("|")[2]

                elif split_player_output_card_one[1].startswith("g"):

                    str_player_cards_output += "\n        " + ccVars.cc_green_card_template.split("|")[2]

                elif split_player_output_card_one[1].startswith("y"):

                    str_player_cards_output += "\n        " + ccVars.cc_yellow_card_template.split("|")[2]

                elif split_player_output_card_one[1].startswith("wi"):

                    str_player_cards_output += "\n        " + ccVars.cc_wish_card_template.split("|")[2]

                else:

                    str_player_cards_output = "An error occurred while generating a player hand."
                    fCU.log_In_Console("An error occurred while generating a player hand.", "GENERATE-HAND", "err")

                    return str_player_cards_output

                #Unten Karte Rechts
                if split_player_output_card_two[1].startswith("r"):

                    str_player_cards_output += "                        " + ccVars.cc_red_card_template.split("|")[2] + "|.|"

                elif split_player_output_card_two[1].startswith("b"):
                    
                    str_player_cards_output += "                        " + ccVars.cc_blue_card_template.split("|")[2] + "|.|"

                elif split_player_output_card_two[1].startswith("g"):

                    str_player_cards_output += "                        " + ccVars.cc_green_card_template.split("|")[2] + "|.|"

                elif split_player_output_card_two[1].startswith("y"):

                    str_player_cards_output += "                        " + ccVars.cc_yellow_card_template.split("|")[2] + "|.|"

                elif split_player_output_card_two[1].startswith("wi"):

                    str_player_cards_output += "                        " + ccVars.cc_wish_card_template.split("|")[2] + "|.|"

                else:

                    str_player_cards_output = "An error occurred while generating a player hand."
                    fCU.log_In_Console("An error occurred while generating a player hand.", "GENERATE-HAND", "err")

                    return str_player_cards_output


    ccVars.cc_player_str_hand[player_index] = player_card_output

    return str_player_cards_output