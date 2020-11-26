import folium
import pandas 

data=pandas.read_csv("volcano.txt")
def color_producer(elevation):
    if elevation <1000:
        return 'green'
    elif 1000<= elevation <3000:
        return 'yellow' 
    else:
        return 'red' 

lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])           

map=folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")


fgv=folium.FeatureGroup(name="volcano")

for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el)+" m", fill_color=color_producer(el), color='grey', fill_opacity=0.7))

fgp=folium.FeatureGroup(name="population")

fgp.add_child(folium.GeoJson(data=open('world.json','r' ,encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x ['properties']['POP2005'] <10000000 else 'purple' 
if 1000000 <=x ['properties']['POP2005'] <2000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map2.html")