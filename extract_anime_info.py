import urllib.parse
import requests
import json

url = 'https://notify.moe/api/animelist/4J6qpK1ve'
#api_animelist = 'https:/notify.moe/api/animelist/'
#input_id = input("ENTER YOU userId: \n")
#id = input_Id
#url = api_animelist + urllib.parse.urlencode('id')

json_data = requests.get(url).json()
#print(json_data)

json_userId = json_data['userId']
print(json_userId)

json_Id = json_data['items'][0]['animeId']
json_status = json_data['items'][0]['status']
print(json_Id +" | "+ json_status)