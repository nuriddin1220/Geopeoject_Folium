import folium

mapObj = folium.Map(zoom_start=7, location=[37.566536, 126.977966])

mapObj.get_root().html.add_child(folium.Element(
    """
    <div style='position:fixed;left:70px;top:20px;width:200px;height:200px;z-index:900'>
    <h3><strong>Korean Penincuela</strong></h3>
    <button>South Korea</button>
    <button>North Korea</button>
    </div>
    """
))
mapObj.save('map.html')
