test = __import__('temp.test')
crontabHandler = __import__('handlers.crontabHandler')


def main(msg):
    response = ''

    if msg[0:5].lower() == 'cron ':
        return crontabHandler.main(msg)
    elif msg.lower() == 'hi':
        return test.main()
