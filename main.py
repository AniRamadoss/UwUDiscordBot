import discord
import asyncio
from config import token


class uwu_bot(discord.Client):
    async def on_ready(self):
        print("uwu time")

    async def on_message(self, message: discord.Message):
        if message.author.id == 235058650513670145:
            result = self.uwufiable(message)
            if result[0]:
                await asyncio.sleep(0.250)
                await message.edit(content=result[1])

    def uwufiable(self, message: discord.Message) -> tuple:
        msg = message.content
        if "`" in msg or "*" in msg or "|" in msg:
            return False, ""
        msg = list(msg)
        uwufiable = False
        print(message.content)
        for i in range(0, len(msg)):
            if (msg[i] == "r" and i != 0 and msg[i - 1] != "f") or msg[i] == "l" or (msg[i] == "r" and i == 0):
                msg[i] = "w"
                uwufiable = True
            elif msg[i] == 'n' and ((msg[i + 1]).isalpha() and msg[i + 1] != "y"):
                if not (msg == "ong" or (1 < i < len(msg) - 2 and msg[i - 2] == " " and msg[i + 2] == " " and msg[i - 1] == "o" and msg[i + 1] == "g") or (i == 1 and msg[i - 1] == "o" and i < len(msg) - 3 and not(msg[i + 2]).isalpha()) or (i == len(msg) - 2 and i >= 1 and msg[i - 1] == "o" and msg[i + 1] == "g")):
                    msg.insert(i + 1, "y")
                    uwufiable = True
        msg = "".join(msg)
        return uwufiable, msg


client = uwu_bot()
client.run(token, bot=False)
