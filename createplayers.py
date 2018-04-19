import random
def create_player(num):
    nlist='abcdefghijklmnopqrstuvwxyz'
    players=[]
    for i in range(0,num):
        name=''
        name+=random.choice(nlist)+random.choice(nlist)+random.choice(nlist)
        players.append(name)
    return players

def mould_player(players_name):
    character=[{"t":'echo','m':10,'f':'t'},{"t":'pink','m':10,'f':'t'},{"t":'faker','m':10,'f':'f'},{"t":'iron','m':10,'f':'t'},{"t":'spy','m':10,'f':'t'}]
    players={}
    for i in players_name:
        players[i]=random.choice(character)
    return players
