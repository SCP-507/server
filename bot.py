import discord
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import youtube_dl
import os
import json
from discord import Spotify

client = commands.Bot( command_prefix = '.')
client.remove_command('help')
id=client.get_guild (630475494936019015)
os.chdir(r'C:\Users\Acer\OneDrive\Рабочий стол\server')

#spam
@client.command(pass_context=True)
@commands.has_permissions( administrator = True )
async def rak(ctx, amount = 10 ):
	await ctx.message.delete(delay = 0.6)
	await ctx.send('Рак лох')

#play
@client.command(pass_context=True)
async def play(ctx, url):
    if not client.is_voice_connected(ctx.message.server):
        voice = await client.join_voice_channel(ctx.message.author.voice_channel)
    else:
        voice = client.voice_client_in(ctx.message.server)

    player = await voice.create_ytdl_player(url, after=toggle_next)
    await songs.put(player)
# error
@client.event
async def on_command_error(ctx,error):
  	print(error)

#connection

@client.event
async def on_ready():
	print( 'Бот подключен' )

	await client.change_presence(activity=discord.Game(name="Уь ептубупшоп фнёо, ема сбтщйхспглй юупдп, оё убл мй?"))
#hello
@client.command( pass_context = True )
async def hello(ctx):
	await ctx.message.delete(delay = 0.6)
	await ctx.send('Здравствуйте, я прибыл из компании КиберЛайф , чтоб украсть ваши печеньки')

#clear message
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def clear(ctx, amount = 100 ):
	await ctx.channel.purge( limit = amount )

