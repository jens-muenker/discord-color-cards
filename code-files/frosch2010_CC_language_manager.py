import os
import sys
import json


import frosch2010_Console_Utils as fCU
import frosch2010_CC_language_DE as fCLDE
import frosch2010_CC_language_EN as fCLEN


def setup_language(ccLanguage, ccSettings):

    fCU.log_In_Console("Load language...", "SETUP-LANG", "inf")


    if ccSettings.cc_use_language_file:

        fCU.log_In_Console("Use custom path for the language file...", "SETUP-LANG", "inf")
        cc_language_file_path = ccSettings.cc_language_file_path + "cc-language.txt"


        if not os.path.isfile(cc_language_file_path):

            fCU.log_In_Console("The language file could not be found! File will now be created...", "SETUP-LANG", "err")
            create_language_file(cc_language_file_path)

        load_language_file(cc_language_file_path, ccLanguage)

    else:

        if ccSettings.cc_discord_language.lower() == "de":

            fCU.log_In_Console("Loading german language...", "SETUP-LANG", "inf")
            load_german_language(ccLanguage)
            
            

        elif ccSettings.cc_discord_language.lower() == "en":

            fCU.log_In_Console("Loading english language...", "SETUP-LANG", "inf")
            load_english_language(ccLanguage)

        else:

            fCU.log_In_Console("The language specified in the settings could not be found! English is used now.", "SETUP-LANG", "err")
            load_english_language(ccLanguage)


        fCU.log_In_Console("Language successfully loaded.", "SETUP-LANG", "inf")



