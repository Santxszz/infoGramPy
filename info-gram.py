import discord
from discord.ext import commands
from instagramy import InstagramUser
from instagramy.core.cache import clear_caches

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado - [Bot: {bot.user}] | [ID: {bot.user.id}] ')
    activity = discord.Game(name="by: Santxsz#0363", type=2)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def clearCache(ctx):
    if ctx.message.author.id == 924824138173022270:
        clear_caches()
    else:
        await ctx.message.channel.send('Você não tem permissão!')

@bot.command()
async def info(ctx):
    infoEmbed = discord.Embed(color=0x0f0f0f, description='Todas informações do bot.')
    infoEmbed.set_author(name='{} - Informações'.format(bot.user.name), icon_url=ctx.message.author.avatar.url)
    infoEmbed.set_thumbnail(url=ctx.message.author.avatar.url)
    infoEmbed.add_field(name='Linguagem', value='```Python 3```', inline= True)
    infoEmbed.add_field(name='Versão', value='```1.0```', inline= True)
    infoEmbed.add_field(name='Desenvolvedor', value='```Santxsz#0363```', inline= True)

    await ctx.send(embed=infoEmbed)

@bot.command()
async def infogram(ctx, args1):
    user = args1
    UsuarioDD = InstagramUser(user)
    avatarUser = UsuarioDD.profile_picture_url
    # print(UsuarioDD.posts_display_urls)
    verificado = ''
    if UsuarioDD.is_verified == True:
        verificado = 'Verificado(a)'
    else:
        verificado = 'Não Verificado(a)'
    
    embedVar = discord.Embed(color=0x0f0f0f)

    embedVar.set_image(url='https://cdn.discordapp.com/attachments/1013227735851749408/1015307882390097930/unknown.png')
    embedVar.set_thumbnail(url=avatarUser)
    embedVar.set_author(name='@{}'.format(user), icon_url=avatarUser)

    embedVar.add_field(name="Usuário", value="```{}```".format(UsuarioDD.fullname), inline=False)
    embedVar.add_field(name="Status", value='```{}```'.format(verificado), inline= False)
    embedVar.add_field(name="Seguidores", value="```{}```".format(UsuarioDD.number_of_followers), inline=True)
    embedVar.add_field(name="Seguindo", value='```{}```'.format(UsuarioDD.number_of_followings), inline= True)
    embedVar.add_field(name="Posts", value='```{}```'.format(UsuarioDD.number_of_posts), inline= True)
    await ctx.channel.send(embed=embedVar)

bot.run('')