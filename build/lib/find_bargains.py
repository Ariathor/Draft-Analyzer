__author__ = 'Ioannis'

import AH_data_handler
import collection_handler


myCollection = collection_handler.collection_open('Collection/My_Collection.json')
medianValues = AH_data_handler.short_term_median()
valuableCards = []

for card in myCollection:
    if myCollection[card] > 4:                             # Only sell cards I have more than 4-of
        for key in medianValues:
            # REMINDER: key = (cardName, rarity, currency)
            # For example, the following checks that the card name is equal to our selected card (that we have more than 4-of)
            # that we're looking at sales done with gold and the the card is not an AA (AA rarity = 5)
            if key[0] == card and key[2] == 'GOLD' and key[1]!='5':
                if medianValues[key][0] >= 1000:
                    valuableCards.append((key, medianValues[key]))

for item in valuableCards:
    print(item)