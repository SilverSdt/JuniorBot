import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user: return

    if message.content.startswith('$hello'): await message.channel.send('Hello!')
    
    if message.content.startswith('$Shifumi'): await message.channel.send(f'Implementation for {str(message.author).split("#")[1]}')

client.run('MTAzNDA4NjY5ODA3NTgxNTk1Ng.GSSRLK.Ainw04FbAxv5LbIvbmj3VQEcmgXfB6zQnlkoEg')
