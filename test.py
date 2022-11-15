import folium
import webbrowser
import base64
from folium import IFrame
encoded = base64.b64encode(open('mypic.jpg', 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=250, height=250)
popup = folium.Popup(iframe)
#different dtyle can be for mapping 
#m=folium.Map(location=[41.311081,69.240562],tiles='Stamen Watercolor',zoom_start=10)
my_first_icon=folium.features.CustomIcon('askue.jpg',icon_size=(70,70))
m=folium.Map(location=[41.305539982037985, 69.27947968028873],zoom_start=12)
folium.Marker(location=[41.305539982037985, 69.27947968028873],popup='HETK AJ',tooltip='ASKUE DEPARTMENT',icon=my_first_icon).add_to(m)
#folium.Marker(location=[41.33350184899742, 69.29862864198834],popup='Gijduvon Kafe',tooltip='Gijduvon',icon=folium.Icon(icon='home',color='red')).add_to(m)
folium.Marker(location=[41.37311860784571, 69.3182790370898],popup=popup,tooltip='Islom Akani Uyi',icon=folium.Icon(icon='home',color='red')).add_to(m)
folium.PolyLine(([41.305539982037985, 69.27947968028873],[41.37311860784571, 69.3182790370898])).add_to(m)
m.save('map.html')
webbrowser.open("map.html")