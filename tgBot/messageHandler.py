from tgBot.handlers import crontabHandler
from tgBot.temp import test

def main(msg):
    response = ''

    if msg[0:5].lower() == 'cron ':
        return crontabHandler.main(msg)
    elif msg.lower() == 'hi':
        return test.main()