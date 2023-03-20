# ControlCV_TelegramBot
This is a Telegram bot that copies the text of the last received message to the clipboard. The bot runs on Python and utilizes the telegram, asyncio, and pyperclip libraries.

Dependencies:

    'telegram'
    'asyncio'
    'pyperclip'

To use the bot:

    1. Replace "your token HERE" with your bot token in the code.
    2. Run the code.
    3. Send a message to the bot on Telegram.
    4. The text of the message will be copied to the clipboard.

Note: The bot will only copy the text of a message once, when it is first received. If the same message is received again, it will not be copied to the clipboard again.
