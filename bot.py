import pyrogram
import logging
import os
from config import Config

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

class channelforward(pyrogram.Client):
    
    def __init__(self):
        try:
            super().__init__(
                name="CHANNELFORWARD",
                bot_token=Config.BOT_TOKEN,
                api_id=Config.API_ID,
                api_hash=Config.API_HASH,
                workers=20,
                plugins=dict(
                    root="Plugins"
                )
            )
        except Exception as e:
            logger.error(f"Error initializing client: {e}")
            raise

if __name__ == "__main__":
    try:
        channelforward().run()
    except Exception as e:
        logger.error(f"Error running bot: {e}")

# import pyrogram

# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# import os

# from config import Config
# from pyrogram import Client 
# logging.getLogger("pyrogram").setLevel(logging.WARNING)

# class channelforward(Client):
    
#     def __init__(self):
#         super().__init__(
#             name="CHANNELFORWARD",
#             bot_token = Config.BOT_TOKEN,
#             api_id = Config.API_ID,
#             api_hash = Config.API_HASH,
#             workers = 20,
#             plugins = dict(
#                 root="Plugins"
#             )
#         )

# if __name__ == "__main__" :
#     channelforward().run()

