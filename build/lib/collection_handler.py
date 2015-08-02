# Copyright 2015, Ioannis Mouratidis, All rights reserved.
__author__ = 'Ioannis'

import os
import json
import csv
from ast import literal_eval

import card_info_handler
import AH_data_handler
import config_handler

os.makedirs('Collection', exist_ok=True)

# Takes a collection API message and a collection path and dumps the cards in a file in that path. Format:
# {
# "Action":"Update|Overwrite",
# "CardsAdded":[...],
# "CardsRemoved":[...],
# "User":"<NAME>",
# "Message":"Collection"
# }
# Each card has its own dict

def collection_update(jsonDict):
    PATH = 'Collection/My_Collection.json'
    if jsonDict['Action'] == 'Overwrite':
        myCollection = {}
    if jsonDict['Action'] == 'Update':
        myCollection = collection_open(PATH)

    for card in jsonDict['CardsAdded']:
        if card['Name'] in myCollection:
            myCollection[card['Name']] += 1
        else:
            myCollection[card['Name']] = 1

    for card in jsonDict['CardsRemoved']:
        if card['Name'] in myCollection:
            myCollection[card['Name']] -= 1

    with open(PATH, 'wt') as fp:
        json.dump(myCollection, fp, indent=4, sort_keys=True)

# Takes a collection path as argument
# Returns a dictionary of cards. Each card is paired with the number owned.
def collection_open(path):
    myCollection = {}
    try:
        with open(path, 'rt') as fp:
            cards = json.load(fp)
        for card in cards:
            if card in myCollection:
                myCollection[card] += 1
            else:
                myCollection[card] = cards[card]
    except (FileNotFoundError, ValueError):
        if path != 'Collection/My_Drafted_Cards.json':
            if config_handler.verboseFlag:
                print("Please update your collection by listing a card in the Auction House and then cancelling your auction")
    return myCollection

# Needs the file path name to determine whether we should add to the collection or to the drafted cards
def add_card(path, cardDict):
    myCollection = collection_open(path)
    try:
        if cardDict['Name'] in myCollection:
            myCollection[cardDict['Name']] += 1
        else:
            myCollection[cardDict['Name']] = 1
    except TypeError:
        myCollection = {}
        myCollection[cardDict['Name']] = 1

    with open(path, 'wt') as fp:
        json.dump(myCollection, fp, indent = 4, sort_keys=True)


# CAUTION: If you crash during draft Hex_API will send all cards you have picked until then for a second time
def draft_card_picked(path, cardName):
    add_card(path, cardName)

# Opens the AH-Data database created by Main.py
# Return a dictionary in this format: {(cardName, RarityNumber, Currency):(averagePrice, numberOfSales)}
def open_ah_data():
    with open('database.json', 'rt') as fp:
        cards = json.load(fp)

    # Converting keys to tuples
    # Without creating a temporary dict, "for key in cards" would run for the new keys too
    newCards = {}
    for key in cards:
        newCards[literal_eval(key)] = cards[key]
    cards = newCards

    return cards


# # Returns a dictionary of cards paired with their rounded average plat value. Doesn't take AAs into account
# def simple_plat_values():
#     ahData = open_ah_data()
#     platAHData = {}
#     for key in ahData:
#         if key[2] == 'PLATINUM' and key[1] != '5':
#             platAHData[key[0]] = round(ahData[key][0])
#     return platAHData


# WORK IN PROGRESS
def update_draft_value(value):
    with open('Collection/Draft_Values.json', 'r+t') as fp:
        try:
            drafts = json.load(fp)
            drafts[-1] += value                                 # Current draft
        except ValueError:
            drafts = []
        json.dump(drafts, fp, indent=4, sort_keys=True)


def export_collection():
    collection = collection_open('Collection/My_Collection.json')
    colors = card_info_handler.simple_colors()
    sets = card_info_handler.simple_set()
    rarities = card_info_handler.simple_rarity()
    prices = AH_data_handler.open_simple_median()
    with open("Collection/My_Collection.csv", 'wt')as fp:
        writer = csv.writer(fp, delimiter=';')
        writer.writerow(['Card', 'Price', 'Shard', 'Set', 'Rarity', 'Number Owned'])
        for key in collection:
            if key not in ('Blood Shard', 'Diamond Shard', 'Sapphire Shard', 'Ruby Shard', 'Wild Shard'):
                try:
                    price = prices[key.replace(',', '')]                                     # AH Data has no commas
                except:
                    price = 0
                writer.writerow([key, price, colors[key], sets[key], rarities[key], collection[key]])



if __name__ == '__main__':
    print(collection_open('Collection/My_Collection.json'))
    export_collection()









