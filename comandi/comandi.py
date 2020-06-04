import discord
from discord.ext import commands

from core.paginator import EmbedPaginatorSession

class ServStatus(commands.Cog):
      def __init__(self, bot):
            self.bot = bot
            
      @commands.command(aliases=["accetot"])
      async def accetto(self, ctx):
            """<#595319716344758291>"""
            member = ctx.author
            role = discord.utils.find(lambda r: r.name == "Membri",ctx.guild.roles)
            await member.add_roles(role)

      @commands.command(aliases=["stato"])
      async def statomc(self, ctx):
            """Mostra lo stato del server Minecraft."""
            response = await self.bot.session.get("http://statomc.vincysuper07.cf/api.php")
            status = (await response.content.readline()).decode('UTF-8')
            embed = discord.Embed(title = "Server Minecraft: mc.Vincysuper07.cf", description = f"Al momento il server è {status}")
            if status == "OFFLINE.":
                embed.color = discord.Color.red()
            else:
                embed.color = discord.Color.green()
            await ctx.send(embed=embed)
            
      @commands.command(aliases=["help"])
      async def comandi(self,ctx):
            """Mostra i comandi del bot"""
            embed = discord.Embed(title="Tags", description=f"{ctx.prefix}tag <nome> - Usa un tag!\n{ctx.prefix}tags add <nome> <risposta> - Crea un tag!", color = discord.Color.green())
            embed1 = discord.Embed(title="Divertimento", description=f"{ctx.prefix}inspiro(bot) - Mostra un immagine a caso da InspiroBot.me\n{ctx.prefix}choose <primo oggetto> <secondo oggetto> Scegli tra 2 oggetti!\n{ctx.prefix}roll - Lancia un dado\n{ctx.prefix}flip - Lancia una moneta\n{ctx.prefix}rps - Sasso, Carta, o Forbici?\n{ctx.prefix}8ball <domanda>? - La 8Ball risponderà a ogni tua domanda!\n{ctx.prefix}reverse <messaggio> - !otseT out li etrevnI\n{ctx.prefix}meme - Ti da una meme a caso\n{ctx.prefix}roast <persona> - Insulta la persona menzionata\n{ctx.prefix}smallcaps <messaggio> - ᴄᴏɴᴠᴇʀᴛᴇ ɪʟ ᴛᴜᴏ ᴛᴇꜱᴛᴏ ᴀ ᴜɴ ᴍᴀɪᴜꜱᴄᴏʟᴏ ᴘɪᴄᴄᴏʟᴏ!", color = discord.Color.green())
            embed2 = discord.Embed(title="Hastebin", description=f"{ctx.prefix}hastebin <messaggio> - Inserisce il tuo testo su Hastebin", color = discord.Color.green())
            embed3 = discord.Embed(title="Benvenuto", description=f"{ctx.prefix}welcomer <chatincuiappareilmessaggio> <contenutomessaggio> - Da un messaggio di benvenuto  ogni utente che entra nel server", color = discord.Color.green())
            embed4 = discord.Embed(title="Moderazione", description=f"{ctx.prefix}purge <numero> - Elimina una quantità da 1 a 100 di messaggi\n{ctx.prefix}kick <persona> - Espelle un membro del server\n{ctx.prefix}mute <persona> - Muta una persona nel server\n{ctx.prefix}unmute <persona> - Smuta una persona nel server\n{ctx.prefix}nuke - Eimina tutti i messaggi di una chat\n{ctx.prefix}ban <persona> - Banna una persona dal server\n{ctx.prefix}unban <persona> - Revoca il ban a una persona del server", color = discord.Color.green())
            embed5 = discord.Embed(title="Annunci", description=f"{ctx.prefix}announcement start - crea un annuncio interattivo\n{ctx.prefix}announcement quick <canale> [ruolo] <messaggio> - Un vecchio modo per creare un'annuncio", color = discord.Color.green())
            embed6 = discord.Embed(title="Musica", description=f"{ctx.prefix}join - Entra in un canale vocale\n{ctx.prefix}leave - Esce da un canale vocale\n{ctx.prefix}now - Mostra la canzone in riproduzione\n{ctx.prefix}pause - Mette una canzone in pausa\n{ctx.prefix}play <link-canzone> - Riproduce una canzone\n{ctx.prefix}queue - mostra la coda\n{ctx.prefix}remove - Rimuove una canzone dalla coda\n{ctx.prefix}resume - Riprende una canzone dopo averla messa in pausa\n{ctx.prefix}shuffle - Attiva la riproduzione casuale\n{ctx.prefix}skip - Salta una canzone passando a quella successiva\n{ctx.prefix}stop - Ferma la riproduzione della musica, ma pulisce la coda\n{ctx.prefix}summon - Lo stesso di v!play, entra in un canale vocale\n{ctx.prefix}volume <volume> - Cambia il volume del bot", color=discord.Color.green())
            embed7 = discord.Embed(title="Altro", description=f"{ctx.prefix}embed send <titolo> <Descrizione> - Invia un messaggio incorporato\n{ctx.prefix}embed color <hexcode> - Cambia il colore del tuo messaggio incorporato\n{ctx.prefix}welcomer <chat> <messaggio> - Crea un messaggio di benvenuto!\n{ctx.prefix}reactionrole add <id_messaggio> <ruolo> <emoji> - Inserisce una reazione ad un messaggio, che servirà per ricevere un ruolo!\n{ctx.prefix}stato - Controlla se il server Minecraft di Vincy è online!\n{ctx.prefix}comandi - Mostra questo messaggio!\n{ctx.prefix}help - Mostra questo messaggio!", color = discord.Color.green())
            embeds = []
            embed_list = [embed, embed1, embed2, embed3, embed4, embed5, embed6, embed7]
            for embed in embed_list:
                embed.set_footer(text=f"Usa le frecce per cambiare pagina. • Prefix: {ctx.prefix}")
                embed.set_author(name="VincyBot07", icon_url=self.bot.user.avatar_url)
                embeds.append(embed)
            session = EmbedPaginatorSession(ctx, *embeds)
            await session.run()

      @commands.command(aliases=["helpmod", "helpm", "hmod", "hadmin", "helpa", "hm"])
      async def helpadmin(self,ctx):
            await ctx.send_help()

def setup(bot):
      bot.add_cog(ServStatus(bot))
