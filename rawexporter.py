import requests

api_animelist = 'https://notify.moe/api/animelist/'
try1 = False

#Getting userId from Nick
user_info = 'https://notify.moe/api/nicktouser/'
user= str(input("ENTER YOUR NOTIFY.MOE USERNAME: \n"))

#checking if entered nick exists
try:
       req = requests.get(user_info + user).json()
       Id = (req['userId'])
       try1 = True
       json_data = requests.get(api_animelist + Id).json()

except:
       print('USERNAME "' + user + '" NOT FOUND')


#on true start program          
while try1:
       #requesting user to input their Anilist username
       usernam = str(input("ENTER YOU'R ANILIST USERNAME:  \n"))

       #getting number of anime from json file
       a = int(len((json_data['items'])))

       #storing status to be later inputed in .xml file
       store_Id = []
       store_status = []
       watching = 0
       completed = 0
       planned = 0
       hold = 0
       dropped = 0
       
       print('Adding status')
       i = int(0)
       for i in range(a):
       #values stored in list form
              store_Id.append(json_data['items'][i]['animeId'])
              store_status.append(json_data['items'][i]['status'])

       #getting status type and replacing it
       j = int(0)
       for j in range(a):
              #arranging status
              if store_status[j]== 'watching':
                     watching += 1
                     store_status[j] = str('Watching')

              elif store_status[j] == 'completed':
                     completed += 1
                     store_status[j] = str('Completed')

              elif store_status[j] == 'planned':
                     planned += 1
                     store_status[j] = str('Plan to watch')
                     
              elif store_status[j] == 'hold':
                     hold += 1
                     store_status[j] = str('Paused')

              elif store_status[j] == 'dropped':
                     dropped += 1
                     store_status[j] = str('Dropped')

              else:
                     store_Id.pop(j)
                     store_status.pop(j)
                    
                 
       #getting total number of each variable
       watching = str(watching)
       completed = str(completed)
       planned = str(planned)
       hold = str(hold)
       dropped = str(dropped)

       
       print("Replacing Id's")

       #now getting anilist Id's
       anime_api_url = 'https://notify.moe/api/anime/'
       store_Id_ani = []
       q = []
       for g in range(a):
              url_ani = requests.get(anime_api_url + store_Id[g]).json()

              mapp = url_ani['mappings']
              
              len_mapp = len(mapp)

              for m in range(len_mapp):
                     q.append(url_ani['mappings'][m]['service'])

              k =[]
              
              for f in range(len_mapp):
                     k = (mapp[f]['service'])
                     if k == 'anilist/anime':

                            z =k.index('anilist/anime')
                            store_Id_ani.append(mapp[z]['serviceId'])
                            
                     #else:
                            #store_Id.pop(f)
                            #store_status.pop(f)

       #now add id's to format and done?
       #following 3 are test variables
       nam = str('')
       ep = str('0')
       wano = str('0')

       print('Importing to xml')
       #converting into anilist xml file--
       refresh = open('anilistlist.xml','w')
       refresh.write('')
       refresh.close()

       scrape_anilist = open('anilistlist.xml','a')
       scrape_anilist.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
       scrape_anilist.write('<myanimelist>\n')
       scrape_anilist.write('      <myinfo>\n')
       scrape_anilist.write('             <user_id></user_id>\n')
       scrape_anilist.write('             <user_name>' + usernam +'</user_name>\n')
       scrape_anilist.write('             <user_export_type>1</user_export_type>\n')
       scrape_anilist.write('             <user_total_anime>' + str(a) + '</user_total_anime>\n')
       scrape_anilist.write('             <user_total_watching>' + watching +'</user_total_watching>\n')
       scrape_anilist.write('             <user_total_completed>' + completed + '</user_total_completed>\n')
       scrape_anilist.write('             <user_total_onhold>' + hold +'</user_total_onhold>\n')
       scrape_anilist.write('             <user_total_dropped>' + dropped + '</user_total_dropped>\n')
       scrape_anilist.write('             <user_total_plantowatch>' + planned +'</user_total_plantowatch>\n')
       scrape_anilist.write('      </myinfo>\n')


       r = int(0)
       for r in range(a):
              scrape_anilist.write('      <anime>\n')
              scrape_anilist.write('           <series_animedb_id>' + store_Id_ani[r] + '</series_animedb_id>\n')
              scrape_anilist.write('           <series_title><![CDATA[' + nam + ']]></series_title>\n')
              scrape_anilist.write('           <series_type></series_type>\n')
              scrape_anilist.write('           <series_episodes>' + ep + '</series_episodes>\n')
              scrape_anilist.write('           <my_id>0</my_id>\n')
              scrape_anilist.write('           <my_watched_episodes>' + wano + '</my_watched_episodes>\n')
              scrape_anilist.write('           <my_start_date>0000-00-00</my_start_date>\n')
              scrape_anilist.write('           <my_finish_date>0000-00-00</my_finish_date>\n')
              scrape_anilist.write('           <my_rated></my_rated>\n')
              scrape_anilist.write('           <my_score>0</my_score>\n')
              scrape_anilist.write('           <my_dvd></my_dvd>\n')
              scrape_anilist.write('           <my_storage></my_storage>\n')
              scrape_anilist.write('           <my_status>' + store_status[r] +'</my_status>\n')
              scrape_anilist.write('           <my_comments><![CDATA[]]></my_comments>\n')
              scrape_anilist.write('           <my_times_watched>0</my_times_watched>\n')
              scrape_anilist.write('           <my_rewatch_value></my_rewatch_value>\n')
              scrape_anilist.write('           <my_rewatching>0</my_rewatching>\n')
              scrape_anilist.write('           <my_rewatching_ep>0</my_rewatching_ep>\n')
              scrape_anilist.write('           <update_on_import>0</update_on_import>\n')
              scrape_anilist.write('      </anime>\n')


       scrape_anilist.write('</myanimelist>\n')
       scrape_anilist.close()
       print('Done')
       break
#--END-- 