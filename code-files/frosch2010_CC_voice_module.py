
import discord
import asyncio
from gtts import gTTS
import os
import sys


import frosch2010_Console_Utils as fCU


async def say_text(text, ccSettings, client):

    voice_channel = client.get_channel(ccSettings.cc_channelID_voice)
    voice_client = discord.utils.get(client.voice_clients, guild=client.get_guild(ccSettings.cc_ServerID))

    if voice_client is None or not voice_client.is_connected():
        fCU.log_In_Console("Join the voice channel...","VOICE-SAY", "inf")
        try:
            vc = await voice_channel.connect()
        except Exception as e:
            fCU.log_In_Console("Cant join the voice channel! - {}".format(str(e)), "VOICE-SAY", "err")

    else:
        vc = voice_client


    if vc.is_playing():
        vc.stop()

    fCU.log_In_Console("The following is output in the voice channel: {}".format(str(text)),"VOICE-SAY", "inf")

    output = gTTS(text=text, lang=ccSettings.cc_voice_language, slow=False)
    output.save(sys.argv[0].replace(os.path.basename(sys.argv[0]), "") + "voice_text.mp3")


    #Check os
    if os.name == "nt":

        try:
            vc.play(discord.FFmpegPCMAudio(executable=ccSettings.cc_ffmpeg_path, options="-nostats -loglevel quiet", source=sys.argv[0].replace(os.path.basename(sys.argv[0]), "") + "voice_text.mp3"))
        except Exception as e:
            fCU.log_In_Console("When trying to say something about the voice channel, an error occurred. - {}".format(str(e)),"VOICE-SAY", "err")

    else:
        
        try:
            vc.play(discord.FFmpegPCMAudio(options="-nostats -loglevel quiet", source=sys.argv[0].replace(os.path.basename(sys.argv[0]), "") + "voice_text.mp3"))
        except Exception as e:
            fCU.log_In_Console("When trying to say something about the voice channel, an error occurred. - {}".format(str(e)),"VOICE-SAY", "err")



async def disconnect_when_possible(ccSettings, client):

    fCU.log_In_Console("Leave the voice channel as soon as possible","VOICE-DIS-POS", "inf")

    voice_client = discord.utils.get(client.voice_clients, guild=client.get_guild(ccSettings.cc_ServerID))

    if voice_client is None or not voice_client.is_connected():
        return

    while voice_client.is_playing():
        await asyncio.sleep(.1)

    await voice_client.disconnect()

    os.remove(sys.argv[0].replace(os.path.basename(sys.argv[0]), "") + "voice_text.mp3")



async def disconnect_voice(ccSettings, client):

    fCU.log_In_Console("Leave the voice channel...","VOICE-DIS", "inf")

    voice_client = discord.utils.get(client.voice_clients, guild=client.get_guild(ccSettings.cc_ServerID))

    if voice_client is None or not voice_client.is_connected():
        return

    await voice_client.disconnect()

    os.remove(sys.argv[0].replace(os.path.basename(sys.argv[0]), "") + "voice_text.mp3")