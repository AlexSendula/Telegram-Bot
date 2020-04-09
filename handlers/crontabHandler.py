from crontab import CronTab

cronjobs = []
f = open('handlers/cronjobs.txt', 'r')
x = f.readlines()
for i in x:
    i = i[:-1]
    x = i.split(', ')
    cronjobs.append(x)


def main(msg):
    msg = msg.split()
    cron = CronTab(user=True)
    # Check if job is active => disable
    cmd = cron.find_command(command=msg[1])
    for z in cron:
        z = str(z)
        if z.find(msg[1]) > -1:
            cron.remove(cmd)
            cron.write()
            result = "Cronjob is '{}' disabled.".format(msg[1])
            return result
    # Check if job exists in job list => enable
    for y in cronjobs:
        if y[0] == msg[1]:
            cmd = y[1]
            job = cron.new(command=cmd)
            job.setall(str(y[2]))
            cron.write()
            result = 'Cronjob {} enabled.'.format(msg[1])
            return result

    result = 'Try again...'
    return result

# CODE: TO ADD TIME IN MESSAGE FOR CRONJOB TIMING

# * * * * * python3 main/Telegram-Bot/temp/test.py
# */30 8-22 * * * python3 main/Telegram-Bot/webscraper/makro.py # makro
