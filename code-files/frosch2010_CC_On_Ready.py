import discord

import frosch2010_Console_Utils as fCU


async def on_ready(client):

    fCU.log_In_Console("Logged in as user {}".format(client.user.name), "ON-READY", "inf")