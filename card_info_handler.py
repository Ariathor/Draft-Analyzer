# Copyright 2015, Ioannis Mouratidis, All rights reserved.
__author__ = 'Ioannis'

import json
import os.path

import config_handler

#Possible Improvement: Download data from cwik's API automatically

def store_colors():
    os.makedirs('Card Info', exist_ok=True)
    with open('Card Info/card_info.json', 'rt') as fp:
        response = json.load(fp)

    if not response["error"] and response["status"] == 200:
        cardInfo = response["data"]
    else:
        if config_handler.verboseFlag:
            print("Data not downloaded correctly")

    cardColors = {}                    #Dictionary that relates cards to their threshold requirements
    for cardDict in cardInfo:
        if cardDict['set_id'] not in ('ArenaEquipment', 'BoosterPack','Gem'):           #Ignoring non-cards
            if cardDict['rarity'] in ('Common', 'Uncommon', 'Rare', 'Legendary'):       #Ignoring AAs, champions and non-collectible cards
                cardColors[cardDict['name']] = cardDict['color']
    with open('Card Info/simple_colors.json', 'wt') as fp:
        json.dump(cardColors, fp, indent=4, sort_keys=True)


def store_rarity():
    os.makedirs('Card Info', exist_ok=True)
    with open('Card Info/card_info.json', 'rt') as fp:
        response = json.load(fp)

    if not response["error"] and response["status"] == 200:
        cardInfo = response["data"]
    else:
        if config_handler.verboseFlag:
            print("Data not downloaded correctly")


    cardRarity = {}
    for cardDict in cardInfo:
        if cardDict['set_id'] not in ('BoosterPack','Gem'):                             #Ignoring non-cards
            if cardDict['rarity'] in ('Common', 'Uncommon', 'Rare', 'Legendary'):       #Ignoring AAs, champions and non-collectible cards
                cardRarity[cardDict['name']] = cardDict['rarity']

    with open('Card Info/simple_rarity.json', 'wt') as fp:
        json.dump(cardRarity, fp, indent=4, sort_keys=True)

def store_set():
    os.makedirs('Card Info', exist_ok=True)
    with open('Card Info/card_info.json', 'rt') as fp:
        response = json.load(fp)

    if not response["error"] and response["status"] == 200:
        cardInfo = response["data"]
    else:
        if config_handler.verboseFlag:
            print("Data not downloaded correctly")

    cardSet = {}
    translation = {'001': 'Shards of Fate',
                   '002': 'Shattered Destiny',
                   '003': 'Armies of Myth',
                   'PVE001': 'Frost Ring Arena',
                   }

    for cardDict in cardInfo:
        if cardDict['set_id'] not in ('BoosterPack','Gem'):                             #Ignoring non-cards
            if cardDict['rarity'] in ('Common', 'Uncommon', 'Rare', 'Legendary'):       #Ignoring AAs, champions and non-collectible cards
                try:
                    traslatedSet = translation[cardDict['set_id']]
                except KeyError:
                    traslatedSet = cardDict['set_id']
                cardSet[cardDict['name']] = traslatedSet

    with open('Card Info/simple_set.json', 'wt') as fp:
        json.dump(cardSet, fp, indent=4, sort_keys=True)


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




if __name__ == '__main__':
    store_colors()
    print(simple_colors())
    print(set(simple_colors().values()))
    print(simple_rarity())
    store_set()
    print(simple_set())
    print()