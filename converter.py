import requests        

def converter(nanimeId):
    url = 'https://notify.moe/api/anime/'
    aanimeId = ''
    links = []
    link = ''
    aindex = ''

    req = requests.get(url + nanimeId).json()

    find = req['mappings']
    
    noofentries = len(find)

    for b in range(noofentries):
        links.append(str(req['mappings'][b]['service']))

    for c in range(noofentries):
            link = (find[c]['service'])
            if link == 'anilist/anime':

                aindex = link.index('anilist/anime')
                aanimeId = (find[aindex]['serviceId'])
                return aanimeId