def load_english_language(ccLanguage):

    #General
    ccLanguage.cc_wrong_arguments = fCLEN.cc_language().cc_wrong_arguments
    ccLanguage.cc_wrong_game_command = fCLEN.cc_language().cc_wrong_game_command
    ccLanguage.cc_shutdown_bot = fCLEN.cc_language().cc_shutdown_bot


    #Game
    ccLanguage.cc_game_already_running = fCLEN.cc_language().cc_game_already_running
    ccLanguage.cc_cards_per_player_set_to = fCLEN.cc_language().cc_cards_per_player_set_to
    ccLanguage.cc_no_game_running = fCLEN.cc_language().cc_no_game_running
    ccLanguage.cc_user_already_joined = fCLEN.cc_language().cc_user_already_joined
    ccLanguage.cc_user_joined_game = fCLEN.cc_language().cc_user_joined_game
    ccLanguage.cc_more_players_needed = fCLEN.cc_language().cc_more_players_needed
    ccLanguage.cc_user_started_game = fCLEN.cc_language().cc_user_started_game
    ccLanguage.cc_user_not_part = fCLEN.cc_language().cc_user_not_part
    ccLanguage.cc_player_won = fCLEN.cc_language().cc_player_won

    ccLanguage.cc_user_leave_no_part = fCLEN.cc_language().cc_user_leave_no_part
    ccLanguage.cc_game_end_because_user_left = fCLEN.cc_language().cc_game_end_because_user_left
    ccLanguage.cc_user_left = fCLEN.cc_language().cc_user_left
    ccLanguage.cc_user_cant_leave_his_turn = fCLEN.cc_language().cc_user_cant_leave_his_turn

    ccLanguage.cc_user_no_turn = fCLEN.cc_language().cc_user_no_turn
    ccLanguage.cc_card_not_exist = fCLEN.cc_language().cc_card_not_exist
    ccLanguage.cc_user_cant_lay_card = fCLEN.cc_language().cc_user_cant_lay_card
    ccLanguage.cc_user_your_turn = fCLEN.cc_language().cc_user_your_turn

    ccLanguage.cc_wish_without_color = fCLEN.cc_language().cc_wish_without_color
    ccLanguage.cc_wish_unknown_color = fCLEN.cc_language().cc_wish_unknown_color

    ccLanguage.cc_input_only_numbers = fCLEN.cc_language().cc_input_only_numbers
    ccLanguage.cc_input_no_number_arg = fCLEN.cc_language().cc_input_no_number_arg

    ccLanguage.cc_game_stopped_by = fCLEN.cc_language().cc_game_stopped_by
    ccLanguage.cc_game_cant_stopped = fCLEN.cc_language().cc_game_cant_stopped
    ccLanguage.cc_game_player_has_cc = fCLEN.cc_language().cc_game_player_has_cc
    ccLanguage.cc_game_player_can_lay = fCLEN.cc_language().cc_game_player_can_lay
    ccLanguage.cc_game_player_cant_lay = fCLEN.cc_language().cc_game_player_cant_lay

    ccLanguage.cc_please_choose_wish_color_react = fCLEN.cc_language().cc_please_choose_wish_color_react
    ccLanguage.cc_please_choose_card_color_react = fCLEN.cc_language().cc_please_choose_card_color_react
    ccLanguage.cc_please_choose_card_num_react = fCLEN.cc_language().cc_please_choose_card_num_react

    ccLanguage.cc_false_choose_color_react = fCLEN.cc_language().cc_false_choose_color_react
    ccLanguage.cc_false_choose_number_react = fCLEN.cc_language().cc_false_choose_number_react

    ccLanguage.cc_no_kick_user = fCLEN.cc_language().cc_no_kick_user
    ccLanguage.cc_kick_user_isnt_player = fCLEN.cc_language().cc_kick_user_isnt_player
    ccLanguage.cc_cant_kick_current_player = fCLEN.cc_language().cc_cant_kick_current_player
    ccLanguage.cc_user_kicked = fCLEN.cc_language().cc_user_kicked


    #Suspend
    ccLanguage.cc_suspend_player_cant_lay_direct_chat = fCLEN.cc_language().cc_suspend_player_cant_lay_direct_chat
    ccLanguage.cc_suspend_player_cant_lay = fCLEN.cc_language().cc_suspend_player_cant_lay
    ccLanguage.cc_suspend_player_false_card = fCLEN.cc_language().cc_suspend_player_false_card
    ccLanguage.cc_suspend_player_must_counter = fCLEN.cc_language().cc_suspend_player_must_counter

    ccLanguage.cc_suspend_player_counter_cant_get_new_cards = fCLEN.cc_language().cc_suspend_player_counter_cant_get_new_cards
    ccLanguage.cc_suspend_player_cant_get_new_cards = fCLEN.cc_language().cc_suspend_player_cant_get_new_cards

    ccLanguage.cc_suspend_player_want_sit_out = fCLEN.cc_language().cc_suspend_player_want_sit_out
    ccLanguage.cc_suspend_player_cant_sit_out = fCLEN.cc_language().cc_suspend_player_cant_sit_out
    ccLanguage.cc_suspend_player_cant_skip = fCLEN.cc_language().cc_suspend_player_cant_skip


    #Plus-Card
    ccLanguage.cc_plus_card_player_can_lay = fCLEN.cc_language().cc_plus_card_player_can_lay
    ccLanguage.cc_plus_card_player_cant_lay = fCLEN.cc_language().cc_plus_card_player_cant_lay
    ccLanguage.cc_plus_card_player_lay_false_card = fCLEN.cc_language().cc_plus_card_player_lay_false_card
    ccLanguage.cc_plus_card_player_cant_lay_false_card = fCLEN.cc_language().cc_plus_card_player_cant_lay_false_card

    ccLanguage.cc_plus_card_player_cant_take = fCLEN.cc_language().cc_plus_card_player_cant_take
    ccLanguage.cc_plus_card_player_take = fCLEN.cc_language().cc_plus_card_player_take
    ccLanguage.cc_plus_card_player_cant_skip = fCLEN.cc_language().cc_plus_card_player_cant_skip

    ccLanguage.cc_plus_card_player_cant_get_new_cards = fCLEN.cc_language().cc_plus_card_player_cant_get_new_cards
    ccLanguage.cc_plus_card_player_counter_cant_get_new_cards = fCLEN.cc_language().cc_plus_card_player_counter_cant_get_new_cards



    #Card-STR
    ccLanguage.cc_timer_action_sit_out = fCLEN.cc_language().cc_timer_action_sit_out
    ccLanguage.cc_timer_action_take_plus_cards = fCLEN.cc_language().cc_timer_action_take_plus_cards
    ccLanguage.cc_your_cards = fCLEN.cc_language().cc_your_cards
    ccLanguage.cc_current_mid_card = fCLEN.cc_language().cc_current_mid_card
    ccLanguage.cc_player_sequence = fCLEN.cc_language().cc_player_sequence
    ccLanguage.cc_players_turn = fCLEN.cc_language().cc_players_turn
    ccLanguage.cc_player_laid_card = fCLEN.cc_language().cc_player_laid_card
    ccLanguage.cc_player_picked_up_card = fCLEN.cc_language().cc_player_picked_up_card


    #Voice
    ccLanguage.cc_voice_players_turn = fCLEN.cc_language().cc_voice_players_turn
    ccLanguage.cc_voice_player_won = fCLEN.cc_language().cc_voice_player_won
    ccLanguage.cc_voice_player_sit_out = fCLEN.cc_language().cc_voice_player_sit_out



