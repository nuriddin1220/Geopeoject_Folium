import folium 
from selenium import webdriver
import os
import time
mapObj=folium.Map(location=[37.098910662890795,126.97998046875001],zoom_start=7)
shapes_layer=folium.FeatureGroup(name="shapes").add_to(mapObj)

folium.Circle(radius=50000,location=[37.566536,126.977966],
            color='red',weight=4,fill=True,fill_color='blue',fill_opacity=0.7,stroke=False,tooltip='this is circle of 50 km',
            popup=folium.Popup("Korean capital <b>Seoul</b> <div> <img src='https://img.freepik.com/premium-photo/sunset-seoul-city-seoul-tower-south-korea_258360-172.jpg?w=2000' alt='Seoul' style='max-width=150px;max-height:100px';</div>",max_width=500)).add_to(shapes_layer)
folium.LayerControl().add_to(shapes_layer)
map_name='map.html'
mapObj.save(map_name)
print(os.getcwd())
mapUrl='file://{0}/{1}'.format(os.getcwd(),map_name )
driver=webdriver.Chrome()
driver.get(mapUrl)
time.sleep(5)
driver.save_screenshot('map.png')
driver.quit()