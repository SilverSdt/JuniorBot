import discord
from discord.ext import commands
from discord.commands import slash_command
import sys

from Junior import Junior

def start(token: str):

    client = commands.Bot()

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    """
    @client.event
    async def on_message(message):
        if message.author == client.user: return
    """
        
    @client.slash_command(name = "lvl", description = "Donne le lvl de votre Junior")
    async def stats(ctx):
        junior: Junior = Junior.load_junior(str(ctx.author))
        await ctx.respond(junior.__str__())
        
    @client.slash_command(name = "change_name", description = "Change le nom de votre Junior")
    async def change_name(ctx, new_name: str):
        junior: Junior = Junior.load_junior(str(ctx.author))
        junior.name = new_name
        junior.save_junior()
        if ctx.author.nick == None: user: str = str(ctx.author).split("#")[0]
        else: user: str = ctx.author.nick
        
        await ctx.respond(f"Le nom du Junior de {user} à était défini à {new_name}.")
        
    @client.slash_command(name = "give_exp", description = "donne de l'exp aux junior d'un membre")
    @commands.has_permissions(administrator = True)
    async def give_exp(ctx, member: discord.User, exp: int):
        if isinstance(exp, int):
            junior: Junior = Junior.load_junior(str(member))
            old_level: int = junior.lvl
            junior += exp
            junior.save_junior()
            new_level: int = junior.lvl
            
            if member.nick == None: user: str = str(member).split("#")[0]
            else: user: str = ctx.author.nick
            
            if new_level != old_level:
                channel = client.get_channel(956592548598653019)
                await channel.send(f"<@{member.id}>, votre {junior.name} est maintenant de niveau {new_level} ! Félicitation !")
            
            await ctx.respond(f"{junior.name} de {junior.owner} gagne {exp} exp.")
        else:
            await ctx.respond("Veuillez indiquer une valeur d'exp valide (int)..")
        
    

    client.run(token)
    
if __name__ == '__main__':
    eval(sys.argv[1])
    