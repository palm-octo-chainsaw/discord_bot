#gtts_cog.py
import discord
from discord.ext import commands
from gtts import gTTS


async def setup(bot):
    await bot.add_cog(SpeakCog(bot))

class SpeakCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc = None

    async def play(self):
        self.vc.play(discord.FFmpegPCMAudio(executable='./ffmpeg/bin/ffmpeg.exe',source='TTS.mp3'))

    # @commands.command(name='leave',aliases=['l', 'd'],help='Leave vc')
    # async def leave(self, bot):
    #     await self.bot.voice_clients[0].disconnect()

    @commands.command(pass_context=True,name='speak',aliases=['say'],help='Speak in voice chat the argument')
    async def speak(self, ctx, *args):
        channel = ctx.author.voice.channel

        if channel != None:
            if not self.vc:
                self.vc = await channel.connect()
            args = ' '.join(args)
            gTTS(text=args).save('TTS.mp3')
            await self.play()
            print('sayed it')
        else:
            await ctx.send('Ай влез ма')
        
