#extracting anime list from notify.moe

import requests
import notifyId
import replace
import converter
import builder

username = str(input('Enter your notify.moe username:\n'))
userId = (notifyId.notifyId(username))
validity = False

if userId is 'null':
    print('Invalid username or unexpected error: \n')

elif userId is not 'null':
    validity = True 

while validity:
    print('Sucess: ')
    url = 'https://notify.moe/api/animelist/'

    nanimeId = []
    nstatus = []
    aanimeId = []
    astatus = []

    watching = 0
    completed = 0
    planned = 0
    hold = 0
    dropped =0

    req = requests.get(url + userId).json()
    noofanime = int(len((req['items'])))

    #print('Number of anime:' + str(noofanime) + '\n')

    for a in range(noofanime):
        nanimeId.append(req['items'][a]['animeId'])
        nstatus.append(req['items'][a]['status'])
    
    #arranging status
    print('Replacing status: ')
    for b in range(noofanime):
        astatus.append(replace.replace(nstatus[b]))
        
    print('Done! ')
    #replacing Id's
    print('Replacing ID\'s: ')
    for c in range(noofanime):
        aanimeId.append(converter.converter(nanimeId[c]))

        #removing anime without anilist links
        if aanimeId[c] == None:
            aanimeId.pop(c)
            astatus.pop(c) 
    print('Done! ')
    #print(aanimeId)
    #print(astatus)
    #building .xml file
    print('Now Building: ')

    break