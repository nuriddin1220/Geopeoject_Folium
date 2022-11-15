import folium

mapObj = folium.Map(zoom_start=7, location=[37.566536, 126.977966])
folium.Marker(location=[36.693474, 128.004915],
              icon=folium.DivIcon(html="""
                                  <span><h3>South Korea</h3></span>
                                  """, class_name='mapText')
              ).add_to(mapObj)
mapObj.get_root().html.add_child(folium.Element(
    """
    <style>
    .mapText{
        color:blue;
        font-size:large;
        white-space:nowrap;
    }
    </style>
    """
))
mapObj.save('map.html')