def load_german_language(ccLanguage):

    #General
    ccLanguage.cc_wrong_arguments = fCLDE.cc_language().cc_wrong_arguments
    ccLanguage.cc_wrong_game_command = fCLDE.cc_language().cc_wrong_game_command
    ccLanguage.cc_shutdown_bot = fCLDE.cc_language().cc_shutdown_bot


    #Game
    ccLanguage.cc_game_already_running = fCLDE.cc_language().cc_game_already_running
    ccLanguage.cc_cards_per_player_set_to = fCLDE.cc_language().cc_cards_per_player_set_to
    ccLanguage.cc_no_game_running = fCLDE.cc_language().cc_no_game_running
    ccLanguage.cc_user_already_joined = fCLDE.cc_language().cc_user_already_joined
    ccLanguage.cc_user_joined_game = fCLDE.cc_language().cc_user_joined_game
    ccLanguage.cc_more_players_needed = fCLDE.cc_language().cc_more_players_needed
    ccLanguage.cc_user_started_game = fCLDE.cc_language().cc_user_started_game
    ccLanguage.cc_user_not_part = fCLDE.cc_language().cc_user_not_part
    ccLanguage.cc_player_won = fCLDE.cc_language().cc_player_won

    ccLanguage.cc_user_leave_no_part = fCLDE.cc_language().cc_user_leave_no_part
    ccLanguage.cc_game_end_because_user_left = fCLDE.cc_language().cc_game_end_because_user_left
    ccLanguage.cc_user_left = fCLDE.cc_language().cc_user_left
    ccLanguage.cc_user_cant_leave_his_turn = fCLDE.cc_language().cc_user_cant_leave_his_turn

    ccLanguage.cc_user_no_turn = fCLDE.cc_language().cc_user_no_turn
    ccLanguage.cc_card_not_exist = fCLDE.cc_language().cc_card_not_exist
    ccLanguage.cc_user_cant_lay_card = fCLDE.cc_language().cc_user_cant_lay_card
    ccLanguage.cc_user_your_turn = fCLDE.cc_language().cc_user_your_turn

    ccLanguage.cc_wish_without_color = fCLDE.cc_language().cc_wish_without_color
    ccLanguage.cc_wish_unknown_color = fCLDE.cc_language().cc_wish_unknown_color

    ccLanguage.cc_input_only_numbers = fCLDE.cc_language().cc_input_only_numbers
    ccLanguage.cc_input_no_number_arg = fCLDE.cc_language().cc_input_no_number_arg

    ccLanguage.cc_game_stopped_by = fCLDE.cc_language().cc_game_stopped_by
    ccLanguage.cc_game_cant_stopped = fCLDE.cc_language().cc_game_cant_stopped
    ccLanguage.cc_game_player_has_cc = fCLDE.cc_language().cc_game_player_has_cc
    ccLanguage.cc_game_player_can_lay = fCLDE.cc_language().cc_game_player_can_lay
    ccLanguage.cc_game_player_cant_lay = fCLDE.cc_language().cc_game_player_cant_lay

    ccLanguage.cc_please_choose_wish_color_react = fCLDE.cc_language().cc_please_choose_wish_color_react
    ccLanguage.cc_please_choose_card_color_react = fCLDE.cc_language().cc_please_choose_card_color_react
    ccLanguage.cc_please_choose_card_num_react = fCLDE.cc_language().cc_please_choose_card_num_react

    ccLanguage.cc_false_choose_color_react = fCLDE.cc_language().cc_false_choose_color_react
    ccLanguage.cc_false_choose_number_react = fCLDE.cc_language().cc_false_choose_number_react

    ccLanguage.cc_no_kick_user = fCLDE.cc_language().cc_no_kick_user
    ccLanguage.cc_kick_user_isnt_player = fCLDE.cc_language().cc_kick_user_isnt_player
    ccLanguage.cc_cant_kick_current_player = fCLDE.cc_language().cc_cant_kick_current_player
    ccLanguage.cc_user_kicked = fCLDE.cc_language().cc_user_kicked


    #Suspend
    ccLanguage.cc_suspend_player_cant_lay_direct_chat = fCLDE.cc_language().cc_suspend_player_cant_lay_direct_chat
    ccLanguage.cc_suspend_player_cant_lay = fCLDE.cc_language().cc_suspend_player_cant_lay
    ccLanguage.cc_suspend_player_false_card = fCLDE.cc_language().cc_suspend_player_false_card
    ccLanguage.cc_suspend_player_must_counter = fCLDE.cc_language().cc_suspend_player_must_counter

    ccLanguage.cc_suspend_player_counter_cant_get_new_cards = fCLDE.cc_language().cc_suspend_player_counter_cant_get_new_cards
    ccLanguage.cc_suspend_player_cant_get_new_cards = fCLDE.cc_language().cc_suspend_player_cant_get_new_cards

    ccLanguage.cc_suspend_player_want_sit_out = fCLDE.cc_language().cc_suspend_player_want_sit_out
    ccLanguage.cc_suspend_player_cant_sit_out = fCLDE.cc_language().cc_suspend_player_cant_sit_out
    ccLanguage.cc_suspend_player_cant_skip = fCLDE.cc_language().cc_suspend_player_cant_skip


    #Plus-Card
    ccLanguage.cc_plus_card_player_can_lay = fCLDE.cc_language().cc_plus_card_player_can_lay
    ccLanguage.cc_plus_card_player_cant_lay = fCLDE.cc_language().cc_plus_card_player_cant_lay
    ccLanguage.cc_plus_card_player_lay_false_card = fCLDE.cc_language().cc_plus_card_player_lay_false_card
    ccLanguage.cc_plus_card_player_cant_lay_false_card = fCLDE.cc_language().cc_plus_card_player_cant_lay_false_card

    ccLanguage.cc_plus_card_player_cant_take = fCLDE.cc_language().cc_plus_card_player_cant_take
    ccLanguage.cc_plus_card_player_take = fCLDE.cc_language().cc_plus_card_player_take
    ccLanguage.cc_plus_card_player_cant_skip = fCLDE.cc_language().cc_plus_card_player_cant_skip

    ccLanguage.cc_plus_card_player_cant_get_new_cards = fCLDE.cc_language().cc_plus_card_player_cant_get_new_cards
    ccLanguage.cc_plus_card_player_counter_cant_get_new_cards = fCLDE.cc_language().cc_plus_card_player_counter_cant_get_new_cards



    #Card-STR
    ccLanguage.cc_timer_action_sit_out = fCLDE.cc_language().cc_timer_action_sit_out
    ccLanguage.cc_timer_action_take_plus_cards = fCLDE.cc_language().cc_timer_action_take_plus_cards
    ccLanguage.cc_your_cards = fCLDE.cc_language().cc_your_cards
    ccLanguage.cc_current_mid_card = fCLDE.cc_language().cc_current_mid_card
    ccLanguage.cc_player_sequence = fCLDE.cc_language().cc_player_sequence
    ccLanguage.cc_players_turn = fCLDE.cc_language().cc_players_turn
    ccLanguage.cc_player_laid_card = fCLDE.cc_language().cc_player_laid_card
    ccLanguage.cc_player_picked_up_card = fCLDE.cc_language().cc_player_picked_up_card



    #Voice
    ccLanguage.cc_voice_players_turn = fCLDE.cc_language().cc_voice_players_turn
    ccLanguage.cc_voice_player_won = fCLDE.cc_language().cc_voice_player_won
    ccLanguage.cc_voice_player_sit_out = fCLDE.cc_language().cc_voice_player_sit_out



