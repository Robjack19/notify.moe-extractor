#extracting Notify userId

import requests 

def notifyId(username):
    url = 'https://notify.moe/api/nicktouser/'

    #checking if username is valid
   
    try:
        req = requests.get(url + username).json()
        userId = (req['userId'])
        return userId

    except:
        userId = 'null'
        return userId