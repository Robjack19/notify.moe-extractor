#extracting anime list from notify.moe

import xml.etree.cElementTree as ET
import requests
import notifyId
import replace
import converter

username = str(input('Enter your notify.moe username:\n'))
userId = (notifyId.notifyId(username))
validity = False

if userId is 'null':
    print('Invalid username or unexpected error: \n')

elif userId is not 'null':
    validity = True 

while validity:
    print('Sucess: ')
    ausername = str(input('Enter your Anilist username: \n'))
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
        w, c, p, h, d, =  0, 0, 0, 0, 0
        Id, w ,c ,p ,h ,d = (replace.replace(nstatus[b]))

        aanimeId.append(Id)
        watching += w 
        completed += c 
        planned += p 
        hold += h 
        dropped += d 


    atotal = watching + completed + planned + hold + dropped
        
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
    convertedlistani = open('convertedlistani.xml','w')
    convertedlistani.write('<?xml version="1.0" encoding="UTF-8" ?>')

    myanimelist = ET.Element('myanimelist')
    myinfo = ET.SubElement(myanimelist, 'myinfo')
    anime = ET.SubElement(myanimelist,'anime')

    ET.SubElement(myinfo, 'user_id').text = ''
    ET.SubElement(myinfo, 'user_name').text = ausername
    ET.SubElement(myinfo, 'user_export_type').text = '1'
    ET.SubElement(myinfo, 'user_total_anime').text = str(atotal)
    ET.SubElement(myinfo, 'user_total_watching').text = str(watching)
    ET.SubElement(myinfo, 'user_total_completed').text = str(completed)
    ET.SubElement(myinfo, 'user_total_onhold').text = str(hold)
    ET.SubElement(myinfo, 'user_total_dropped').text = str(dropped)
    ET.SubElement(myinfo, 'user_total_plantowatch').text = str(planned)

    for d in range(noofanime):
        ET.SubElement(anime, 'series_animedb_id').text = str(aanimeId[d])
        ET.SubElement(anime, 'series_title').text = ''
        ET.SubElement(anime, 'series_type').text = ''
        ET.SubElement(anime, 'series_episodes').text = ''
        ET.SubElement(anime, 'my_id').text = '0'
        ET.SubElement(anime, 'my_watched_episodes').text = '0'
        ET.SubElement(anime, 'my_start_date').text = '0000-00-00'
        ET.SubElement(anime, 'my_finish_date').text = '0000-00-00'
        ET.SubElement(anime, 'my_rated').text = ''
        ET.SubElement(anime, 'my_score').text = '0'
        ET.SubElement(anime, 'my_dvd').text = ''
        ET.SubElement(anime, 'my_storage').text = ''
        ET.SubElement(anime, 'my_status').text = nstatus[d]
        ET.SubElement(anime, 'my_comments').text = ''
        ET.SubElement(anime, 'my_times_watched').text = ''
        ET.SubElement(anime, 'my_rewatch_value').text = ''
        ET.SubElement(anime, 'my_tags').text = ''
        ET.SubElement(anime, 'my_rewatching').text = '0'
        ET.SubElement(anime, 'my_rewatching_ep').text = '0'
        ET.SubElement(anime, 'update_on_import').text = '0'

    tree = ET.ElementTree(myanimelist)
    tree.write('convertedlistani.xml')
    convertedlistani.close()

    break