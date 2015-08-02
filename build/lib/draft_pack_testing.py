__author__ = 'Ioannis'

import requests
import time

data1 = '["DraftPack","Ariathor",["Feral Ogre","Construction Plans: Crank Rocket","Shin\'hare Militia","Shadowblade Lurker","Technical Genius","Hop\'hiro, Samurai", "Archmage Wrenlocke"]]'
data2 = '["DraftPack","Ariathor",["Grand Squirrel Titan","Kog\'tepetl\'s Thirst","Wounded War Hero","Ambling Bluff","Excavation Hulk","Grave Nibbler","Dreamsmoke Mystic","Adrenaline Rush","Lethal Weapons","Underfoot Commander","Timestep Magistrate","Dread Monolith","Tome of Knowledge", "Lanupaw, Prophet of Fate", "TEST"]]'
data3 = '["DaraftCardPicked","Ariathor",["Allo Kitty"]]'
data4 = '["DaraftCardPicked","Ariathor",["Charge Hulk"]]'
data5 = '["DaraftCardPicked","Ariathor",["Hop\'hiro, Samurai"]]'
data6 = '["DaraftCardPicked","Ariathor",["Shin\'hare Militia"]]'
data7 = '["DraftPack","Ariathor",["Royal Herald", "Mindcaller", "Grand Squirrel Titan","Kog\'tepetl\'s Thirst","Wounded War Hero","Ambling Bluff","Excavation Hulk","Grave Nibbler","Spirit Oracle","Adrenaline Rush","Lethal Weapons","Underfoot Commander","Timestep Magistrate","Dread Monolith","Tome of Knowledge"]]'
data8 = '["DaraftCardPicked","Ariathor",["Royal Herald"]]'
data9 = '{"Card":{"Name":"Hempseed Dryad","Flags":"","Guid":{"m_Guid":"53c82b95-aad0-4210-96f1-7e11c71df985"},"Gems":[]},"User":"Ariathor","Message":"DraftCardPicked"}'
data10 = '{"Cards":[{"Name":"Hempseed Dryad","Flags":"","Guid":{"m_Guid":"53c82b95-aad0-4210-96f1-7e11c71df985"},"Gems":[]}],"User":"Ariathor","Message":"DraftPack"}'
data11 = '{"Cards":[{"Name":"Dreamsmoke Mystic","Flags":"","Guid":{"m_Guid":"8e644857-602c-4dad-a115-086717be58a3"},"Gems":[]},{"Name":"Bloatcap","Flags":"","Guid":{"m_Guid":"702f45ec-c117-4fc2-9e38-1b9e66ebb8ad"},"Gems":[]},{"Name":"Etherealize","Flags":"","Guid":{"m_Guid":"46eedbaf-fcfa-47f6-b4b1-001c446ff32c"},"Gems":[]},{"Name":"Snarling Ambusher","Flags":"","Guid":{"m_Guid":"e33bb5b7-1b69-481e-99cc-b5fcdc352cf6"},"Gems":[]},{"Name":"Swordplay","Flags":"","Guid":{"m_Guid":"af2345c1-7dde-44e9-9bc3-d3818679e189"},"Gems":[]}],"User":"Ariathor","Message":"DraftPack"}'
data12 = '{"Message": "DraftPack", "Cards": [{"Name": "Brightmoon Brave", "Flags": "", "Gems": [], "Guid": {"m_Guid": "74454a5c-1fd5-4d89-a775-72b96830f247"}}, {"Name": "Taint", "Flags": "", "Gems": [], "Guid": {"m_Guid": "8259e05a-043c-42fd-a49c-50ac5ae2fed5"}}, {"Name": "Vine Lash", "Flags": "", "Gems": [], "Guid": {"m_Guid": "9f4f19de-70a8-47d6-9465-3bda793135a5"}}, {"Name": "Thunderfield Seer", "Flags": "", "Gems": [], "Guid": {"m_Guid": "a9224795-471a-48b7-9c79-80ca547a920b"}}, {"Name": "Etherealize", "Flags": "", "Gems": [], "Guid": {"m_Guid": "46eedbaf-fcfa-47f6-b4b1-001c446ff32c"}}, {"Name": "Merry Minstrels", "Flags": "", "Gems": [], "Guid": {"m_Guid": "730ea063-830a-4433-a3e9-e62972dda465"}}, {"Name": "Sepulchra Bonewalker", "Flags": "", "Gems": [], "Guid": {"m_Guid": "64d41ff0-fa0e-437e-b88b-48346db1aebd"}}, {"Name": "Predatory Prey", "Flags": "", "Gems": [], "Guid": {"m_Guid": "2c4f416c-4faf-408e-a8c1-f807f9296b4d"}}, {"Name": "Skewer", "Flags": "", "Gems": [], "Guid": {"m_Guid": "0d7abbcc-af4a-457e-b3dd-d5e5ff3b7376"}}, {"Name": "Frigid Buffalo", "Flags": "", "Gems": [], "Guid": {"m_Guid": "4310820a-bbc5-430d-a34f-7783bb26032b"}}, {"Name": "Hatchery Broodguard", "Flags": "", "Gems": [], "Guid": {"m_Guid": "a4ef5dd1-4aac-4922-82c7-dc234d413609"}}, {"Name": "Bombwright", "Flags": "", "Gems": [], "Guid": {"m_Guid": "de31cf44-324f-4a50-acf9-6d0b5f2b236c"}}, {"Name": "Chimera Guard Fallen", "Flags": "", "Gems": [], "Guid": {"m_Guid": "0ea8b19a-8d3f-4a82-854a-e37541639a81"}}, {"Name": "Flamehand Invoker", "Flags": "", "Gems": [], "Guid": {"m_Guid": "8a291bed-c5ea-4016-9fe5-a42d87bbc24e"}}, {"Name": "Starsphere", "Flags": "", "Gems": [], "Guid": {"m_Guid": "0f928c81-da82-4ca0-a0d9-f50d80e4d9ee"}}], "User": "Ariathor"}'
data13 = '{"User":"Risterral", "Message":"GameStarted", "Players":["Risterral","PlayerName2","PlayerName3"]}'
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

