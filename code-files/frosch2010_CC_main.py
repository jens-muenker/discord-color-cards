import discord
from discord import guild
import discord.member
import asyncio
import os
import sys


import frosch2010_CC_Startup as fCS
import frosch2010_Discord_Utils as fDU
import frosch2010_Console_Utils as fCU
import frosch2010_CC_language
import frosch2010_CC_settings
import frosch2010_CC_variables
import frosch2010_Class_Utils as fCLU
import frosch2010_CC_manage_timer as fCMT
import frosch2010_CC_On_Ready as fCCOR
import frosch2010_CC_On_Start_Game as fUCCSG
import frosch2010_CC_lay_card as fCCLC
import frosch2010_CC_other_functions as fCCOF
import frosch2010_CC_get_new_cards as fCCGNC
import frosch2010_CC_On_Reaction as fCCOREACT
import frosch2010_CC_player_leave as fCCPL
import frosch2010_CC_voice_module as fCCVM


#-----------------------------------------------------
#Variables
#-----------------------------------------------------

ccSettings = frosch2010_CC_settings.cc_settings()
ccVars = frosch2010_CC_variables.cc_variables()
ccLanguage = frosch2010_CC_language.cc_language()


#-----------------------------------------------------
#Create Discord-Client
#-----------------------------------------------------

intents = discord.Intents.all()
client = discord.Client(intents=intents)


#-----------------------------------------------------
#Discord-Client-Events
#-----------------------------------------------------

@client.event
async def on_ready():

    global client

    await fCCOR.on_ready(client)


