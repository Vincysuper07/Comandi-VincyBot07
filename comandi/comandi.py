import discord
from discord.ext import commands

from core.paginator import EmbedPaginatorSession

class ServStatus(commands.Cog):
      def __init__(self, bot):
            self.bot = bot
            
      @commands.command()
      async def comandi(self,ctx):
            embed = discord.Embed(title="Lista comandi", description="Prefix: v!\n**Tags**\nv!tag <nome> - Usa un tag!\nv!tags add <nome> <risposta> - Crea un tag!", color = discord.Color.green())
            embed1 = discord.Embed(title="Lista comandi", description="Prefix: v!\n**Embed**\nv!embed send <titolo> <Descrizione> - Invia un messaggio incorporato\nv!embed color <hexcode> - Cambia il colore del tuo messaggio incorporato", color = discord.Color.green())
            embed2 = discord.Embed(title="Lista comandi", description="Prefix: v!\n**Divertimento**\nv!choose <primo oggetto> <secondo oggetto> Scegli tra 2 oggetti!\nv!roll - Lancia un dado\nv!flip - Lancia una moneta\nv!rps - Sasso, Carta, o Forbici?\nv!8ball <domanda>? - La 8Ball risponderà a ogni tua domanda!\nv!reverse <messaggio> - !otseT out li etrevnI\nv!meme - Ti da una meme a caso\nv!roast <persona> - Insulta la persona menzionata\nv!smallcaps <messaggio> - ᴄᴏɴᴠᴇʀᴛᴇ ɪʟ ᴛᴜᴏ ᴛᴇꜱᴛᴏ ᴀ ᴜɴ ᴍᴀɪᴜꜱᴄᴏʟᴏ ᴘɪᴄᴄᴏʟᴏ!", color = discord.Color.green())
            embed3 = discord.Embed(title="Lista comandi", description="Prefix: v!\n**Hastebin**\nv!hastebin <messaggio> - Inserisce il tuo testo su Hastebin", color = discord.Color.green())
            embed4 = discord.Embed(title="Lista comandi", description="Prefix: v!\n**Benvenuto**\nv!welcomer <chatincuiappareilmessaggio> <contenutomessaggio> - Da un messaggio di benvenuto  ogni utente che entra nel server", color = discord.Color.green())
            embed5 = discord.Embed(title="Lista comandi", description="Prefix: v!\n**Moderazione**\nv!purge <numero> - Elimina una quantità da 1 a 100 di messaggi\nv!kick <persona> - Espelle un membro del server\nv!mute <persona> - Muta una persona nel server\nv!unmute <persona> - Smuta una persona nel server\nv!nuke - Eimina tutti i messaggi di una chat\nv!ban <persona> - Banna una persona dal server\nv!unban <persona> - Revoca il ban a una persona del server", color = discord.Color.green())
            embed6 = discord.Embed(title="Lista comandi", description="Prefix: v!\n**Annunci**\nv!announcement start - crea un annuncio interattivo\nv!announcement quick <canale> [ruolo] <messaggio> - Un vecchio modo per creare un'annuncio", color = discord.Color.green())
            embed.set_author(name="VincyBot07", icon_url="https://vincybot07.vincysuper07.cf/assets/images/immagine-VincyBot07-rotonda.png")
            embed1.set_author(name="VincyBot07", icon_url="https://vincybot07.vincysuper07.cf/assets/images/immagine-VincyBot07-rotonda.png")
            embed2.set_author(name="VincyBot07", icon_url="https://vincybot07.vincysuper07.cf/assets/images/immagine-VincyBot07-rotonda.png")
            embed3.set_author(name="VincyBot07", icon_url="https://vincybot07.vincysuper07.cf/assets/images/immagine-VincyBot07-rotonda.png")
            embed4.set_author(name="VincyBot07", icon_url="https://vincybot07.vincysuper07.cf/assets/images/immagine-VincyBot07-rotonda.png")
            embed5.set_author(name="VincyBot07", icon_url="https://vincybot07.vincysuper07.cf/assets/images/immagine-VincyBot07-rotonda.png")
            embed6.set_author(name="VincyBot07", icon_url="https://vincybot07.vincysuper07.cf/assets/images/immagine-VincyBot07-rotonda.png")
            embeds = []
            embed_list = [embed, embed1, embed2, embed3, embed4, embed5, embed6]
            for embed in embed_list:
                embeds.append(embed)
            session = EmbedPaginatorSession(ctx, *embeds)
            await session.run()
            
def setup(bot):
      bot.add_cog(ServStatus(bot))
