import logging
logger = logging.getLogger('Discord Bot')

import os
from typing import Optional
import discord
from discord.ext.commands import Bot as DiscordBot

class Bot(DiscordBot):
	prefix: Optional[str] = os.getenv('BOT_PREFIX')
	token: Optional[str] = os.getenv('DISCORD_TOKEN')

	def __init__(self) -> None:
		if not self.prefix:
			logger.error('bot prefix env var not defined')
			raise ValueError('missing prefix env var')
		
		if not self.token:
			logger.error('discord token env var not defined')
			raise ValueError('missing discord token env var')
		
		intents = discord.Intents.default()
		intents.message_content = True # privileged gateway intent
		intents.guild_reactions = True
		intents.expressions = True
		intents.guild_messages = True
		intents.guild_typing = True

		super().__init__(
			command_prefix=self.prefix, intents=intents, help_command=None)

	def run(self) -> None:
		"""
		overwrites the original 'run' Bot method
		"""

		super().run(token=self.token, reconnect=True, log_handler=None, log_level=None)

	async def setup_hook(self):
		"""
		Method automatically called by Bot before connecting to Discord.
		Ideal place to load cogs or something else.
		"""

		current_dir = os.path.dirname(os.path.abspath(__file__))
		cogs_dir = os.path.join(current_dir, 'cogs')

		for filename in os.listdir(cogs_dir):
			if not filename.startswith('_') and filename.endswith('.py'):
				#keep the 'cogs' folder in the same path as this file (e.g., bot.py)
				extension = f'{__package__}.cogs.{filename[:-3]}'

				#TODO: handle errors
				try:
					await self.load_extension(extension)
					logger.info(f'loaded extension: {extension}')
				
				except Exception as e:
					logger.error(f'failed to load extension {extension}: {repr(e)}')
					raise
		
		#TODO: handle errors
		try:
			await self.tree.sync()
		except Exception as e:
			logger.error(f'failed to sync slash commands: {repr(e)}')
			raise
