from crontab import CronTab

cron = CronTab(user=True)
job = cron.new('python3 main/Telegram-Bot/temp/test.py')
job.setall('50-59 * * * *')
cron.write()
