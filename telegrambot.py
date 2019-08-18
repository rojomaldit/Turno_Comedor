import telegram
bot = telegram.Bot(token='830421539:AAFBIzACZglNI5Z8m8htuLkJB4NTnzuBlkY')

updates = bot.get_updates()

print([u.message.text for u in updates])

chat_id = bot.get_updates()[-1].message.chat_id

bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
