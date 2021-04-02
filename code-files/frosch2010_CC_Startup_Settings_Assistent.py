import os
import sys
import json


import frosch2010_Console_Utils as fCU


def settings_assistent(settings_file):

    print("\nWelcome to the setup wizard. Just answer the following questions via the console and the settings file will be created in the background. If you have more specific questions about the settings, check the GitHub page again.\nBut now we start...\n")


    #Create Settings-Vars
    settings_data = {}
    settings_data["Channel-IDs"] = {}
    settings_data["General-Settings"] = {}
    settings_data["Language-Settings"] = {}
    settings_data["Game-Card-Settings"] = {}
    settings_data["Game-Settings"] = {}
    settings_data["Voice-Settings"] = {}



    #------------------------------------------------------------------------------------------------------------
    #General-Settings        

    #Bot-Token
    print("Specify the bot token.")
    bot_token = input("Bot-Token: ")

    while bot_token == "":
        print("You must specify a bot token!")
        bot_token = input("Server-ID: ")

    settings_data["General-Settings"]["Bot-Token"] = bot_token


    #Server-ID
    print("\nSpecify the server ID on which the bot should run.")
    server_id = input("Server-ID: ")

    while not server_id.isdigit():
        print("That was not a channel ID! A channel ID can only contain numbers.\nPlease enter a channel ID.")
        server_id = input("Server-ID: ")

    settings_data["General-Settings"]["Server-ID"] = int(server_id)
    print(server_id)


    #------------------------------------------------------------------------------------------------------------
    #Channel-Settings

    #Join-Channel
    print("\nWhat is the channel ID for the join channel?")
    join_channel_id = input("Join-Channel-ID: ")

    while not join_channel_id.isdigit():
        print("That was not a channel ID! A channel ID can only contain numbers.\nPlease enter a channel ID.")
        join_channel_id = input("Join-Channel-ID: ")

    settings_data["Channel-IDs"]["Join"] = int(join_channel_id)
    print(join_channel_id)



    #Admin-Channel
    print("\nWhat is the channel ID for the admin channel?")
    admin_channel_id = input("Admin-Channel-ID: ")

    while not admin_channel_id.isdigit():
        print("That was not a channel ID! A channel ID can only contain numbers.\nPlease enter a channel ID.")
        admin_channel_id = input("Admin-Channel-ID: ")

    settings_data["Channel-IDs"]["Administration"] = int(admin_channel_id)
    print(admin_channel_id)



    #Spectate-Channel
    print("\nShould there be a viewer channel?")
    user_viewer_channel_choice = input("YES or NO? [y/N] ")
    output_to_spectate = None

    
    while output_to_spectate == None:
        
        if user_viewer_channel_choice.lower() == "n" or user_viewer_channel_choice == "":
            output_to_spectate = False
            break

        elif user_viewer_channel_choice.lower() == "y":
            output_to_spectate = True
            break

        print("Please use y for yes and n for no.")
        user_viewer_channel_choice = input("YES or NO? [Y/n] ")


    #Use Spectate-Channel
    if output_to_spectate:
        settings_data["Game-Settings"]["Output-To-Spectate"] = True


        print("What is the channel ID for the spectate channel?")
        spectate_channel_id = input("Spectate-Channel-ID: ")

        while not spectate_channel_id.isdigit():
            print("That was not a channel ID! A channel ID can only contain numbers.\nPlease enter a channel ID.")
            spectate_channel_id = input("Spectate-Channel-ID: ")

        settings_data["Channel-IDs"]["Spectate"] = int(spectate_channel_id)
        print(spectate_channel_id)

    
    #Disable the Spectate-Channel
    else:
        settings_data["Game-Settings"]["Output-To-Spectate"] = False
        settings_data["Channel-IDs"]["Spectate"] = 0



    #Voice-Channel
    print("\nIf the bot is also to output via a voice channel?")
    user_voice_choice = input("YES or NO? [y/N] ")
    output_voice = None

    
    while output_voice == None:
        
        if user_voice_choice.lower() == "n" or user_voice_choice == "":
            output_voice = False
            break

        elif user_voice_choice.lower() == "y":
            output_voice = True
            break

        print("Please use y for yes and n for no.")
        user_voice_choice = input("YES or NO? [y/N] ")


    #Use voice
    if output_voice:
        settings_data["Voice-Settings"]["Use-Voice"] = True

        #Language
        print("In which language should the voice output be?\nPlease enter the corresponding abbreviation. For example, 'en' for English. For a list of all supported languages, type 'gtts-cli --all' in another terminal or check the ColorCards GitHUB page again.")
        user_voice_language_choice = input("Language: ")

        while user_voice_language_choice == "":
            print("You must specify an language!")
            user_voice_language_choice = input("Server-ID: ")

        settings_data["Voice-Settings"]["Language"] = user_voice_language_choice


        #Check if the operating system is windows and set the FFmpeg path if necessary
        if os.name == "nt":

            print("Since the bot runs on a Windows server, you need to specify the path to FFmpeg-Exe.\nWhat is the path?")
            user_ffmpeg_path = input("FFmpeg-Path: ")


            if os.path.isfile(user_ffmpeg_path):
                settings_data["Voice-Settings"]["Windows-FFmpeg-Exe-Path"] = user_ffmpeg_path
            else:

                while True:
                    print("This is not a valid path. Please specify a path to FFmpeg.exe.")
                    user_ffmpeg_path = input("FFmpeg-Path: ")

                    if os.path.isfile(user_ffmpeg_path):
                        settings_data["Voice-Settings"]["Windows-FFmpeg-Exe-Path"] = user_ffmpeg_path
                        break


        else:
            settings_data["Voice-Settings"]["Windows-FFmpeg-Exe-Path"] = ""


    else:
        settings_data["Channel-IDs"]["Voice"] = 0
        settings_data["Voice-Settings"]["Use-Voice"] = False
        settings_data["Voice-Settings"]["Language"] = "en"
        settings_data["Voice-Settings"]["Windows-FFmpeg-Exe-Path"] = ""


    #------------------------------------------------------------------------------------------------------------
    #Language-Settings

    #English or German?
    print("\nDo you want to use a language other than English or German or create a language file?")
    user_language_file_choice = input("YES or NO? [y/N] ")
    language_file_voice = None

    
    while language_file_voice == None:
        
        if user_language_file_choice.lower() == "n" or user_language_file_choice == "":
            language_file_voice = False
            break

        elif user_language_file_choice.lower() == "y":
            language_file_voice = True
            break

        print("Please use y for yes and n for no.")
        user_language_file_choice = input("YES or NO? [y/N] ")

    settings_data["Language-Settings"]["Use-Language-File"] = language_file_voice


    #Create language-file?
    if language_file_voice:
        
        settings_data["Language-Settings"]["Discord-Language"] = ""


        print("A language file will be created. If you don't want to save it in the bot's folder, specify a different save path now.\nOtherwise just press Enter.")
        user_language_file_path = input("Language-File-Path: ")


        if os.path.isdir(user_language_file_path):
            settings_data["Language-Settings"]["Language-File-Path"] = user_language_file_path
        else:

            while True:
                print("This is not a valid path. Please specify a path to FFmpeg.exe.")
                user_language_file_path = input("Language-File-Path: ")

                if os.path.isdir(user_language_file_path):
                    settings_data["Language-Settings"]["Language-File-Path"] = user_language_file_path
                    break


    #Use a build in language
    else:
        print("Select German 'de' or English 'en.")
        user_selected_language = input("Language: ")

        while user_selected_language.lower() != "de" and user_selected_language.lower() != "en":
            print("Please choose between 'de' and 'en'!")
            user_selected_language = input("Language: ")

        settings_data["Language-Settings"]["Discord-Language"] = user_selected_language
        settings_data["Language-Settings"]["Language-File-Path"] = ""


    
    #----------------------------------------------------------------------------------------------------------
    #Finish
    print("\nAll necessary settings have been made. If you want to change them in the future or make further settings, you can do this at any time via the settings file.")


    #Game-Card-Settings
    settings_data["Game-Card-Settings"]["Default-Cards-Per-Player"] = 6
    settings_data["Game-Card-Settings"]["Plus-Card-Amount"] = 2
    settings_data["Game-Card-Settings"]["Wish-Question-Min-Amount"] = 3
    settings_data["Game-Card-Settings"]["Wish-Question-Max-Amount"] = 6
    settings_data["Game-Card-Settings"]["Wish-All-Min-Amount"] = 3
    settings_data["Game-Card-Settings"]["Wish-All-Max-Amount"] = 6


    #Game-Settings
    settings_data["Game-Settings"]["Min-Players"] = 2
    settings_data["Game-Settings"]["Game-Command"] = "cc"
    settings_data["Game-Settings"]["Inf-Messages-Auto-Delete"] = 10
    settings_data["Game-Settings"]["Better-Player-Notification"] = True
    settings_data["Game-Settings"]["Show-Player-Card-Count"] = True
    settings_data["Game-Settings"]["Output-To-Spectate"] = False
    settings_data["Game-Settings"]["Delete-Old-Messages"] = False
    settings_data["Game-Settings"]["Play-With-Reactions"] = False



    fCU.log_In_Console("Save settings to file...", "FIRST-ST", "inf")


    with open(settings_file, "w", encoding="UTF-8") as outfile:
        json.dump(settings_data, outfile, indent=4, sort_keys=True, ensure_ascii=False)


    fCU.log_In_Console("Saved settings sucessfully.", "FIRST-ST", "inf")