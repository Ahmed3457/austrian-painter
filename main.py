import nextcord
from nextcord.ext import commands
from lib import gen_scramble, cubes

token_file = open("token.txt", "r")
token = token_file.read()
token_file.close()

bot = commands.Bot()
intents = nextcord.Intents.all()
test_servers = [937639594030153758]
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(description = "Scramble a cube", force_global = True, dm_permission = True, guild_ids=test_servers)
async def scramble(interaction: nextcord.Interaction, length: int = nextcord.SlashOption(description = "The length of the scramble.", required = False), cube: str = nextcord.SlashOption(description = "The cube you want to scramble.", required = False, choices = cubes.keys())):
    await interaction.response.defer()
    if length > 50 or length == None or length < 1:
        length = 20
    if cube == None:
        cube = "333"
    scramble = gen_scramble(length=length, cube=cube)
    await interaction.followup.send(f"Here is your scramble <@{interaction.user.id}>: ```{scramble}```")
    
bot.run(token)