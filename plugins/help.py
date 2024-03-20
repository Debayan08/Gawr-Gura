from pyrogram import Client,filters


@Client.on_message(filters.command(["help", "h","list"]))
async def help(client, message):
    await message.reply_text("`――――――――――――[HELP]――――――――――――\n\n• Prefix [ '/ ' ] \n\n[Comments] \n\n• anime [anime name]\nDes- This will give brief description about the anime with the official poster.\n\n• qr [Link/Text]\nDes- Give text or link it will convert them into QR code.\n\n• bored\nDes- It will give you a certain task to do.\n\n• fact\nDes- It will give you fun fact.\n\n• jokes\nDes- It will give you a funny joke.\n\n• waifu \nDes- It will give waifus.\n\n• whatanime [Replied anime clip or Gif]\nDes- It will give the anime name of the clip or Gif.\n\n• voice [Text]\nDes- Text -> Audio\n\n• Translate or t [Text/Replied message]\nDes- It will translate the message into any languages \n\n•yt_dl [Link]\nDes- Download YouTube videos and audios.\n\n•ig_dl [Link]\nDes- Download Instagram videos and audios.\n\n• profile\nDes- Give user's profile Picture and usename and use id \n\n• event\nDes- Welcome message and Good Bye message \n\n• pin [Text]\nDes- Pin the message.\n\n• chat_info\nDes- Chat profile picture,id and title \n\n• link\nDes- provide the chat invite Link \n\n• id\nDes- Give your id and username\n\n• rps \nDes- Rock Paper Scissor Game\n\n• tic_tac_toe\nDes- Tic Tac Toe Game \n――――――――――――――――――――――――――――――`") 
