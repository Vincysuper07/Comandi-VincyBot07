import discord
from discord.ext import commands

class ServStatus(commands.Cog):
      def __init__(self, bot):
            self.bot = bot
      @commands.command()
      async def stato(self,ctx):
            embed=discord.Embed(title="Lista comandi", description="Prefix: v!", color=0x7289da)
            embed.set_author(name="VincyBot07", icon_url="https://vincybot07.vincysuper07.cf/assets/images/immagine-VincyBot07-rotonda.png")
            embed.add_field(name="Tags", value="v!tag <nome> - Usa un tag!\nv!tags add <nome> <risposta> - Crea un tag!", inline=True)
            embed.add_field(name="Embed", value="v!embed send <titolo> <Descrizione> - Invia un messaggio incorporato\nv!embed color <hexcode> - Cambia il colore del tuo messaggio incorporato", inline=True)
            embed.add_field(name="Divertimento", value="v!choose <primo oggetto> <secondo oggetto> Scegli tra 2 oggetti!\nv!roll - Lancia un dado\nv!flip - Lancia una moneta\nv!rps - Sasso, Carta, o Forbici?\nv!8ball <domanda>? - La 8Ball risponderà a ogni tua domanda!\nv!reverse <messaggio> - !otseT out li etrevnI\nv!meme - Ti da una meme a caso\nv!roast <persona> - Insulta la persona menzionata\nv!smallcaps <messaggio> - ᴄᴏɴᴠᴇʀᴛᴇ ɪʟ ᴛᴜᴏ ᴛᴇꜱᴛᴏ ᴀ ᴜɴ ᴍᴀɪᴜꜱᴄᴏʟᴏ ᴘɪᴄᴄᴏʟᴏ!", inline=True)
            embed.add_field(name="Hastebin", value="v!hastebin <messaggio> - Inserisce il tuo testo su Hastebin", inline=True)
            embed.add_field(name="Benvenuto", value="v!welcomer <chatincuiappareilmessaggio> <contenutomessaggio> - Da un messaggio di benvenuto  ogni utente che entra nel server", inline=True)
            embed.add_field(name="Moderazione", value="v!purge <numero> - Elimina una quantità da 1 a 100 di messaggi\nv!kick <persona> - Espelle un membro del server\nv!mute <persona> - Muta una persona nel server\nv!unmute <persona> - Smuta una persona nel server\nv!nuke - Eimina tutti i messaggi di una chat\nv!ban <persona> - Banna una persona dal server\nv!unban <persona> - Revoca il ban a una persona del server", inline=True)
            embed.add_field(name="Annunci", value="v!announcement start - crea un annuncio interattivo\nv!announcement quick <canale> [ruolo] <messaggio> - Un vecchio modo per creare un'annuncio", inline=True)
            await ctx.send(embed=embed)
            
def setup(bot):
      bot.add_cog(ServStatus(bot))
