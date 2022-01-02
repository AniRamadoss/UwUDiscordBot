import discord
import asyncio
from config import token

level2_owo = False
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
        msg_copy = msg.copy()
        uwufiable = False
        print(message.content)
        j = 0
        for i in range(0, len(msg_copy)):
            if ((msg_copy[i] == "r" or msg_copy[i] == "R") and i != 0 and msg_copy[i - 1] != "f") or (msg_copy[i] == "l" or msg_copy[i] == "L") or (msg_copy[i] == "r" and i == 0):
                msg[j] = "w"
                uwufiable = True
            # elif msg[i] == 'n' and ((msg[i + 1]).isalpha() and msg[i + 1] != "y"):
            #     if not (msg == "ong" or (1 < i < len(msg) - 2 and msg[i - 2] == " " and msg[i + 2] == " " and msg[i - 1] == "o" and msg[i + 1] == "g") or (i == 1 and msg[i - 1] == "o" and i < len(msg) - 3 and not(msg[i + 2]).isalpha()) or (i == len(msg) - 2 and i >= 1 and msg[i - 1] == "o" and msg[i + 1] == "g")):
            #         msg.insert(i + 1, "y")
            #         uwufiable = True
            if level2_owo and ((msg_copy[i] == "o" and i < len(msg_copy) - 2 and msg_copy[i + 1] != "n" and msg_copy[i + 2] != "g") or (msg_copy[i] == "o" and i >= len(msg_copy) - 2) or msg_copy[i] == "u" or msg_copy[i] == "O" or msg_copy[i] == "U"):
                msg.insert(j + 1, "w")
                msg.insert(j + 2, msg[j])
                j += 2
                uwufiable = True
            j += 1
        msg = "".join(msg)
        return uwufiable, msg


client = uwu_bot()
client.run(token, bot=False)
