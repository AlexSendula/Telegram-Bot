import bs4 as bs
import urllib.request
import requests

msg =''
bot = 'https://api.telegram.org/bot1160110586:AAGq6npXmn839dWitkAvA-KSZYvisgdvFLc/sendMessage?text={}&chat_id=680658091'

# Web-scraper
def main():
    source = urllib.request.urlopen('https://voorraad.makro.nl/voorraad/?artno=626548&variant=1&bundle=1').read()
    soup = bs.BeautifulSoup(source, 'lxml')

    table = soup.table
    table_rows = table.find_all('tr')

    brow = []
    for tr in table_rows:
        td = tr.find_all('td')
        x = 0
        for i in td:
            if td.index(i) % 2 != 0:
                continue
            if x:
                brow.append(i.text)
                break
            if i.text == 'Barendrecht':
                brow.append(i.text)
                x += 1

    # On condition publish
    if brow[1] != 'niet op voorraad':
        msg = 'Toilet papier op voorraad'
        requests.get(bot.format(msg))
    else:
        msg1 = 'Niet op voorraad'
        requests.get(bot.format(msg1))

main()
