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
logging.basicConfig(level=int(os.getenv('LOG_LEVEL')), force=True)
logger = logging.getLogger("Main")

# omitting libs DEBUG logs when in dev
logging.getLogger("urllib3").setLevel(logging.INFO)

logger.info('intializing...')

import threading
import signal

#from library.demucs import HTdemucs, HTdemucs6s, _DemucsProcessor, ProcessPayload

stop_event = threading.Event()

def signal_handler(sig, frame):
	logger.info('signal received, finishing application gracefully...')
	stop_event.set()

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

logger.info('init completed!')
# --------------------------

# ------ running project -------
def run():
	#while not stop_event.is_set():
	a = 1

if __name__ == "__main__":
	run()

	print("bye!")
	sys.exit(0)
# ------------------------------