@client.event
async def on_message(msg):


    if msg.author.bot:
        return


    if not msg.content.lower().startswith("!" + ccSettings.cc_game_command) and not msg.channel.type == discord.channel.ChannelType.private:
        return


    if not msg.content.lower().startswith("!" + ccSettings.cc_game_command) and msg.channel.type == discord.channel.ChannelType.private and ccVars.cc_is_running == False:
        await fDU.send_Message_To_Channel(ccLanguage.cc_no_game_running.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], 4)
        return


    args = msg.content.replace("! ", "!").split(" ")


    #Check msg channel type (performance)
    if msg.channel.type == discord.channel.ChannelType.private:

        # --------------------------------------------------------
        # Lay card - COMMAND
        if args[0].lower() == "!card" or args[0].lower() == "!c":

            await fCCLC.lay_card(msg, client, ccVars, ccSettings, ccLanguage)


        #------------------------------------------------------------------
        #Getnewcard - COMMAND
        elif args[0].lower() == "!getnewcard" or args[0].lower() == "!gnc":

            await fCCGNC.get_new_card(msg, client, ccVars, ccSettings, ccLanguage)


        #------------------------------------------------------------------
        #Sit out - COMMAND
        elif args[0].lower() == "!sitout" or args[0].lower() == "!so":

            if ccVars.cc_player_is_suspend:

                if not ccVars.cc_suspended_player_can_lay:

                    await fDU.send_Message_To_Channel(ccLanguage.cc_suspend_player_cant_skip.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
                    fCU.log_In_Console("{} wants to sit out, but he does already.".format(msg.author.name), "PRIVATE-COMS", "inf")
                    return


                fCLU.Timer(10, fCMT.manage_timer, [ccVars, ccSettings, ccLanguage, client])

                await fDU.send_Message_To_Channel(ccLanguage.cc_suspend_player_want_sit_out.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
                fCU.log_In_Console("{} wants to sit out.".format(msg.author.name), "PRIVATE-COMS", "inf")
                return

            else:

                await fDU.send_Message_To_Channel(ccLanguage.cc_suspend_player_cant_sit_out.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
                fCU.log_In_Console("{} wants to sit out, but he cant sit out.".format(msg.author.name), "PRIVATE-COMS", "war")
                return


        #------------------------------------------------------------------
        #Take - COMMAND
        elif args[0].lower() == "!take" or args[0].lower() == "!t":

            if ccVars.cc_plus_card_amount > 0:

                if not ccVars.cc_plus_player_can_lay:

                    await fDU.send_Message_To_Channel(ccLanguage.cc_plus_card_player_cant_skip.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
                    fCU.log_In_Console("{} wants to sit out, but he cant sit out.".format(msg.author.name), "PRIVATE-COMS", "war")
                    return

                fCLU.Timer(10, fCMT.manage_timer, [ccVars, ccSettings, ccLanguage, client])

                await fDU.send_Message_To_Channel(ccLanguage.cc_plus_card_player_take.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
                fCU.log_In_Console("{} wants to sit out.".format(msg.author.name), "PRIVATE-COMS", "inf")
                return

            else:

                await fDU.send_Message_To_Channel(ccLanguage.cc_plus_card_player_cant_take.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel], ccSettings.cc_message_auto_delete)
                fCU.log_In_Console("{} wants to sit out, but he cant sit out.".format(msg.author.name), "PRIVATE-COMS", "war")
                return


        #------------------------------------------------------------------
        #Leave - COMMAND
        elif args[0].lower() == "!leave":

            await fCCPL.player_leave(msg, ccVars, ccSettings, ccLanguage)


        elif args[0].lower().startswith("!"):

            if msg.author in ccVars.cc_player_list:

                await fDU.send_Message_To_Channel(ccLanguage.cc_wrong_game_command.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel])
                fCU.log_In_Console("{} entered an unknown command. - {}".format(msg.author.name, str(msg.content)), "PRIVATE-COMS", "war")

    else:

        if len(args) <= 1:

            await fDU.send_Message_To_Channel(ccLanguage.cc_wrong_arguments.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel])
            fCU.log_In_Console("{} has forgotten arguments.".format(msg.author.name), "PRIVATE-COMS", "war")
            return


        #----------------------------------------------------------------------------------------
        #Shutdown Bot - COMMAND
        if args[1].lower() == "shutdown" and msg.channel.id == ccSettings.cc_channelID_bot_admin:

            fCU.log_In_Console("Shut down bot...", "SHUTDOWN-COM", "inf")
            await fDU.send_Message_To_Channel(ccLanguage.cc_shutdown_bot, [msg.channel])

            fCU.log_In_Console("Finished. See you soon...", "SHUTDOWN-COM", "inf")

            #Audio-Module
            await fCCVM.disconnect_voice(ccSettings, client)

            await client.logout()


        #---------------------------------------------------------------------------------
        #Join cc - COMMAND
        elif args[1].lower() == "join" and msg.channel.id == ccSettings.cc_channelID_join:

            if ccVars.cc_is_running:

                fCU.log_In_Console("{} tried to join cc. cc already running.".format(msg.author.name), "JOIN-COM","war")

                await fDU.send_Message_To_Channel(ccLanguage.cc_game_already_running.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel])

            else:

                if msg.author in ccVars.cc_player_list:

                    fCU.log_In_Console("{} tried to join cc. {} already joined.".format(msg.author.name, msg.author.name), "JOIN-COM","war")

                    await fDU.send_Message_To_Channel(ccLanguage.cc_user_already_joined.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel])

                else:

                    ccVars.cc_player_list.append(msg.author)

                    fCU.log_In_Console("{} joined cc. [{} Players]".format(msg.author.name, str(len(ccVars.cc_player_list))), "JOIN-COM","inf") if len(ccVars.cc_player_list) > 1 else fCU.log_In_Console("{} joined cc. [{} Player]".format(msg.author.name, str(len(ccVars.cc_player_list))), "JOIN-COM","inf")

                    await fDU.send_Message_To_Channel(ccLanguage.cc_user_joined_game.replace("[USER_ID]", "<@" + str(msg.author.id) + ">").replace("[PLAYER_JOINED_COUNT]", str(len(ccVars.cc_player_list))), [msg.channel])

            return


        #------------------------------------------------------------------------------------
        #Start - COMMAND
        elif args[1].lower() == "start" and msg.channel.id == ccSettings.cc_channelID_join:

            if ccVars.cc_is_running:

                fCU.log_In_Console("{} tried to start a game. Game already running.".format(msg.author.name), "START-COM", "war")

                await fDU.send_Message_To_Channel(ccLanguage.cc_game_already_running.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel])

            else:

                if len(ccVars.cc_player_list) >= ccSettings.cc_min_players:

                    await fUCCSG.on_Start_Game(msg, ccSettings.cc_cards_per_player, ccVars, ccSettings, ccLanguage, client)

                else:

                    fCU.log_In_Console("{} tried to start, but more players are needed for a start! At least {} players are needed for a start.".format(msg.author.name, str(ccSettings.cc_min_players)), "START-COM", "war")

                    await fDU.send_Message_To_Channel(ccLanguage.cc_more_players_needed.replace("[USER_ID]", "<@" + str(msg.author.id) + ">").replace("[MIN_PLAYER_COUNT]", str(ccSettings.cc_min_players)), [msg.channel])


        #--------------------------------------------------------------------------------------
        #Kick - COMMAND
        elif args[1].lower() == "kick" and msg.channel.id == ccSettings.cc_channelID_bot_admin:

            if len(args) > 2:

                if len(msg.mentions) > 0:

                    kick_user = await client.fetch_user(msg.mentions[0].id)

                    if kick_user in ccVars.cc_player_list:

                        if ccVars.cc_player_list[ccVars.cc_current_player] == kick_user:

                            await fDU.send_Message_To_Channel(ccLanguage.cc_cant_kick_current_player.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel])

                        else:

                            player_index = ccVars.cc_player_list.index(kick_user)

                            del ccVars.cc_player_hand[player_index]
                            del ccVars.cc_player_str_hand[player_index]

                            del ccVars.cc_player_card_str[player_index]
                            del ccVars.cc_card_messages[player_index]

                            del ccVars.cc_player_list[player_index]

                            ccVars.cc_player_display_list = fCCOF.generate_current_display(ccVars, ccSettings)


                            await fDU.send_Message_To_Channel(ccLanguage.cc_user_kicked, [msg.channel])

                            fCU.log_In_Console("{} kicked player {}".format(str(msg.author.name), str(kick_user.name)), "KICK-COM")

                    else:

                        await fDU.send_Message_To_Channel(ccLanguage.cc_kick_user_isnt_player.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel])

                else:

                    await fDU.send_Message_To_Channel(ccLanguage.cc_no_kick_user.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel])

            else:

                await fDU.send_Message_To_Channel(ccLanguage.cc_wrong_arguments.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel])


        #----------------------------------------------------------------------------------------
        #Stop - COMMAND
        elif args[1].lower() == "stop" and msg.channel.id == ccSettings.cc_channelID_bot_admin:

            if ccVars.cc_is_running:

                if msg.author in ccVars.cc_player_list:

                    fCU.log_In_Console("Stopping cc...", "STOP-COM", "inf")

                    ccVars.cc_is_running = False


                    #Print stop to all players
                    player_channels = []

                    for player in ccVars.cc_player_list:
                        player_channels.append(player.dm_channel)

                    await fDU.send_Message_To_Channel(ccLanguage.cc_game_stopped_by.replace("[USER_NAME]", str(msg.author.name)), player_channels, ccSettings.cc_message_auto_delete)


                    #Audio-Module
                    if ccSettings.cc_use_voice:
                        await fCCVM.say_text(ccLanguage.cc_game_stopped_by.replace("[USER_NAME]", str(msg.author.name)), ccSettings, client)
                        await fCCVM.disconnect_when_possible(ccSettings, client)


                    fCU.log_In_Console("Delete reaction-messages...", "STOP-COM", "inf")

                    #Delete wish-reaction, if possible:
                    if ccVars.cc_wish_react_message is not None:
                        try:
                            await ccVars.cc_wish_react_message.delete()
                        except:
                            pass


                    #Delete old reaction-message
                    if ccSettings.cc_play_with_reactions:
                        try:
                            await fCCOF.delete_lay_react_message(ccVars)
                        except:
                            pass



                    if ccSettings.cc_delete_old_messages:
                        fCU.log_In_Console("Delete card-messages...", "STOP-COM", "inf")

                        #Delete card-messages
                        for card_msg in ccVars.cc_card_messages:
                            try:
                                await card_msg.delete()
                            except:
                                pass


                    fCU.log_In_Console("Reset variables...", "STOP-COM", "inf")
                    fCCOF.reset_vars(ccVars)


                    fCU.log_In_Console("{} stopped cc.".format(msg.author.name), "STOP-COM", "inf")

                else:

                    await fDU.send_Message_To_Channel(ccLanguage.cc_game_cant_stopped.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel])

                    fCU.log_In_Console("{} tried to stop cc. But he does not play along!".format(msg.author.name), "STOP-COM", "war")

            else:

                await fDU.send_Message_To_Channel(ccLanguage.cc_no_game_running.replace("[USER_ID]", "<@" + str(msg.author.id) + ">"), [msg.channel])


@client.event
async def on_reaction_add(reaction, user):

    if user.bot:
        return

    if not ccVars.cc_is_running:
        return

    await fCCOREACT.on_Reaction_Add(reaction, user, ccVars, ccSettings, ccLanguage, client)


#---------------------------------------------------------------------------------

fCS.initialize_bot(ccVars, ccLanguage, ccSettings)


try:
    client.run(ccSettings.cc_bot_token)
except Exception as error:
    fCU.log_In_Console("{}".format(error), "START", "err")