def test2():
    r = requests.post('http://localhost:18888/draft_analyzer', data9)
    r = requests.post('http://localhost:18888/draft_analyzer', data10)
    r = requests.post('http://localhost:18888/draft_analyzer', data11)
    r = requests.post('http://localhost:18888/draft_analyzer', data12)
    r = requests.post('http://localhost:18888/draft_analyzer', data13)

def test3():
    data1='["DraftPack","Ariathor",["Dementia Daisies","Ambling Bluff","Rotting Buffalo","Strength of the Redwood","Immortal Tears","Field Tactician","Boulder Toss","Killblade of the Milky Eye","Construction Plans: Hornet Bot","Mazat Spearman","Bucktooth Bannerbunny","Mentor of the Flames","Royal Enforcer","Royal Diplomat","Zakiir"]]'
    data2='["DraftPack","Ariathor",["Immortal Tears","Duskwing Outrider","Careful Rummaging","Grand Squirrel Titan","Sly Huntress","War Bot Bunker","Underground Overdriver","Bastion of Adamanth","Brutal Bonecracker","Thorntongue Snapdragon","Overtime Bot","Sentinel of Nulzann","Inductocopter Bot","Immortal Decree"]]'
    data3='["DraftPack","Ariathor",["Ridge Raider","Tormented Ritualist","Augmented Awakening","Crackling Sprout","S.P.A.M. Bot","Kraken Guard Seapriest","Feeding the Young Ones","Battle Hardened Pa","Overtime Bot","Hawkwind","Dread Monolith","Time Wave","Highlands Shinobi"]]'
    data4='["DraftPack","Ariathor",["Dragon Guard Stalwart","To the Skies!","Compost","Burrow Bunny","Ridge Raider","Murmurs From The Void","Arena Regular","Crackling Boon","Sterling Starwatcher","Mentor of the Grave","Shard of Conquest","Shard of Savagery"]]'
    data5='["DraftPack","Ariathor",["Sterling Starwatcher","Immortal Tears","Cunning Skullcaster","Duskwing Outrider","Blossoming Concubunny","Flak Scrapper","Armitron","Maniacal Entrepreneur","Field Tactician","Underfoot Commander","Scraptech Brawler"]]'
    data6='["DraftPack","Ariathor",["Cunning Skullcaster","Duskwing Outrider","Blossoming Concubunny","Mesmeric Hypnoscientist","Killblade of the Milky Eye","Mindcaller","Recovery Specialist","Child of Rust","Rallying Banner","Necrophage Sensei"]]'
    data7='["DraftPack","Ariathor",["Fish Hands","Manti Ranger","Dragon Guard Stalwart","To the Skies!","Preservation","Murmurs From The Void","Adrenaline Rush","Child of Rust","Shard of Cunning"]]'
    data8='["DraftPack","Ariathor",["Surprise Runt Gang","Fish Hands","Light Of Hope","Overtime Bot","Cottontail Scout","Ridge Raider","Starfire Totemist","Necrophage Sensei"]]'
    data9='["DraftPack","Ariathor",["Dementia Daisies","Ambling Bluff","Rotting Buffalo","Immortal Tears","Field Tactician","Mazat Spearman","Bucktooth Bannerbunny"]]'
    data10='["DraftPack","Ariathor",["Duskwing Outrider","Careful Rummaging","Grand Squirrel Titan","War Bot Bunker","Thorntongue Snapdragon","Overtime Bot"]]'
    data11='["DraftPack","Ariathor",["Ridge Raider","Feeding the Young Ones","Overtime Bot","Hawkwind","Time Wave"]]'
    data12='["DraftPack","Ariathor",["Dragon Guard Stalwart","Compost","Burrow Bunny","Crackling Boon"]]'
    data13='["DraftPack","Ariathor",["Cunning Skullcaster","Duskwing Outrider","Maniacal Entrepreneur"]]'
    data14='["DraftPack","Ariathor",["Cunning Skullcaster","Duskwing Outrider"]]'
    data15='["DraftPack","Ariathor",["Fish Hands"]]'

    r = requests.post('http://localhost:18888/draft_analyzer', data1)
    r = requests.post('http://localhost:18888/draft_analyzer', data2)
    r = requests.post('http://localhost:18888/draft_analyzer', data3)
    r = requests.post('http://localhost:18888/draft_analyzer', data4)
    r = requests.post('http://localhost:18888/draft_analyzer', data5)
    r = requests.post('http://localhost:18888/draft_analyzer', data6)
    r = requests.post('http://localhost:18888/draft_analyzer', data7)
    r = requests.post('http://localhost:18888/draft_analyzer', data8)
    r = requests.post('http://localhost:18888/draft_analyzer', data9)
    r = requests.post('http://localhost:18888/draft_analyzer', data10)
    r = requests.post('http://localhost:18888/draft_analyzer', data11)
    r = requests.post('http://localhost:18888/draft_analyzer', data12)
    r = requests.post('http://localhost:18888/draft_analyzer', data13)
    r = requests.post('http://localhost:18888/draft_analyzer', data14)
    r = requests.post('http://localhost:18888/draft_analyzer', data15)
    print(r)
    print(r.status_code)
    print(r.headers)
    print(r.content)
    print(r.request.headers)

def test4():
    data1='["Collection","Ariathor",["Fish Hands"]]'
    data2='["Collection","Ariathor",["Adamanthian Scrivener"]]'

    r = requests.post('http://localhost:18888/draft_analyzer', data1)
    r = requests.post('http://localhost:18888/draft_analyzer', data2)


if __name__ == '__main__':
    #test()
    test2()
    #for i in range(100):
    #        r = requests.post('http://localhost:18888/draft_analyzer', data2)
    #test3()
    #test4()
