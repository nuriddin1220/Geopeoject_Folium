import folium 
#import webbrowser
#-------------------------------------------------------------Layers.tiles------------------------------------------------------
"""
mapObj=folium.Map(location=[41.3117047941392, 69.27960480057175],zoom_start=16,tiles='openstreetmap')
                #tiles=None ---no tiles
                #,zoom_control=False)
folium.TileLayer('Stamen Terrain',attr='Stamen Terrain').add_to(mapObj)
folium.TileLayer('Stamen Toner',attr='Stamen Toner').add_to(mapObj)
folium.TileLayer('Stamen Watercolor',attr='Stamen Watercolor').add_to(mapObj)
folium.TileLayer('CartoDB positron',attr='CartoDB positron').add_to(mapObj)
folium.TileLayer(tiles='https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',attr='OpenStreetMap.HOT',name='OpenStreetMap.HOT').add_to(mapObj)
folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',attr='Esri.WorldImagery',name='Esri.WorldImagery').add_to(mapObj)
folium.LayerControl(position='bottomright',collapsed=True).add_to(mapObj)
"""
#----------------------------------------------working--with--borders---------------------------------------------------------------------------




mapObj.save("map.html")
#webbrowser.open("map.html")