import folium


mapObj = folium.Map(zoom_start=7, location=[37.566536, 126.977966])
"""folium.Marker(location=[37.566536, 126.977966],
             tooltip='Korean Capital',
              #popup='Seoul City'
              popup=folium.Popup('Seoul City', max_width=500)).add_to(mapObj)"""
# -----------------------------bootstrap--icons-----------------------------------------------
folium.Marker(location=[37.566536, 126.977966],
              tooltip='Korean Capital',
              icon=folium.Icon(icon='glyphicon-star', color='green'),
              popup=folium.Popup('Seoul City', max_width=500)).add_to(mapObj)
# -----------------------------fontawesome--icons-----------------------------------------------
folium.Marker(location=[35.179554, 129.075638],
              tooltip='Korean Capital',
              icon=folium.Icon(icon='plane', prefix='fa', color='blue'),
              popup=folium.Popup('Pusan City', max_width=500)).add_to(mapObj)
mapObj.save('map.html')
