import folium
import pandas as pd

def colordefiner(ele):
    if ele<=1000:
        return 'green'
    elif ele >1000 and ele<=2500:
        return 'blue'
    else:
        return 'red'

data=pd.read_csv("Volcanoes.txt")
lat=list(data['LAT'])
lon=list(data['LON'])
name=list(data['NAME'])
elevation=list(data['ELEV'])

map=folium.Map(location=[38,-98],zoom_start=3,tiles="Stamen Terrain")

fgv=folium.FeatureGroup(name="Volcanoes in USA")

for i,j,k,el in zip(lat,lon,name,elevation):
    fgv.add_child(folium.Marker(location=[i,j],popup=k,icon=folium.Icon(color=colordefiner(el))))

fgp=folium.FeatureGroup(name="Population Color")

da=open('world.json','r',encoding='utf-8-sig').read()

fgp.add_child(folium.GeoJson(data=da,
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl(position='bottomright'))
map.save("MAP1.html")