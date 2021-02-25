import logging
from pyrogram import Client
from vars import var

logging.basicConfig(level=logging.INFO)

AnoMeSeBot = Client('Anonymous_Messages_Sender',
                  api_id=var.API_ID,
                  api_hash=var.API_HASH,
                  bot_token=var.BOT_TOKEN,
                  plugins=dict(root="plugins"))

AnoMeSeBot.run()
