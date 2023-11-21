import nextcord
from nextcord.ext import commands
from lib import gen_scramble, cubes

token_file = open(
    "token.txt", 
    "r"
    )
token = token_file.read()
token_file.close()

bot = commands.Bot()
intents = nextcord.Intents.all()
test_servers = [937639594030153758]
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(
    description = "Generate a scramble for the chosen cube.", 
    force_global = True, 
    dm_permission = True, 
    guild_ids=test_servers
)
async def scramble(
    interaction: nextcord.Interaction, 
    length: int = nextcord.SlashOption(
        description = "The length of the scramble, 50 at maximum.", 
        required = False
    ), 
    cube: str = nextcord.SlashOption(
        description = "The cube you want to scramble.", 
        required = False, 
        choices = cubes.keys()
    ),
    count: int = nextcord.SlashOption(
        description = "The amount of scrambles you want, 25 at maximum.",
        required = False
    )
):
    await interaction.response.defer()

    user = interaction.user
    scramble = None
    h = 0

    embed = nextcord.Embed()
    embed.set_footer(
        text = f"{user.name}", 
        icon_url = user.avatar.url
        )

    if length == None or length > 50 or length < 1:
        length = 20

    if cube == None:
        cube = "333"

    if count == None or count < 1:
        count = 1

    if count > 25:
        count = 25

    if count > 1:
        embed.title = "Here are your scrambles:"

    else:
        embed.title = "Here is your scramble:"
    
    for i in range(count):
        h += 1
        scramble = gen_scramble(
            length=length, 
            cube=cube
            )
        if count > 1:
            embed.add_field(name=f"{h}", value=scramble[0])
        else:
            embed.description = scramble[0]

    await interaction.followup.send( embed = embed )
bot.run(token)