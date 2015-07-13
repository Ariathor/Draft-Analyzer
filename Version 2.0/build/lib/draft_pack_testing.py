__author__ = 'Ioannis'

import requests

data1 = '["DraftPack","Ariathor",["Feral Ogre","Construction Plans: Crank Rocket","Shin\'hare Militia","Shadowblade Lurker","Technical Genius","Hop\'hiro, Samurai", "Archmage Wrenlocke"]]'
data2 = '["DraftPack","Ariathor",["Grand Squirrel Titan","Kog\'tepetl\'s Thirst","Wounded War Hero","Ambling Bluff","Excavation Hulk","Grave Nibbler","Spirit Oracle","Adrenaline Rush","Lethal Weapons","Underfoot Commander","Timestep Magistrate","Dread Monolith","Tome of Knowledge", "HAHAHA", "TEST"]]'
data3 = '["DaraftCardPicked","Ariathor",["Allo Kitty"]]'
data4 = '["DaraftCardPicked","Ariathor",["Charge Hulk"]]'
data5 = '["DaraftCardPicked","Ariathor",["Hop\'hiro, Samurai"]]'
data6 = '["DaraftCardPicked","Ariathor",["Shin\'hare Militia"]]'
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
        test()
