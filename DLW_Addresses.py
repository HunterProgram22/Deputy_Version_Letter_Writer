from tinydb import TinyDB

def create_list():
    prison_db = TinyDB('C:\\Users\\kudelaj\\Desktop\\Prisons.json')
    PRISON_LIST = []
    for place in prison_db:
        PRISON_LIST.append(place['Institution_Name'])
    tuple(PRISON_LIST)
    return PRISON_LIST

PRISON_LIST = create_list()
PRISON_DB = TinyDB('C:\\Users\\kudelaj\\Desktop\\Prisons.json')
