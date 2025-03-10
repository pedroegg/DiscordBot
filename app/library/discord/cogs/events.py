import logging
logger = logging.getLogger('Discord Bot - Events Extension')

from discord.ext.commands import Cog, Bot, Context, CommandError, CommandNotFound, MissingRequiredArgument

class Events(Cog):
	def __init__(self, bot: Bot):
		self.bot = bot
	
	@Cog.listener()
	async def on_ready(self):
		logger.info(f'logged in as {self.bot.user.name} ({self.bot.user.id})')

	@Cog.listener()
	async def on_command_error(self, ctx: Context, error: CommandError):
		if isinstance(error, CommandNotFound):
			await ctx.send('Invalid command. Type ?help for a list of commands.')

		elif isinstance(error, MissingRequiredArgument):
			await ctx.send('Missing required arguments. Check the command usage with ?help <command>.')
		
		else:
			logger.error(f'command error: {error}')

async def setup(bot: Bot):
	await bot.add_cog(Events(bot))
