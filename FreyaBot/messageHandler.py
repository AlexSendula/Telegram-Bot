from webscraper import makro


def main(msg):
    response = ''

    if msg.lower() == 'makro':
        return makro.main()
