import discord
from discord.ext import commands
import os
from utils.scraper import scraper
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv("BOT_TOKEN")
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
bot.help_command = None


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def livescore(ctx):
    data = scraper()
    if(data is None):
       await ctx.reply("Something went wrong...")
    else:
        if(data['state'] == "scheduled"):
            embed = discord.Embed(title=f'Scheduled : {data["team1_name"]} vs {data["team2_name"]}', color=discord.Color(0x2f3136) , url=f'https://www.espncricinfo.com{data["url"]}')
            embed.add_field(name='Match Details', value=data['match_details'], inline=False)
            embed.add_field(name='Tournament Info', value=data['tournament_info'], inline=False)
            embed.add_field(name='Starts In' , value=data['starts_in'])
            
            await ctx.reply(embed=embed)


        elif (data['state'] == 'live'):
            embed = discord.Embed(title=f'{data["team1_name"]} vs {data["team2_name"]}', color=discord.Color(0x2f3136) , url=f'https://www.espncricinfo.com{data["url"]}' , description = data['match_comment'])
            embed.add_field(name='Tournament Info', value=data['tournament_info'], inline=False)
            embed.add_field(name='Team 1 Score', value=data['team1_score'], inline=True)
            embed.add_field(name='⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀' , value='⠀')
            embed.add_field(name='Team 2 Score', value=data['team2_score'], inline=True)
            embed.add_field(name='Team 1 Overs', value=data['team1_over'], inline=True)
            embed.add_field(name='⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀' , value='⠀')
            embed.add_field(name='Team 2 Overs', value=data['team2_over'], inline=True)

            await ctx.reply(embed=embed)


        elif (data['state'] == 'result'):
            embed = discord.Embed(title=f'{data["team1_name"]} vs {data["team2_name"]}', color=discord.Color(0x2f3136) , url=f'https://www.espncricinfo.com{data["url"]}' , description = data['match_result'])
            embed.add_field(name='Match Details', value=data['match_details'], inline=False)
            embed.add_field(name='Tournament Info', value=data['tournament_info'], inline=False)
            embed.add_field(name='Team 1 Score', value=data['team1_score'], inline=True)
            embed.add_field(name='⠀' , value='⠀')
            embed.add_field(name='Team 2 Score', value=data['team2_score'], inline=True)
            embed.add_field(name='Team 1 Overs', value=data['team1_over'], inline=True)
            embed.add_field(name='⠀' , value='⠀')
            embed.add_field(name='Team 2 Overs', value=data['team2_over'], inline=True)

            await ctx.reply(embed=embed)
@bot.command()
async def generate(ctx):
    await ctx.reply(file=discord.File('cricket_data.csv'))

@bot.command()
async def help(ctx):
    await ctx.reply('**Commands** :\n- `!livescore` -> Information about the latest match\n- `!generate` -> csv file showing all the fetched matches\n- `!help` -> shows this menu')



bot.run(bot_token)