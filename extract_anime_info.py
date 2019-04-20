from urllib.parse import urljoin
import requests


a = int(input("ENTER THE NUMBER OF YOUR ANIME: \n"))
a +=1

api_animelist = 'https://notify.moe/api/animelist/'

input_Id = str(input("ENTER YOU userId: \n"))
id = input_Id

url = urljoin(api_animelist , id) 

json_data = requests.get(url).json()
#print(json_data)

json_userId = json_data['userId']
print(json_userId)

i=0
for i in range(a):
   json_Id = json_data['items'][i]['animeId']
   json_status = json_data['items'][i]['status']
   print(json_Id +" | "+ json_status)