import os
import sys
import json

import frosch2010_Console_Utils as fCU


def load_settings(settings_file, ccSettings):

    with open(settings_file, encoding="UTF-8") as json_file:

        try:
            settings_data = json.load(json_file)
        except Exception as error:

            fCU.log_In_Console("Failed to load settings! - {}".format(str(error)), "LOAD-SETTINGS", "err")
            exit()


        try:

            #Channel-IDs
            ccSettings.cc_channelID_join = int(settings_data["Channel-IDs"]["Join"])
            ccSettings.cc_channelID_spectate = int(settings_data["Channel-IDs"]["Spectate"])
            ccSettings.cc_channelID_voice = int(settings_data["Channel-IDs"]["Voice"])
            ccSettings.cc_channelID_bot_admin = int(settings_data["Channel-IDs"]["Administration"])


            #General-Settings
            ccSettings.cc_ServerID = int(settings_data["General-Settings"]["Server-ID"])
            ccSettings.cc_bot_token = str(settings_data["General-Settings"]["Bot-Token"])


            #Language-Settings
            ccSettings.cc_use_language_file = bool(settings_data["Language-Settings"]["Use-Language-File"])
            ccSettings.cc_language_file_path = str(settings_data["Language-Settings"]["Language-File-Path"])
            ccSettings.cc_discord_language = str(settings_data["Language-Settings"]["Discord-Language"])


            #Game-Card-Settings
            ccSettings.cc_cards_per_player = int(settings_data["Game-Card-Settings"]["Default-Cards-Per-Player"])
            ccSettings.cc_plus_card_amount = int(settings_data["Game-Card-Settings"]["Plus-Card-Amount"])
            ccSettings.cc_wish_next_get_cards_amount_min = int(settings_data["Game-Card-Settings"]["Wish-Question-Min-Amount"])
            ccSettings.cc_wish_next_get_cards_amount_max = int(settings_data["Game-Card-Settings"]["Wish-Question-Max-Amount"])
            ccSettings.cc_wish_all_get_cards_amount_min = int(settings_data["Game-Card-Settings"]["Wish-All-Min-Amount"])
            ccSettings.cc_wish_all_get_cards_amount_max = int(settings_data["Game-Card-Settings"]["Wish-All-Max-Amount"])


            #Game-Settings
            ccSettings.cc_min_players = int(settings_data["Game-Settings"]["Min-Players"])
            ccSettings.cc_game_command = str(settings_data["Game-Settings"]["Game-Command"])
            ccSettings.cc_message_auto_delete = int(settings_data["Game-Settings"]["Inf-Messages-Auto-Delete"])
            ccSettings.cc_send_extra_msg_if_players_turn = bool(settings_data["Game-Settings"]["Better-Player-Notification"])
            ccSettings.cc_show_player_card_count = bool(settings_data["Game-Settings"]["Show-Player-Card-Count"])
            ccSettings.cc_show_game_in_spectate = bool(settings_data["Game-Settings"]["Output-To-Spectate"])
            ccSettings.cc_delete_old_messages = bool(settings_data["Game-Settings"]["Delete-Old-Messages"])
            ccSettings.cc_play_with_reactions = bool(settings_data["Game-Settings"]["Play-With-Reactions"])


            #Voice-Settings
            ccSettings.cc_use_voice = bool(settings_data["Voice-Settings"]["Use-Voice"])
            ccSettings.cc_voice_language = str(settings_data["Voice-Settings"]["Language"])
            ccSettings.cc_ffmpeg_path = str(settings_data["Voice-Settings"]["Windows-FFmpeg-Exe-Path"])


        except Exception as error:

            fCU.log_In_Console("Failed to load settings! - {}".format(str(error)), "LOAD-SETTINGS", "err")
            fCU.log_In_Console("Shutdown bot. Please check the settings-file for errors.", "LOAD-SETTINGS", "inf")
            exit()


        fCU.log_In_Console("Settings successfully loaded.", "LOAD-SETTINGS", "inf")



def create_default_settings_file(settings_file):

    fCU.log_In_Console("Creating settings-file...", "CREATE-SETTINGS", "inf")

    settings_data = {}
    settings_data["Channel-IDs"] = {}
    settings_data["General-Settings"] = {}
    settings_data["Language-Settings"] = {}
    settings_data["Game-Card-Settings"] = {}
    settings_data["Game-Settings"] = {}
    settings_data["Voice-Settings"] = {}



    #Channel-IDs
    channel_names = ["Join", "Spectate", "Voice", "Administration"]

    for channel_name in channel_names:
        settings_data["Channel-IDs"][channel_name] = 0


    #General-Settings
    settings_data["General-Settings"]["Server-ID"] = 0
    settings_data["General-Settings"]["Bot-Token"] = ""


    #Language-Settings
    settings_data["Language-Settings"]["Use-Language-File"] = False
    settings_data["Language-Settings"]["Language-File-Path"] = ""
    settings_data["Language-Settings"]["Discord-Language"] = "de"


    #Game-Card-Settings
    settings_data["Game-Card-Settings"]["Default-Cards-Per-Player"] = 6
    settings_data["Game-Card-Settings"]["Plus-Card-Amount"] = 2
    settings_data["Game-Card-Settings"]["Wish-Question-Min-Amount"] = 0
    settings_data["Game-Card-Settings"]["Wish-Question-Max-Amount"] = 3
    settings_data["Game-Card-Settings"]["Wish-All-Min-Amount"] = 0
    settings_data["Game-Card-Settings"]["Wish-All-Max-Amount"] = 3


    #Game-Settings
    settings_data["Game-Settings"]["Min-Players"] = 2
    settings_data["Game-Settings"]["Game-Command"] = "cc"
    settings_data["Game-Settings"]["Inf-Messages-Auto-Delete"] = 10
    settings_data["Game-Settings"]["Better-Player-Notification"] = True
    settings_data["Game-Settings"]["Show-Player-Card-Count"] = True
    settings_data["Game-Settings"]["Output-To-Spectate"] = False
    settings_data["Game-Settings"]["Delete-Old-Messages"] = False
    settings_data["Game-Settings"]["Play-With-Reactions"] = False


    #Voice-Settings
    settings_data["Voice-Settings"]["Use-Voice"] = False
    settings_data["Voice-Settings"]["Language"] = "de"
    settings_data["Voice-Settings"]["Windows-FFmpeg-Exe-Path"] = ""


    fCU.log_In_Console("Save default settings to file...", "FIRST-ST", "inf")


    with open(settings_file, "w", encoding="UTF-8") as outfile:
        json.dump(settings_data, outfile, indent=4, sort_keys=True, ensure_ascii=False)


    fCU.log_In_Console("Saved default settings sucessfully.", "CREATE-SETTINGS", "inf")