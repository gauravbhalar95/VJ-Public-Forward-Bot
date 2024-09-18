from forwardbot import Config
from telethon.tl.functions.users import GetFullUserRequest
from forwardbot.utils import forwardbot_cmd, is_sudo
from forwardbot import bot
from ethon.mystarts import start_srb

# Configuration and status settings
MessageCount = 0
BOT_STATUS = "0"
status = set(int(x) for x in (BOT_STATUS).split())
help_msg = Config.HELP_MSG
sudo_users = Config.SUDO_USERS

# Start command - Welcomes the user and provides information about the bot
@forwardbot_cmd("start", is_args=False)
async def start(event):
    text = (
        "**Hi, I am a public forwarder bot.**\n"
        "**Using me, you can forward all files from one channel to another easily.**\n"
        "**However, I might get banned anytime, so please join our [Update Channel](https://t.me/vj_botz) "
        "to get new bot updates.**\n"
        "**Type /help to know more about the bot.**"
    )
    await start_srb(event, text)

# Help command - Provides help message from config
@forwardbot_cmd("help", is_args=False)
async def handler(event):
    await event.respond(help_msg)

# Test command - Provides information about the bot owner
@forwardbot_cmd("test", is_args=False)
async def handler(event):
    await event.respond(f"The bot owner is: {bot.owner}")

# Admin command - Checks if the user is an admin (sudo user)
@forwardbot_cmd("admin", is_args=False)
async def handler(event):
    if str(event.sender_id) in sudo_users:
        await event.respond("You are an admin.")
    else:
        await event.respond("You are not an admin.")
