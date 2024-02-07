# Import API keys
import creds

# Import Discord API
import discord
from discord.ext import commands

# Import OpenAI API and set API key
from openai import OpenAI
client = OpenAI(api_key = creds.openai_api_key)

# Define the intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Initialize bot with the defined intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Bot event set so that when bot launches successfully it can be seen in the terminal
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Set the kind of message required for the bot to reply and the role that it will be playing
@bot.command()
async def chat(ctx, *, message: str):

    gpt_message=[{"role": "system", "content": "You are The Doctor, the witty main character from the popular British TV show Doctor Who."}, {"role": "user", "content": message}]
    temperature=0.2
    max_tokens=256
    frequency_penalty=0.0

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = gpt_message,
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penalty
    )

    await ctx.send(response.choices[0].message.content)

# Run the bot with its token
bot.run(creds.discord_api_key)
