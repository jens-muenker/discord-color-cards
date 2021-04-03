import os
import sys
from termcolor import colored, cprint
import colorama


import frosch2010_Console_Utils as fCU
import frosch2010_CC_Startup_Settings_Assistent as fCSSA
import frosch2010_CC_settings_file_manager as fCSFM
import frosch2010_CC_language_manager as fCLM


def initialize_bot(ccVars, ccLanguage, ccSettings):

    colorama.init()
    
    cprint(colored("\n####   ####   #      ####   ###       ####    ##    ###    ###    ####", "red"))
    cprint(colored("#      #  #   #      #  #   #  #      #      #  #   #  #   #  #   ##", "yellow"))
    cprint(colored("#      #  #   #      #  #   ###       #      ####   ###    #  #     ##", "green"))
    cprint(colored("####   ####   ####   ####   #  #      ####   #  #   #  #   ###    ####", "blue"))
    cprint(colored("\n                            by Frosch2010 \n", "yellow"))

    fCU.log_In_Console("Starting...", "INIT-BOT", "inf")


    #Checking if settings-file exists
    fCU.log_In_Console("Try to load settings-file...", "INIT-BOT", "inf")
    settings_file = sys.argv[0].replace(os.path.basename(sys.argv[0]), "") + "cc-settings.config"

    if not os.path.isfile(settings_file):
        first_start(settings_file, ccVars, ccLanguage, ccSettings)


    fCSFM.load_settings(settings_file, ccSettings)


    #Check/setup language
    fCLM.setup_language(ccLanguage, ccSettings)



def first_start(settings_file, ccVars, ccLanguage, ccSettings):

    fCU.log_In_Console("No settings-file found. Prepare bot for first start...", "FIRST-ST", "war")


    #Query whether to use the setup wizard
    print("Do you want to use the setup wizard or just create the settings file, which you would have to fill in yourself?")
    user_choice = input("YES or NO? [Y/n] ")
    use_assistent = None

    
    while use_assistent == None:
        
        if user_choice.lower() == "y" or user_choice == "":
            use_assistent = True
            break

        elif user_choice.lower() == "n":
            use_assistent = False
            break

        print("Please use y for yes and n for no.")
        user_choice = input("YES or NO? [Y/n] ")


    #Assistent
    if use_assistent:
        fCSSA.settings_assistent(settings_file)

    #No Assistent
    else:

        fCSFM.create_default_settings_file(settings_file)        
        fCU.log_In_Console("Please adjust the settings file and then start the bot again.", "FIRST-ST", "inf")

        exit()