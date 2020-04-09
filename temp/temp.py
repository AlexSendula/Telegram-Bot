from crontab import CronTab


def cronadd():
    cron = CronTab(user=True)
    job = cron.new('python3 main/Telegram-Bot/temp/test.py')
    job.setall('50-59 * * * *')
    cron.write()

def crondel(msg):
    cron = CronTab(user=True)
    cmd = cron.find_command(command=msg)
    cron.remove(cmd)
    cron.write()
    reply = 'Deleted: {}'.format(cmd)
    return reply
