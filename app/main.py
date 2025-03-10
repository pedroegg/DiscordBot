# ------ loading environment ------
from dotenv import load_dotenv
import sys
import os

load_dotenv('prod.env')
if os.getenv("ENV") != "production":
	load_dotenv('.env', override=True)
# ------------------------------

# ------ init project ------
import logging
logging.basicConfig(
	level=int(os.getenv('LOG_LEVEL', '20')),
	stream=sys.stdout,
	format='%(asctime)s %(levelname)s %(name)s: %(message)s',
	datefmt='%Y/%m/%d %H:%M:%S',
	force=True,
)

logger = logging.getLogger("Main")
logger.info('intializing...')

# omitting libs DEBUG logs when in dev
logging.getLogger('urllib3').setLevel(logging.INFO)
logging.getLogger('asyncio').setLevel(logging.INFO)
logging.getLogger('discord').setLevel(logging.INFO)

from library.discord.bot import Bot
bot = Bot()

import signal
import asyncio

def signal_handler(sig, frame):
	logger.info('signal received, finishing application gracefully...')

	if not bot.is_closed():
		bot.loop.call_soon_threadsafe(lambda: asyncio.create_task(bot.close()))

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

logger.info('init completed!')
# --------------------------

# ------ running project -------
def run():
	try:
		bot.run()
	
	except Exception as e:
		logger.error(f'unexpected error: {repr(e)}')

if __name__ == "__main__":
	run()

	print("bye!")
	sys.exit(0)
# ------------------------------