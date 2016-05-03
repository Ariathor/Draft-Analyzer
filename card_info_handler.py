# Copyright 2015, Ioannis Mouratidis, All rights reserved.
__author__ = 'Ioannis'

import json
import requests
import datetime
import os.path
import threading

import config_handler

#Possible Improvement: Download data from cwik's API automatically

non_cards = ("BoosterPack","CLASS","CompTicket","DeckSleeve","Gem","Mercenary","PVE001AI","PVE_AI_Card","PVE_Campaign_Card","Stardust","TreasureChest", "Unspecified","VIPProduct")
card_info_lock = threading.Lock()

def store_colors():
    os.makedirs('Card Info', exist_ok=True)
    if not os.path.isfile('Card Info/card_info.json'):
        update(force=True)
    try:
        with card_info_lock:
            with open('Card Info/card_info.json', 'rt') as fp:
                cardInfo = json.load(fp)
    except:
        if config_handler.getter('verboseFlag'):
            print('Card_info.json error')

    # if not response["error"] and response["status"] == 200:
    #     cardInfo = response["data"]
    # else:
    #     if config_handler.getter('verboseFlag'):
    #         print("Data not downloaded correctly")

    cardColors = {}                    #Dictionary that relates cards to their threshold requirements
    for cardDict in cardInfo:
        if cardDict['set_number'] not in non_cards:           #Ignoring non-cards
            if cardDict['rarity'] not in ('Non-Collectible', ''):       #Ignoring AAs, champions and non-collectible cards
                cardColors[cardDict['name']] = cardDict['color']
    with open('Card Info/simple_colors.json', 'wt') as fp:
        json.dump(cardColors, fp, indent=4, sort_keys=True)


def store_rarity():
    os.makedirs('Card Info', exist_ok=True)
    if not os.path.isfile('Card Info/card_info.json'):
        update(force=True)
    try:
        with card_info_lock:
            with open('Card Info/card_info.json', 'rt') as fp:
                cardInfo = json.load(fp)
    except:
        if config_handler.getter('verboseFlag'):
            print('Card_info.json error')

    # if not response["error"] and response["status"] == 200:
    #     cardInfo = response["data"]
    # else:
    #     if config_handler.getter('verboseFlag'):
    #         print("Data not downloaded correctly")


    cardRarity = {}
    for cardDict in cardInfo:
        if cardDict['set_number'] not in non_cards:                             #Ignoring non-cards
            if cardDict['rarity'] not in ('Non-Collectible', ''):       #Ignoring AAs, champions and non-collectible cards
                cardRarity[cardDict['name']] = cardDict['rarity']

    with open('Card Info/simple_rarity.json', 'wt') as fp:
        json.dump(cardRarity, fp, indent=4, sort_keys=True)


def store_set():
    os.makedirs('Card Info', exist_ok=True)
    if not os.path.isfile('Card Info/card_info.json'):
        update(force=True)
    try:
        with card_info_lock:
            with open('Card Info/card_info.json', 'rt') as fp:
                cardInfo = json.load(fp)
    except:
        if config_handler.getter('verboseFlag'):
            print('Card_info.json error')

    cardSet = {}
    translation = {'001': 'Shards of Fate',
                   '002': 'Shattered Destiny',
                   '003': 'Armies of Myth',
                   '004': 'Primal Dawn',
                   'PVE001': 'Frost Ring Arena',
                   'PVE002': 'Chest Loot'
                   }

    for cardDict in cardInfo:
        if cardDict['set_number'] not in non_cards:                             #Ignoring non-cards
            if cardDict['rarity'] not in ('Non-Collectible', ''):       #Ignoring AAs, champions and non-collectible cards
                try:
                    traslatedSet = translation[cardDict['set_number']]
                except KeyError:
                    traslatedSet = cardDict['set_number']
                cardSet[cardDict['name']] = traslatedSet

    with open('Card Info/simple_set.json', 'wt') as fp:
        json.dump(cardSet, fp, indent=4, sort_keys=True)


