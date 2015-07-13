__author__ = 'Ioannis'

import requests

data1 = '["DraftPack","Ariathor",["Feral Ogre","Construction Plans: Crank Rocket","Shin\'hare Militia","Shadowblade Lurker","Technical Genius","Hop\'hiro, Samurai", "Archmage Wrenlocke"]]'
data2 = '["DraftPack","Ariathor",["Grand Squirrel Titan","Kog\'tepetl\'s Thirst","Wounded War Hero","Ambling Bluff","Excavation Hulk","Grave Nibbler","Spirit Oracle","Adrenaline Rush","Lethal Weapons","Underfoot Commander","Timestep Magistrate","Dread Monolith","Tome of Knowledge", "HAHAHA", "TEST"]]'
data3 = '["DaraftCardPicked","Ariathor",["Allo Kitty"]]'
data4 = '["DaraftCardPicked","Ariathor",["Charge Hulk"]]'
data5 = '["DaraftCardPicked","Ariathor",["Hop\'hiro, Samurai"]]'
data6 = '["DaraftCardPicked","Ariathor",["Shin\'hare Militia"]]'
data7 = '["DraftPack","Ariathor",["Royal Herald", "Mindcaller", "Grand Squirrel Titan","Kog\'tepetl\'s Thirst","Wounded War Hero","Ambling Bluff","Excavation Hulk","Grave Nibbler","Spirit Oracle","Adrenaline Rush","Lethal Weapons","Underfoot Commander","Timestep Magistrate","Dread Monolith","Tome of Knowledge"]]'
data8 = '["DaraftCardPicked","Ariathor",["Royal Herald"]]'
data9 = '{"User":"Risterral", "Message":"DraftPack", "Cards":["Grand Squirrel Titan","Kog\'tepetl\'s Thirst","Wounded War Hero","Ambling Bluff","Excavation Hulk","Grave Nibbler","Spirit Oracle","Adrenaline Rush","Lethal Weapons","Underfoot Commander","Timestep Magistrate","Dread Monolith","Tome of Knowledge", "HAHAHA", "TEST"]}'
data10 = '{"User":"Risterral", "Message":"DraftCardPicked", "Card":"Xentoth\'s Inquisitor"}'
data11 = '{"User":"Risterral", "Message":"GameStarted", "Players":["Risterral","PlayerName2","PlayerName3"]}'
# r = requests.post('http://localhost:18888/store.json', data2)
# print(r)
# print(r.status_code)
# print(r.headers)
# print(r.content)
# print(r.request.headers)

def test():
        r = requests.post('http://localhost:18888/draft_analyzer', data1)
        r = requests.post('http://localhost:18888/draft_analyzer', data2)
        r = requests.post('http://localhost:18888/draft_analyzer', data3)
        r = requests.post('http://localhost:18888/draft_analyzer', data4)
        r = requests.post('http://localhost:18888/draft_analyzer', data5)
        r = requests.post('http://localhost:18888/draft_analyzer', data6)

if __name__ == '__main__':
        #test()
        r = requests.post('http://localhost:18888/draft_analyzer', data9)
        r = requests.post('http://localhost:18888/draft_analyzer', data10)
        r = requests.post('http://localhost:18888/draft_analyzer', data11)