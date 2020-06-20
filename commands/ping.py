import datetime
from time import time
import discord
from discord.ext import commands
from discord.utils import snowflake_time

class Ping(commands.Cog, name='Ping'):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(description="Displays connection speed info",
		help='Calculates the latency of the client to the endpoint based on the time it takes for a response message to be sent to the command message. API latency information is provided by the websocket')
	async def ping(self,ctx):
		try:
			m = await ctx.send('Ping?')
			await m.edit(content=f'🏓 Pong! Latency is {int((snowflake_time(m.id) - snowflake_time(ctx.message.id)).microseconds/1000)}ms. API Latency is {round(self.bot.latency*1000)}ms')
		except Exception as e:
			await ctx.send(repr(e))

def setup(bot):
	bot.add_cog(Ping(bot))
