import folium 

mapObj=folium.Map(location=[37.098910662890795,126.97998046875001],zoom_start=7)
shapes_layer=folium.FeatureGroup(name="shapes").add_to(mapObj)
"""folium.Circle(radius=50000,location=[37.566536,126.977966],
            color='red',weight=4,fill=True,fill_color='blue',fill_opacity=0.7,stroke=False,tooltip='this is circle of 50 km',
              #popup='this is the Korean capital'
              popup=folium.Popup(
                  "Korean capital <b>Seoul</b> <div> <img src='https://img.freepik.com/premium-photo/sunset-seoul-city-seoul-tower-south-korea_258360-172.jpg?w=2000' alt='Seoul' style='max-width=150px;max-height:100px';</div>",max_width=500)
              ).add_to(mapObj) #raidus are calculated in meters"""
folium.Circle(radius=50000,location=[37.566536,126.977966],
            color='red',weight=4,fill=True,fill_color='blue',fill_opacity=0.7,stroke=False,tooltip='this is circle of 50 km',
            #popup='this is the Korean capital'
            popup=folium.Popup("Korean capital <b>Seoul</b> <div> <img src='https://img.freepik.com/premium-photo/sunset-seoul-city-seoul-tower-south-korea_258360-172.jpg?w=2000' alt='Seoul' style='max-width=150px;max-height:100px';</div>",max_width=500)).add_to(shapes_layer)
#folium.CircleMarker(radius=100,location=[37.566536,126.977966], #now radius in pixel in circlemarker and circle cant size in zooming
              #color='red',weight=4,fill=True,fill_color='blue',fill_opacity=0.7,stroke=False
              #).add_to(mapObj) #raidus are calculated in meters
folium.LayerControl().add_to(mapObj)
mapObj.save('map.html')