def load_language_file(cc_language_file_path, ccLanguage):
    
    with open(cc_language_file_path, encoding="UTF-8") as json_file:

        try:
            language_data = json.load(json_file)
        except Exception as error:

            fCU.log_In_Console("Failed to load settings! - {}".format(str(error)), "LOAD-SETTINGS", "err")
            exit()


        try:

            #General
            ccLanguage.cc_wrong_arguments = str(language_data["General"]["Wrong-Arguments"])
            ccLanguage.cc_wrong_game_command = str(language_data["General"]["Wrong-Command"])
            ccLanguage.cc_shutdown_bot = str(language_data["General"]["Shutdown-Bot"])


            #Game
            ccLanguage.cc_game_already_running = str(language_data["Game"]["Already-Running"])
            ccLanguage.cc_cards_per_player_set_to = str(language_data["Game"]["Cards-Per-Player-Set"])
            ccLanguage.cc_no_game_running = str(language_data["Game"]["No-Game-Running"])
            ccLanguage.cc_user_already_joined = str(language_data["Game"]["User-Already-Joined"])
            ccLanguage.cc_user_joined_game = str(language_data["Game"]["User-Joined"])
            ccLanguage.cc_more_players_needed = str(language_data["Game"]["More-Players-Needed"])
            ccLanguage.cc_user_started_game = str(language_data["Game"]["User-Started"])
            ccLanguage.cc_user_not_part = str(language_data["Game"]["User-Not-Part"])
            ccLanguage.cc_player_won = str(language_data["Game"]["Player-Won"])

            ccLanguage.cc_user_leave_no_part = str(language_data["Game"]["Leaving-User-No-Part"])
            ccLanguage.cc_game_end_because_user_left = str(language_data["Game"]["Ended-User-Left"])
            ccLanguage.cc_user_left = str (language_data["Game"]["User-Left"])
            ccLanguage.cc_user_cant_leave_his_turn = str(language_data["Game"]["User-Cant-Leave"])

            ccLanguage.cc_user_no_turn = str(language_data["Game"]["Not-Users-Turn"])
            ccLanguage.cc_card_not_exist = str(language_data["Game"]["Card-Not-Exist"])
            ccLanguage.cc_user_cant_lay_card = str(language_data["Game"]["User-Cant-Lay"])
            ccLanguage.cc_user_your_turn = str(language_data["Game"]["Users-Turn"])

            ccLanguage.cc_wish_without_color = str(language_data["Game"]["Wish-Without-Color"])
            ccLanguage.cc_wish_unknown_color = str(language_data["Game"]["Wish-Unknown-Color"])

            ccLanguage.cc_input_only_numbers = str(language_data["Game"]["Input-Only-Numbers"])
            ccLanguage.cc_input_no_number_arg = str(language_data["Game"]["Input-No-Number"])

            ccLanguage.cc_game_stopped_by = str(language_data["Game"]["Stopped-By"])
            ccLanguage.cc_game_cant_stopped = str(language_data["Game"]["Cant-Stop"])
            ccLanguage.cc_game_player_has_cc = str(language_data["Game"]["Player-Has-CC"])
            ccLanguage.cc_game_player_can_lay = str(language_data["Game"]["Player-Can-Lay"])
            ccLanguage.cc_game_player_cant_lay = str(language_data["Game"]["Player-Cant-Lay"])

            ccLanguage.cc_please_choose_wish_color_react = str(language_data["Game"]["Choose-Wish-Color-React"])
            ccLanguage.cc_please_choose_card_color_react = str(language_data["Game"]["Choose-Card-Color-React"])
            ccLanguage.cc_please_choose_card_num_react = str(language_data["Game"]["Choose-Card-Num-React"])

            ccLanguage.cc_false_choose_color_react = str(language_data["Game"]["False-Choose-Color-React"])
            ccLanguage.cc_false_choose_number_react = str(language_data["Game"]["False-Choose-Number-React"])

            ccLanguage.cc_no_kick_user = str(language_data["Game"]["No-Kick-User"])
            ccLanguage.cc_kick_user_isnt_player = str(language_data["Game"]["Kick-User-Isnt-Player"])
            ccLanguage.cc_cant_kick_current_player = str(language_data["Game"]["Cant-Kick-Current-Player"])
            ccLanguage.cc_user_kicked = str(language_data["Game"]["User-Kicked"])


            #Suspend
            ccLanguage.cc_suspend_player_cant_lay_direct_chat = str(language_data["Game"]["Suspend"]["Player-Cant-Lay-Direct"])
            ccLanguage.cc_suspend_player_cant_lay = str(language_data["Game"]["Suspend"]["Player-Cant-Lay"])
            ccLanguage.cc_suspend_player_false_card = str(language_data["Game"]["Suspend"]["Player-False-Card"])
            ccLanguage.cc_suspend_player_must_counter = str(language_data["Game"]["Suspend"]["Player-Must-Counter"])

            ccLanguage.cc_suspend_player_counter_cant_get_new_cards = str(language_data["Game"]["Suspend"]["Player-Counter-No-New-Cards"])
            ccLanguage.cc_suspend_player_cant_get_new_cards = str(language_data["Game"]["Suspend"]["Player-No-New-Cards"])

            ccLanguage.cc_suspend_player_want_sit_out = str(language_data["Game"]["Suspend"]["Player-Want-Sit-Out"])
            ccLanguage.cc_suspend_player_cant_sit_out = str(language_data["Game"]["Suspend"]["Player-Cant-Sit-Out"])
            ccLanguage.cc_suspend_player_cant_skip = str(language_data["Game"]["Suspend"]["Player-Cant-Skip"])


            #Plus-Card
            ccLanguage.cc_plus_card_player_can_lay = str(language_data["Game"]["Plus-Card"]["Player-Can-Lay"])
            ccLanguage.cc_plus_card_player_cant_lay = str(language_data["Game"]["Plus-Card"]["Player-Cant-Lay"])
            ccLanguage.cc_plus_card_player_lay_false_card = str(language_data["Game"]["Plus-Card"]["Player-Lay-False-Card"])
            ccLanguage.cc_plus_card_player_cant_lay_false_card = str(language_data["Game"]["Plus-Card"]["Player-Cant-Lay-False-Card"])

            ccLanguage.cc_plus_card_player_cant_take = str(language_data["Game"]["Plus-Card"]["Player-Cant-Take"])
            ccLanguage.cc_plus_card_player_take = str(language_data["Game"]["Plus-Card"]["Player-Take"])
            ccLanguage.cc_plus_card_player_cant_skip = str(language_data["Game"]["Plus-Card"]["Cant-Skip"])

            ccLanguage.cc_plus_card_player_cant_get_new_cards = str(language_data["Game"]["Plus-Card"]["Player-Cant-Get-New-Cards"])
            ccLanguage.cc_plus_card_player_counter_cant_get_new_cards = str(language_data["Game"]["Plus-Card"]["Player-Counter-Cant-Get-New-Cards"])



            #Card-STR
            ccLanguage.cc_timer_action_sit_out = str(language_data["Card-STR"]["Action-Sit-Out"])
            ccLanguage.cc_timer_action_take_plus_cards = str(language_data["Card-STR"]["Action-Take-Plus-Cards"])
            ccLanguage.cc_your_cards = str(language_data["Card-STR"]["Your-Cards"])
            ccLanguage.cc_current_mid_card = str(language_data["Card-STR"]["Current-Mid-Card"])
            ccLanguage.cc_player_sequence = str(language_data["Card-STR"]["Player-Sequence"])
            ccLanguage.cc_players_turn = str(language_data["Card-STR"]["Players-Turn"])
            ccLanguage.cc_player_laid_card = str(language_data["Card-STR"]["Player-Laid-Card"])
            ccLanguage.cc_player_picked_up_card = str(language_data["Card-STR"]["Player-Picked-Up-Card"])


            #Voice
            ccLanguage.cc_voice_players_turn = str(language_data["Voice"]["Players-Turn"])
            ccLanguage.cc_voice_player_won = str(language_data["Voice"]["Player-Won"])
            ccLanguage.cc_voice_player_sit_out = str(language_data["Voice"]["Player-Sit-Out"])


        except Exception as error:

            fCU.log_In_Console("Failed to load settings! - {}".format(str(error)), "LOAD-SETTINGS", "err")
            fCU.log_In_Console("Shutdown bot. Please check the settings-file for errors.", "LOAD-SETTINGS", "inf")
            exit()


        fCU.log_In_Console("Settings successfully loaded.", "LOAD-SETTINGS", "inf")


