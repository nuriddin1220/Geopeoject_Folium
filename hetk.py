from cmath import nan
import requests
import webbrowser
from geopy.distance import distance
import folium
import pyautogui
import pandas as pd
import openpyxl
import math
base_url='https://nominatim.openstreetmap.org/search?format=json'
city_name='Chortoq'
country="Oʻzbekiston"
city_resp=requests.get(f"{base_url}&country={country}&city={city_name}")
city_resp=city_resp.json()[1]
print(city_resp)
city_location=float(city_resp.get('lat')),float(city_resp.get('lon'))
print(city_location)
df = pd.read_excel("test.xlsx",index_col=False)
data=pd.DataFrame(df)
data_list=data.values.tolist()
width, height= pyautogui.size()
m=folium.Map(location=city_location,width=width,height=height,zoom_start=8)
for i in data_list:
    if math.isnan(i[4]):
        pass
    else:
        print('TR :',i[0])
        print('DCU number: ',i[1])
        print('DCU status: ',i[2])
        if i[2]=='Online':
            color="red"
        else :
            color="blue"
        print('online_offline: ',i[3])
        print('Lat: ',i[4])
        print('Lon: ',i[5])
        location=float(i[4]),float(i[5])
        folium.Marker(location,popup=f"<h6>TR: {i[0]}<br>DCU NUMBER: {i[1]}<br>DCU status: {i[2]}<br>ON_OFFLINE TIME: {i[3]}</h6>",tooltip='TR-'+str(i[0]),icon=folium.Icon(color=color),icon_size=(5, 5)).add_to(m)
m.save("map.html")
webbrowser.open("map.html")