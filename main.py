import requests
import webbrowser
from geopy.distance import distance
import folium
import pyautogui
base_url='https://nominatim.openstreetmap.org/search?format=json'
postcode='G42 9AY'
city_name='Tashkent'
response=requests.get(f"{base_url}&postalcode={postcode}")
response2=requests.get(f"{base_url}&city={city_name}")
data=response.json()
data2=response2.json()
lattitude=data[0].get('lat')
longtitude=data[0].get('lon')
location3=float(data2[0].get('lat')),float(data2[0].get('lon'))
location=float(lattitude),float(longtitude)
location2=float(lattitude)-1,float(longtitude)-1
width, height= pyautogui.size()
m=folium.Map(location=location,width=width,height=height,zoom_start=8)
tooltip = "Click me!"
folium.Marker(location,popup='Glasgov Postcode',tooltip=tooltip).add_to(m)
folium.Marker(location2,popup='somewhere Postcode',tooltip=tooltip).add_to(m)
folium.Marker(location3,popup=city_name,tooltip=tooltip).add_to(m)
folium.PolyLine((location,location2)).add_to(m)
folium.PolyLine((location,location3)).add_to(m)
m.save("map.html")
webbrowser.open("map.html")
km=distance(location,location2)
miles=distance(location,location2).miles
print(km," ,",miles," miles")
print(pyautogui.size())

