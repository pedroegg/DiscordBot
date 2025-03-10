import discord
from discord import app_commands
from discord.ext.commands import Cog, Bot, Context, command

class Help(Cog):
	def __init__(self, bot: Bot):
		self.bot = bot

	@command(name='help')
	async def help(self, ctx: Context):
		await ctx.send('Help list')
		
	@app_commands.command(name='help', description='Lista de comandos')
	async def slash_help(self, interaction: discord.Interaction):
		await interaction.response.send_message(f'Help list')

async def setup(bot: Bot):
	await bot.add_cog(Help(bot))
