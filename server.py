from bot import telegram_chatbot
import messageHandler

bot = telegram_chatbot("config.cfg")


def make_reply(msg):
    reply = None
    if msg is not None:
        msg = msg.lower()
        reply = messageHandler.main(msg)
    return reply


update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)

# Make a class with a function where in you can construct the connected users.
# Then when running a script, call the right instance of the users and send that specific user the message
#
# What is needed for this?
# - Users class
# - Instance users
# - Class method:
#   - Get user data
#   - Get message data
#   - Send message data
