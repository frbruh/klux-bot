
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from setuptools import Command

client = commands.Bot(command_prefix="1")
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    print('Bot logged as {0.user}'.format(client))

@slash.slash(
    name="ping",
    description="Replies with the bots latency",
    guild_ids=[883746608905334835]
)
async def _ping(ctx):
    await ctx.send(f'The bots ping is {round(client.latency * 1000)}ms')

@slash.slash(
    name="Announce",
    description="To announce something important",
    guild_ids=[883746608905334835],
    options=[
        create_option(
            name="title",
            description="Title for the message",
            required=True,
            option_type=3
        ),
        create_option(
            name="description",
            description='Give the description for the Announcement',
            required=True,
            option_type=3
        )

    ]
)
async def _Announce(ctx, title:str, description:str):
    embed = discord.Embed(title=title, description=description, color=discord.Color.red())
    announcementicon = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flaticon.com%2Ffree-icon%2Fannouncement_1870127&psig=AOvVaw1CBmDqo9_Hf6o7vFXDwgR7&ust=1648654608469000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPC3gZbT6_YCFQAAAAAdAAAAABAD',
    embed.set_thumbnail(url=announcementicon)
    embed.set_footer(icon_url='https://img.icons8.com/ios-glyphs/344/verified-account--v1.png', text = "Posted By A certified Mod")
    await ctx.send(embed)

@slash.slash(
    name="lolxd",
    description="A LolxD message",
    guild_ids=[883746608905334835],
    options=[
        create_option(
            name="type",
            description="LolxD msg",
            required=True,
            option_type=3,
            choices=[
                create_choice(
                    name="Dank",
                    value="Dank"
                ),
                create_choice(
                    name="Humour",
                    value="Humour"
                ),
                create_choice(
                    name="other",
                    value="Other"
                )
            ]
        ),
        create_option(
            name="description",
            description="The description of the message",
            required=True,
            option_type=3
        ),
        create_option(
            name="link",
            description="Link",
            required=True,
            option_type=3      
        )
    ]
)
async def _lolxd(ctx,  type:str, description:str, link:str):
    embed = discord.Embed(title ='LolxD Joke', description = type, color = discord.Color.blue())
    embed.add_field(name = 'Description', value = description, inline = True)
    embed.add_field(name = "Link", value = link, inline=False)
    Memeimg = 'https://images-ext-1.discordapp.net/external/pujWKcOs1hxT8nKdvxFm2iXA_rs8Sbxu9p0u0xywS_I/%3Fwidth%3D371%26height%3D371/https/images-ext-1.discordapp.net/external/sEev9rpzR51thKMUIm7PbgzWd4C_9bf9sNI2xpR5Be4/%253Fsize%253D4096/https/cdn.discordapp.com/avatars/270904126974590976/d60c6bd5971f06776ba96497117f7f58.png'
    embed.set_thumbnail(url =Memeimg)
    embed.set_footer(icon_url='https://img.icons8.com/ios-glyphs/344/verified-account--v1.png', text = "Posted By A certified Memer")
    await ctx.send(embed=embed)

client.run('OTI0MTk0NDU3MDk4Nzg4ODk0.YcbBKQ.pa4C3eZP79QCEdVcQX08zrH4sOU')