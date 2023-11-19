import nextcord
from nextcord.ext import commands

token_file = open("token.txt", "r")
token = token_file.read()
token_file.close()
bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="Send a message to someone", force_global = True, dm_permission = True)
async def send(interaction: nextcord.Interaction, ide: int = nextcord.SlashOption(required=True), message: str = nextcord.SlashOption(required=True)):
    await interaction.response.defer()
    mr = bot.get_user(ide)
    mr.send(message)

bot.run(token)