# Translate m-guid/uuid to card names
def store_guid_to_names():
    os.makedirs('Card Info', exist_ok=True)
    if not os.path.isfile('Card Info/card_info.json'):
        update(force=True)
    try:
        with card_info_lock:
            with open('Card Info/card_info.json', 'rt') as fp:
                cardInfo = json.load(fp)
        card_names = {}

        for cardDict in cardInfo:
            if cardDict['set_number'] not in non_cards:  # Ignoring non-cards
                if cardDict['rarity'] not in ('Non-Collectible', '') or cardDict['name'] in (
                'Ruby Shard', 'Diamond Shard', 'Sapphire Shard', 'Wild Shard',
                'Blood Shard'):  # Ignoring champions and non-collectible cards
                    card_names[cardDict['uuid']] = cardDict['name']

    except Exception:
        if config_handler.getter('verboseFlag'):
            print('Card_info.json error')



    with open('Card Info/guid_to_names.json', 'wt') as fp:
        json.dump(card_names, fp, indent=4, sort_keys=True)

def simple_colors():
    if not os.path.isfile('Card Info/simple_colors.json'):
        store_colors()
    with open('Card Info/simple_colors.json', 'rt') as fp:
        cardColors = json.load(fp)
    return cardColors


def simple_rarity():
    if not os.path.isfile('Card Info/simple_rarity.json'):
        store_rarity()
    with open('Card Info/simple_rarity.json', 'rt') as fp:
        cardRarity = json.load(fp)
    return cardRarity


def simple_set():
    if not os.path.isfile('Card Info/simple_set.json'):
        store_set()
    with open('Card Info/simple_set.json', 'rt') as fp:
        cardSet = json.load(fp)
    return cardSet


def simple_guid_to_names(guid):
    if not os.path.isfile('Card Info/guid_to_names.json'):
        store_guid_to_names()
    # This avoids reloading the dictionary on every function call
    if not hasattr(simple_guid_to_names, "guid_dict"):
        with open('Card Info/guid_to_names.json') as fp:
            simple_guid_to_names.guid_dict = json.load(fp)
    name = 'Unknown card'
    try:
        name = simple_guid_to_names.guid_dict[guid]
    except KeyError:
        if config_handler.getter('verboseFlag'):
            print('Card with the following Guid could not be found: ' + guid)
        if guid != '00000000-0000-0000-0000-000000000000':  # Random guid that doesn't correspond to anything
            update()

    return name


def update(force=False):
    try:
        last_check = datetime.datetime.strptime(config_handler.getter('cardInfoCheck'), '%Y-%m-%d')
    except ValueError:
        last_check = datetime.datetime.min              # If string is malformed or empty we want to perform the download

    try:
        if last_check < datetime.datetime.today() - datetime.timedelta(days=1) or force: # Don't spam cwik's API with requests
            r = requests.post('http://hexdbapi2.hexsales.net/v1/objects/search')
            if config_handler.getter('verboseFlag'):
                print("Updated card info from cwik' API")
            with open('Card Info/card_info.json', 'w') as fp:
                json.dump(r.json(), fp, indent=4, sort_keys=True)
            config_handler.setter('cardInfoCheck', datetime.datetime.today().strftime('%Y-%m-%d'))  # update date of last download

            store_colors()                  # Update files
            store_rarity()
            store_guid_to_names()
            store_set()
            with open('Card Info/guid_to_names.json') as fp:        # Update guid_to_names with new values
                simple_guid_to_names.guid_dict = json.load(fp)
            if config_handler.getter('verboseFlag'):
                print('Updated colors, rarity, guid and set information')
    except Exception:
        if config_handler.getter('verboseFlag'):
            print("Could not update card info from cwik's API")


if __name__ == '__main__':
    update()
    # print(simple_colors())
    # print(set(simple_colors().values()))
    # print(simple_rarity())
    # store_set()
    # print(simple_set())
    # print()
    # simpleColors = simple_colors()
    # store_guid_to_names()
    # for card in simpleColors:
    #     colors = simpleColors[card]
    #     if ',' in colors:
    #         print(card + ':' + simpleColors[card])
    # max = 0
    # for card in simpleColors:
    #     if len(card) > max:
    #         print(card)
    #         max = len(card)