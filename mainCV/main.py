import telegram
import asyncio
import pyperclip
from mainbot import TOKEN

bot = telegram.Bot(token=TOKEN)
last_copied_message = ""

async def main():
    last_copied_message = ""
    while True:
        chat_id, message = await get_last_message()
        if message and message != last_copied_message:
            # Copy the text of the message to the clipboard if it's different from the last copied message
            pyperclip.copy(message)
            last_copied_message = message
        await asyncio.sleep(1) # Add a small delay before the next check


async def get_last_message():
    async with bot:
        updates = await bot.get_updates()
        if not updates:
            return None, None
        message = updates[-1].message.text
        chat_id = updates[-1].message.chat_id
        return chat_id, message

asyncio.run(main())

def happyfunktion():
    print('wwww')

happyfunktion()
