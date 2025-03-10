import discord
from discord import app_commands
from discord.ext.commands import Cog, Bot, Context, command

class Ping(Cog):
	def __init__(self, bot: Bot):
		self.bot = bot

	@command(name='ping')
	async def ping(self, ctx: Context):
		await ctx.send('Pong!')

	@app_commands.command(name='ping', description='Ping test')
	async def slash_ping(self, interaction: discord.Interaction):
		await interaction.response.send_message(f'Pong!')

async def setup(bot: Bot):
	await bot.add_cog(Ping(bot))