#kick
@client.command( pass_context = True )
@commands.has_permissions(administrator = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.message.delete(delay = 0.7)
    if reason != None:
        await ctx.send(member.mention)
    else:
        await ctx.send(f' кикнут {member.mention} за педофилию ')
#ban
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def ban(ctx, member: discord.Member, * , reason=None):
	await ctx.message.delete(delay = 0.6)

	await member.ban(reason=reason)
	await ctx.send(f'Забанен {member.mention}')
#users
@client.command( pass_context = True)
async def users(ctx):
	await ctx.message.delete(delay = 0.6)
	id = client.get_guild(630475494936019015)
	await ctx.send(f"""Количество псих-больных: {id.member_count}""")


#unbban
@client.command()
@commands.has_permissions( administrator = True )
async def unban(ctx,*,member_id = 0):
    await ctx.message.delete(delay = 0.7)
    banned_users= await ctx.guild.bans()
    for ban_entry in banned_users:
        if ban_entry.user.id == member_id:
            await ctx.guild.unban(ban_entry.user)
            await ctx.send( f'разбанен {ban_entry.user.mention}')
        return
#mute 
@client.command(pass_context=True)
@commands.has_permissions( administrator = True )
async def mute(ctx, member:discord.Member):
	await ctx.message.delete(delay = 0.7)
	mute_role=discord.utils.get(ctx.message.guild.roles, name = 'mute')
	await member.add_roles( mute_role)
	vazno=discord.utils.get(ctx.message.guild.roles, name='Важный человек')
	await member.remove_roles(vazno)

#unmute
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def unmute(ctx, member:discord.Member):
	await ctx.message.delete(delay=0.7)
	mute_role=discord.utils.get(ctx.message.guild.roles, name='mute')
	await member.remove_roles(mute_role)
	await ctx.send(f'{member.mention} выпустили из изолятора')
	vazno=discord.utils.get(ctx.message.guild.roles, name='Важный человек')
	await member.add_roles(vazno)


	








#help
@client.command( pass_context= True)
async def help(ctx):
	author = ctx.message.author
	await ctx.message.delete(delay = 0.7)


	embed = discord.Embed(
		colour = discord.Colour.orange()
	)


	embed.set_author(name= 'Главные команды (их больше и не будет)')
	embed.add_field(name='kick', value='Выгоняет с сервера и дает билет нахуй', inline=False)
	embed.add_field(name='ban', value='Отправляет в дурку навечно', inline=False)
	embed.add_field(name='unban', value='Выводит из дурки', inline=False)
	embed.add_field(name='clear', value='Чистит вилкой чат', inline=False)
	embed.add_field(name='naher', value='Просто существует', inline=False)
	embed.add_field(name='users', value='Показывает количество человек в палате', inline=False)
	embed.add_field(name='anime', value='Дает вам статус и престиж', inline=False)
	embed.add_field(name='mute', value='Дает путевку в изолятор', inline=False)
	embed.add_field(name='unmute', value='Выпускает из изолятора', inline=False)
	embed.add_field(name='scp', value='Хз, что-то произойдет', inline=False)
	embed.add_field(name='kiss', value='50% шанс, что потом тебе дадут по лицу, после этой команды', inline=False)
	embed.add_field(name='punch', value='MUDA MUDA', inline=False)
	embed.add_field(name='spotify', value='Узнаем то, что и так известно', inline=False)
	embed.add_field(name='avatar', value='Коммунизм', inline=False)






	await ctx.send(author, embed=embed)

#auto role
@client.event
async def on_member_join(member):
	channel = client.get_channel( 630542809627099158 )

	role = discord.utils.get( member.guild.roles, id=630542872055119873)
	await member.add_roles(role)
	await channel.send(f'{member.mention} Прибыл в дурку')



#Anime
@client.command( pass_context = True )
async def anime(ctx):
	await ctx.message.delete(delay = 0.6)
	await ctx.send('Аниме эт моя жизнь БЛЯТЬ')

#roles for voice
@client.event
async def on_voice_state_update(member, before, after):
    if not before.channel and after.channel:
        role = discord.utils.get(member.guild.roles, name="Сидит в войсе")
        await member.add_roles(role)
    elif before.channel and not after.channel:
        role = discord.utils.get(member.guild.roles, name="Сидит в войсе")
        await member.remove_roles(role)




#naher
@client.command( pass_context = True )
async def naher(ctx):
	await ctx.message.delete(delay = 0.6)
	await ctx.send('Ну да, ну да , пошел я нахер')


#scp
@client.command( pass_context = True )
async def scp(ctx):
	await ctx.message.delete(delay = 0.6)
	await ctx.send('SCP SOSAAT ')







#commands for fun
@client.command(pass_context=True)
async def kiss(ctx, member:discord.Member):
	await ctx.message.delete(delay = 0.6)
	await ctx.send("{} Kisses {} https://i.imgur.com/qqq9tA6.jpeg".format(ctx.message.author.mention, member.mention))


@client.command(pass_context = True)
async def punch(ctx,member:discord.Member):
	await ctx.message.delete(delay = 0.6)
	await ctx.send("{} punched {} https://i.imgur.com/IXh5nFf.mp4".format(ctx.message.author.mention, member.mention))












#spotify
@client.command()
async def spotify(ctx, user: discord.Member=None):
    user = user or ctx.author
    for activity in user.activities:
        if isinstance(activity, Spotify):
            await ctx.send(f"{user} is listening to {activity.title} by {activity.artist}")
            await ctx.message.delete(delay = 0.6)
    else:
    	await ctx.send('Нихуя он не слушает')
    	await ctx.message.delete(delay = 0.6)


#avatar
@client.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)
    await ctx.message.delete(delay = 0.6)























































#join voice
@client.command()
async def join(ctx):
	global voice
	channel= ctx.message.author.voice.channel

	voice=get(client.voice_clients, guild=ctx.guild)
	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()
		await ctx.send(f'Бот подключен к {channel}')










#disconnect
@client.command()
async def dis(ctx):
	channel= ctx.message.author.voice.channel

	voice=get(client.voice_clients, guild=ctx.guild)
	if voice and voice.is_connected():
		await voice.disconnect()
	else:
		voice = await connect.channel()
		await ctx.send(f'Бот отключен от {channel}')




	



token = open('token.txt', 'r').readline()

client.run( token )