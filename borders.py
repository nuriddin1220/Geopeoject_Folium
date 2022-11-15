import folium
import requests
# mapObj=folium.Map(location=[51.19252754196984,9.338378906250002],zoom_start=7)
mapObj = folium.Map(location=[37.098910662890795,
                    126.97998046875001], zoom_start=7)
bordersStyle = {
    'color': 'green',
    'opacity': 0.5,
    'weight': 1,
    'fillColor': 'yellow',
    'fillOpacity': 0.1
}
# folium.GeoJson("geojson_files/uzbekistan_regional.geojson",name='Uzbeksitan',
#               style_function=lambda x:bordersStyle).add_to(mapObj)
response_text = requests.get(
    'https://raw.githubusercontent.com/southkorea/southkorea-maps/master/gadm/json/skorea-provinces-geo.json').text
folium.GeoJson(response_text, name='South Korea',
               style_function=lambda x: bordersStyle).add_to(mapObj)
response_text2 = requests.get(
    'https://raw.githubusercontent.com/glynnbird/countriesgeojson/master/north%20korea.geojson').text
folium.GeoJson(response_text2, name='North Korea',
               style_function=lambda x: bordersStyle).add_to(mapObj)
folium.LayerControl().add_to(mapObj)
mapObj.save("map.html")
