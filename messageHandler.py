from handlers import crontabHandler
from temp import test, temp

def main(msg):
    response = ''

    if msg[0:6] == '/cron ':
        return crontabHandler.main(msg)
    elif msg == '/hi':
        return test.main()
    elif msg == 'test':
        return temp.crondel(msg)
