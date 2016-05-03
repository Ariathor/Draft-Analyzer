__author__ = 'Ioannis'

import fileinput
import csv
import json
import datetime
import statistics
import os.path
import _csv                 # To catch the NULL type error
from ast import literal_eval

import config_handler
import download_data
from formatted_date_generator import date_generator

# Reads the AH-Data posted by Cryptozoic stored in file_name and merges them in the dictionary cards
# Deletes data
def update_day(file_name, cards):
    attempts = 0
    while attempts < 2:                     # Try to re-download corrupted data twice before giving up

        # Strip the file of tabs
        try:
            for line in fileinput.input('AH-Data/' + file_name, inplace=True):
                print(line.replace('\t', ''), end='')
        except FileExistsError:
            if config_handler.getter('verboseFlag'):
                print("File exists error: " + file_name + ". Most likely pops up because the file is bugged/empty.")
                attempts = 3

        with open("AH-Data/" + file_name) as f:

            csv_f = csv.reader(f)
            # row[0]=card name, row[1]=rarity, row[2]=currency, row[3]=price, row[4]=date
            # Rarity values: 0-->Equipment, 2-->Common, 3-->Uncommon, 4-->Rare, 5-->AA, 6-->Legendary
            try:
                for row in csv_f:
                    key = (row[0], row[1], row[2])
                    if key in cards:
                        cards[key].append((row[3], row[4]))
                    else:
                        cards[key] = [(row[3], row[4])]
                    attempts = 3                        # No errors - we can go out of the loop
            except (IndexError, _csv.Error):
                    # Erases and re-downloads corrupted files
                    if config_handler.getter('verboseFlag'):
                        print('Re-downloaded', file_name, 'due to an error')
                    download_data.replace_day(file_name)
                    attempts += 1
    # Doesn't need a return value because it just modifies the given card dictionary

def update():
    download_data.main()   # Downloads the latest AH-Data

    days = date_generator()
    cards = {}

    for formatted_date in days:
        try:
            update_day(formatted_date, cards)  # Only works because all instances modify the same card dictionary
        except FileNotFoundError:
            if config_handler.getter('verboseFlag'):
                print('Could not find ' + formatted_date)

    # Convert keys to strings, so that json can recognize them
    # Could also use 'w' instead of 'wt' since opening in text mode is the default
    os.makedirs('Card Info', exist_ok=True)
    with open('Card Info/database.json', 'wt') as fp:
        json.dump({str(key): value for key, value in cards.items()}, fp, indent=4, sort_keys=True)


# Opens the AH-Data database created by update()
# Return a dictionary of lists in this format: {(cardName, RarityNumber, Currency):[(price, date), (price2, date2) etc.]}
def open_ah_data():
    if not os.path.isfile('Card Info/database.json'):
        update()
    try:
        with open('Card Info/database.json', 'rt') as fp:
            cards = json.load(fp)
    except:
        if config_handler.getter('verboseFlag'):
            print('Problem while loading database.json')

    # Converting keys to tuples
    # Without creating a temporary dict, "for key in cards" would run for the new keys too
    newCards = {}
    for key in cards:
        newCards[literal_eval(key)] = cards[key]
    cards = newCards

    return cards


# Returns a dictionary with (card, rarity, currency) as keys and (median, numOfSales) as values
# If there are less than 5 sales in the last 14-days returns long_term_median for that card instead
def short_term_median():
    longTermMedians = long_term_median()        # In case we don't have enough short term sales
    cards = open_ah_data()                      # dict with (card, rarity, currency) tuples as keys and a list of (sale, date) as value
    cardValues = {}
    for key in cards:
        listOfSales = cards[key]                # It's still a pointer to the same list
        recentSales = []
        for i in range(1, len(listOfSales)):    # Start at 1, because list[-0] gives the first element and we want the last
            # if sale of the date is in the last 2 weeks
            if datetime.datetime.strptime(listOfSales[-i][1], '%Y-%m-%d') < datetime.datetime.today() - datetime.timedelta(days=15):
                break                           # Moves on to the next key
            else:
                try:
                    recentSales.append(literal_eval(listOfSales[-i][0]))
                except IndentationError:
                    if config_handler.getter('verboseFlag'):
                        print('Problem with short term median literal_eval of', listOfSales[i][0])
        numberOfSales = len(recentSales)
        if numberOfSales >= 5:
            median = statistics.median(recentSales)
        else:
            median = longTermMedians[key][0]
        cardValues[key] = (median, numberOfSales)

    return cardValues


# Three month-median (database only keeps data up to three months)
def long_term_median():
    cards = open_ah_data()                      # dict with (card, rarity, currency) tuples as keys and a list of (price, date) as value
    cardValues = {}
    for key in cards:
        try:
            listOfSales = cards[key]                # It's still a pointer to the same list
            sales = []
            for sale in listOfSales:
                sales.append(literal_eval(sale[0]))
            numberOfSales = len(sales)
        except IndentationError:
            if config_handler.getter('verboseFlag'):
                print('Problem with long term median of', key)
        try:
            median = statistics.median(sales)
        except statistics.StatisticsError:
            median = 0
        cardValues[key] = (median, numberOfSales)

    return cardValues

# Returns a dictionary of cards paired with their rounded average plat value. Doesn't take AAs into account
# Uses short-term median (reminder: long-term median is used in case there are less than 14 short-term sales)
def simple_median_values():
    cardValues = short_term_median()
    simpleCardMedians = {}
    for key in cardValues:
        if key[2] == 'PLATINUM' and key[1] != '5' and key[1] != '0':    # Ignoring equipment because of some cards being bugged and having entries as equipment
            simpleCardMedians[key[0]] = round(cardValues[key][0])
    return simpleCardMedians

def store_simple_median():
    cardValues = simple_median_values()
    with open('Card Info/simple_medians.json', 'wt') as fp:
        json.dump(cardValues, fp, indent=4, sort_keys=True)

def open_simple_median():
    if not os.path.isfile('Card Info/simple_medians.json'):
        store_simple_median()

    with open('Card Info/simple_medians.json', 'rt') as fp:
        cardValues = json.load(fp)
    return cardValues

# Ignores the price of non-legendary cards that sell at their respective price floor (3-4 plat, 10-11 plat, 30-31plat)
def store_trimmed_values():
    cardValues = short_term_median()
    trimValues = {}
    for key in cardValues:
        if key[2] == 'PLATINUM' and key[1] != '5' and key[1] != '0':    # Ignoring equipment because of some cards being bugged and having entries as equipment
            cardName = key[0]
            cardPrice = cardValues[key][0]
            cardRarity = key[1]
            if cardRarity == '2' and cardPrice <= 5 or cardRarity == '3' and cardPrice <=12 or cardRarity == '4' and cardPrice <= 32:
                cardPrice = 0
            trimValues[cardName] = round(cardPrice)
    with open('Card Info/trimmed_values.json', 'wt') as fp:
        json.dump(trimValues, fp, indent=4, sort_keys=True)

def open_trimmed_values():
    if not os.path.isfile('Card Info/trimmed_values.json'):
        store_trimmed_values()
    with open('Card Info/trimmed_values.json', 'rt') as fp:
        trimValues = json.load(fp)
    return trimValues


def main():
    update()
    store_simple_median()
    store_trimmed_values()



if __name__ == '__main__':
    main()
    print(open_simple_median())






