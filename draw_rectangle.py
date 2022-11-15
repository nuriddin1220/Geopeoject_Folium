import folium

mapObj = folium.Map(location=[37.566536, 126.977966], zoom_start=7)
shapesLayer = folium.FeatureGroup(name='shapes')
shapesLayer.add_to(mapObj)
"""folium.Rectangle(
    [(35.179554, 129.075638), (39.021389, 125.752747)], fill=True, weight=5, fill_color='orange', color='green', fill_opacity=0.8).add_to(mapObj)
"""
"""folium.PolyLine([(35.179554, 129.075638), (37.566536,
                126.977966), (39.021389, 125.752747)], color='red', weight=5).add_to(mapObj)
"""
folium.Polygon([(35.179554, 129.075638), (37.566536,
                126.977966), (39.021389, 125.752747), (36.330101, 127.422470)], color='red', weight=5).add_to(shapesLayer)
folium.LayerControl().add_to(mapObj)
mapObj.save('map.html')