def create_language_file(language_file_path):
    
    fCU.log_In_Console("Creating language-file...", "CREATE-SETTINGS", "inf")

    language_data = {}
    language_data["General"] = {}
    language_data["Game"] = {}
    language_data["Card-STR"] = {}
    language_data["Voice"] = {}



    #General
    language_data["General"]["Wrong-Arguments"] = fCLEN.cc_language.cc_wrong_arguments
    language_data["General"]["Wrong-Command"] = fCLEN.cc_language.cc_wrong_game_command
    language_data["General"]["Shutdown-Bot"] = fCLEN.cc_language.cc_shutdown_bot


    #Game
    language_data["Game"]["Already-Running"] = fCLEN.cc_language.cc_game_already_running
    language_data["Game"]["Cards-Per-Player-Set"] = fCLEN.cc_language.cc_cards_per_player_set_to
    language_data["Game"]["No-Game-Running"] = fCLEN.cc_language.cc_no_game_running
    language_data["Game"]["User-Already-Joined"] = fCLEN.cc_language.cc_user_already_joined
    language_data["Game"]["User-Joined"] = fCLEN.cc_language.cc_user_joined_game
    language_data["Game"]["More-Players-Needed"] = fCLEN.cc_language.cc_more_players_needed
    language_data["Game"]["User-Started"] = fCLEN.cc_language.cc_user_started_game
    language_data["Game"]["User-Not-Part"] = fCLEN.cc_language.cc_user_not_part
    language_data["Game"]["Player-Won"] = fCLEN.cc_language.cc_player_won

    language_data["Game"]["Leaving-User-No-Part"] = fCLEN.cc_language.cc_user_leave_no_part
    language_data["Game"]["Ended-User-Left"] = fCLEN.cc_language.cc_game_end_because_user_left
    language_data["Game"]["User-Left"] = fCLEN.cc_language.cc_user_left
    language_data["Game"]["User-Cant-Leave"] = fCLEN.cc_language.cc_user_cant_leave_his_turn

    language_data["Game"]["Not-Users-Turn"] = fCLEN.cc_language.cc_user_no_turn
    language_data["Game"]["Card-Not-Exist"] = fCLEN.cc_language.cc_card_not_exist
    language_data["Game"]["User-Cant-Lay"] = fCLEN.cc_language.cc_user_cant_lay_card
    language_data["Game"]["Users-Turn"] = fCLEN.cc_language.cc_user_your_turn

    language_data["Game"]["Wish-Without-Color"] = fCLEN.cc_language.cc_wish_without_color
    language_data["Game"]["Wish-Unknown-Color"] = fCLEN.cc_language.cc_wish_unknown_color

    language_data["Game"]["Input-Only-Numbers"] = fCLEN.cc_language.cc_input_only_numbers
    language_data["Game"]["Input-No-Number"] = fCLEN.cc_language.cc_input_no_number_arg

    language_data["Game"]["Stopped-By"] = fCLEN.cc_language.cc_game_stopped_by
    language_data["Game"]["Cant-Stop"] = fCLEN.cc_language.cc_game_cant_stopped
    language_data["Game"]["Player-Has-CC"] = fCLEN.cc_language.cc_game_player_has_cc
    language_data["Game"]["Player-Can-Lay"] = fCLEN.cc_language.cc_game_player_can_lay
    language_data["Game"]["Player-Cant-Lay"] = fCLEN.cc_language.cc_game_player_cant_lay

    language_data["Game"]["Choose-Wish-Color-React"] = fCLEN.cc_language.cc_please_choose_wish_color_react
    language_data["Game"]["Choose-Card-Color-React"] = fCLEN.cc_language.cc_please_choose_card_color_react
    language_data["Game"]["Choose-Card-Num-React"] = fCLEN.cc_language.cc_please_choose_card_num_react

    language_data["Game"]["False-Choose-Color-React"] = fCLEN.cc_language.cc_false_choose_color_react
    language_data["Game"]["False-Choose-Number-React"] = fCLEN.cc_language.cc_false_choose_number_react

    language_data["Game"]["No-Kick-User"] = fCLEN.cc_language.cc_no_kick_user
    language_data["Game"]["Kick-User-Isnt-Player"] = fCLEN.cc_language.cc_kick_user_isnt_player
    language_data["Game"]["Cant-Kick-Current-Player"] = fCLEN.cc_language.cc_cant_kick_current_player
    language_data["Game"]["User-Kicked"] = fCLEN.cc_language.cc_user_kicked


    #Suspend
    language_data["Game"]["Suspend"] = {}

    language_data["Game"]["Suspend"]["Player-Cant-Lay-Direct"] = fCLEN.cc_language.cc_suspend_player_cant_lay_direct_chat
    language_data["Game"]["Suspend"]["Player-Cant-Lay"] = fCLEN.cc_language.cc_suspend_player_cant_lay
    language_data["Game"]["Suspend"]["Player-False-Card"] = fCLEN.cc_language.cc_suspend_player_false_card
    language_data["Game"]["Suspend"]["Player-Must-Counter"] = fCLEN.cc_language.cc_suspend_player_must_counter

    language_data["Game"]["Suspend"]["Player-Counter-No-New-Cards"] = fCLEN.cc_language.cc_suspend_player_counter_cant_get_new_cards
    language_data["Game"]["Suspend"]["Player-No-New-Cards"] = fCLEN.cc_language.cc_suspend_player_cant_get_new_cards

    language_data["Game"]["Suspend"]["Player-Want-Sit-Out"] = fCLEN.cc_language.cc_suspend_player_want_sit_out
    language_data["Game"]["Suspend"]["Player-Cant-Sit-Out"] = fCLEN.cc_language.cc_suspend_player_cant_sit_out
    language_data["Game"]["Suspend"]["Player-Cant-Skip"] = fCLEN.cc_language.cc_suspend_player_cant_skip


    #Plus-Card
    language_data["Game"]["Plus-Card"] = {}

    language_data["Game"]["Plus-Card"]["Player-Can-Lay"] = fCLEN.cc_language.cc_plus_card_player_can_lay
    language_data["Game"]["Plus-Card"]["Player-Cant-Lay"] = fCLEN.cc_language.cc_plus_card_player_cant_lay
    language_data["Game"]["Plus-Card"]["Player-Lay-False-Card"] = fCLEN.cc_language.cc_plus_card_player_lay_false_card
    language_data["Game"]["Plus-Card"]["Player-Cant-Lay-False-Card"] = fCLEN.cc_language.cc_plus_card_player_cant_lay_false_card

    language_data["Game"]["Plus-Card"]["Player-Cant-Take"] = fCLEN.cc_language.cc_plus_card_player_cant_take
    language_data["Game"]["Plus-Card"]["Player-Take"] = fCLEN.cc_language.cc_plus_card_player_take
    language_data["Game"]["Plus-Card"]["Cant-Skip"] = fCLEN.cc_language.cc_plus_card_player_cant_skip

    language_data["Game"]["Plus-Card"]["Player-Cant-Get-New-Cards"] = fCLEN.cc_language.cc_plus_card_player_cant_get_new_cards
    language_data["Game"]["Plus-Card"]["Player-Counter-Cant-Get-New-Cards"] = fCLEN.cc_language.cc_plus_card_player_counter_cant_get_new_cards



    #Card-STR
    language_data["Card-STR"]["Action-Sit-Out"] = fCLEN.cc_language.cc_timer_action_sit_out
    language_data["Card-STR"]["Action-Take-Plus-Cards"] = fCLEN.cc_language.cc_timer_action_take_plus_cards
    language_data["Card-STR"]["Your-Cards"] = fCLEN.cc_language.cc_your_cards
    language_data["Card-STR"]["Current-Mid-Card"] = fCLEN.cc_language.cc_current_mid_card
    language_data["Card-STR"]["Player-Sequence"] = fCLEN.cc_language.cc_player_sequence
    language_data["Card-STR"]["Players-Turn"] = fCLEN.cc_language.cc_players_turn
    language_data["Card-STR"]["Player-Laid-Card"] = fCLEN.cc_language.cc_player_laid_card
    language_data["Card-STR"]["Player-Picked-Up-Card"] = fCLEN.cc_language.cc_player_picked_up_card



    #Voice
    language_data["Voice"]["Players-Turn"] = fCLEN.cc_language.cc_voice_players_turn
    language_data["Voice"]["Player-Won"] = fCLEN.cc_language.cc_voice_player_won
    language_data["Voice"]["Player-Sit-Out"] = fCLEN.cc_language.cc_voice_player_sit_out



    with open(language_file_path, "w", encoding="UTF-8") as outfile:
        json.dump(language_data, outfile, indent=4, sort_keys=True, ensure_ascii=False)


    fCU.log_In_Console("Saved language-file sucessfully.", "CREATE-SETTINGS", "inf")