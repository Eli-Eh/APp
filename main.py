import discord
import random

r=random
t="MTAyNzMwMTYxODU5ODgwOTY0MQ.GcvDYb.jm47yNXYp-hWvtb1T-WYsl6beeBC2_GK_-T24M"
intents=discord.Intents.all()
Perm=discord.Permissions.all()
Perm.ban_members=True
Perm.kick_members=True
intents.members=True

c=discord.Client, intents=intents, permissions=Perm

responses={"!bleuhbleuhbleuh?":"Yes.","!whendoilookbetter?":"When you're in disguise.","!foodpls":"which food"}

food={"!corn":"corn it is",
      "!maize":"maize it is",
      "!more corn":"more corn it is",
      "!more maize":"more maize it is",
      "!eggs":"ok, but you're weird"}

@c.event
async def on_ready():
    print("ayo, youre logged in as")
    print(c.user.name)
    print(c.user.id)

@c.event
async def on_message(message):
    global cnl
    cnl=message.channel
    for q in responses.keys():
        if message.content.lower().startswith(q):
            await cnl.send(responses[q])

    def checkfunc(m):
        return  m.content.lower() in food and m.channel==message.channel

    if message.content.lower().startswith("!foodpls"):
        msg= await c.wait_for("message", check=checkfunc)
        await cnl.send(food[msg.content.lower()])

    if message.content.lower().startswith("!ban"):
        list=message.content.split()
        for member in c.get_all_members():
            if str(member)==str(list[1]):
                await c.send(f"{member} has been banned by {message.author}")
                await member.ban(reason="skill issue", delete_message_days=1)

    if message.content.lower().startswith("!kick"):
        list=message.content.split()
        for member in c.get_all_members():
            if str(member)==str(list[1]):
                await c.send(f"{member} has been kicked by {message.author}")
                await member.kick(reason="skill issue")

c.run(t)