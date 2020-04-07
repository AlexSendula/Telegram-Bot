from crontab import CronTab

cronjobs = []
f = open('cronjobs.txt', 'r')
x = f.readlines()
for i in x:
    i = i[:-1]
    x = i.split(', ')
    cronjobs.append(x)


def main(msg):
    msg = msg.split()
    cron = CronTab(user=True)
    # Check if job is active => disable
    for z in cron:
        if z == msg[1]:
            cmd = cron.find_command(msg[1])
            cron.remove(cmd)
            cron.write()
            result = 'Cron {} disabled'.format(msg[0])
            return result
    # Check if job exists in job list => enable
    for y in cronjobs:
        if y[0] == msg[1]:
            cmd = y[1]
            job = cron.new(command=cmd)
            job.setall(str(y[2]))
            cron.write()
            result = 'succes'
            return result

    result = 'Try again...'
    return result

# CODE: TO ADD TIME IN MESSAGE FOR CRONJOB TIMING

# * * * * * python3 main/Telegram-Bot/temp/test.py
# */30 8-22 * * * python3 main/Telegram-Bot/webscraper/makro.py # makro
