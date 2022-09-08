import os
import discord

custom_intents = discord.Intents.default()
custom_intents.message_content = True

client = discord.Client(intents = custom_intents)

@client.event
async def on_ready():
    print("We have logged in as " + str(client.user))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith("-python"):
        new_message = "```python\n"
        d = 0
        for line in message.content.splitlines():
            if d == 0:
                d += 1
                continue

            line = line.replace("    ", "-    ")
            line = line.replace("\n", "")
            new_message += str(d) + ".  " + line + "\n"
            d += 1

        #new_message = new_message.replace("for", "**for**")




        """#  now detect syntax errors and correct them. Rember to insert them at the end of the code so people can fix it  #"""




        new_message += "\n\nBy " + str(message.author)
        new_message += "\n```"
        print(new_message)

        await message.channel.send(new_message)
        await message.delete()

client.run('')
