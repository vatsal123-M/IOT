import telepot
token = '1252452949:AAF_TVShjOExikj3m30k1FUSx1Y7kMrStqI'
TelegramBot = telepot.Bot(token)
print(TelegramBot.getMe())

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id.format(msg["text"]))

TelegramBot.message_loop(handle)
