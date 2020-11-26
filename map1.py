import folium
import pandas 

def color_producer(elevation):
    if elevation <1000:
        return 'green'
    elif 1000<= elevation <3000:
        return 'black' 
    else:
        return 'pink'      

data=pandas.read_csv("volcano.txt")

map=folium.Map(location=[38.58,-99.09], zoom_start=6)

lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

fg=folium.FeatureGroup(name="My Map")

for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup=str(el)+" m", icon=folium.Icon(color_producer(el))))

map.add_child(fg)
map.save("Map1.html")