import discord
import discord.member
import asyncio


import frosch2010_Console_Utils as fCU


async def wish_choose_color(user, ccVars, ccSettings, ccLanguage):

    ccVars.cc_wish_react_message = await user.send(ccLanguage.cc_please_choose_wish_color_react.replace("[USER_ID]", "<@" + str(user.id) + ">"))

    try:
        await ccVars.cc_wish_react_message.add_reaction("🟥")
    except:
        fCU.log_In_Console("A Reaction could not be added to a message.", "WISH-COLOR", "war")

    try:
        await ccVars.cc_wish_react_message.add_reaction("🟨")
    except:
        fCU.log_In_Console("A Reaction could not be added to a message.", "WISH-COLOR", "war")

    try:
        await ccVars.cc_wish_react_message.add_reaction("🟩")
    except:
        fCU.log_In_Console("A Reaction could not be added to a message.", "WISH-COLOR", "war")

    try:
        await ccVars.cc_wish_react_message.add_reaction("🟦")
    except:
        fCU.log_In_Console("A Reaction could not be added to a message.", "WISH-COLOR", "war")