import folium

mapObj = folium.Map(zoom_start=7, location=[37.566536, 126.977966])
folium.Marker(location=[36.693474, 128.004915],
              icon=folium.DivIcon(html="""
                                  <span><h3>South Korea</h3></span>
                                  """, class_name='mapText')
              ).add_to(mapObj)
map_js_var = mapObj.get_name()
mapObj.get_root().html.add_child(folium.Element(
    """
    <style>
    .mapText{
        color:blue;
        font-size:large;
        white-space:nowrap;
    }
    </style>
    <script type='text/javascript'>
    window.onload=function(){
    var  sizeFromZoom=function(z){return (0.5*z)+"em"}
    {mapObj}.on('zoomend',function(){
        var mapZoom={mapObj}.getZoom();
        var txtSize=sizeFromZoom(mapZoom);
        $('.mapText').css('font-size',txtSize);
        });}
    </script>
    """.replace("{mapObj}", map_js_var)
))
mapObj.save('map.html')
