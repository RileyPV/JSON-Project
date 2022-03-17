import json

infile = open('eq_data_1_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')


eq_data = json.load(infile)

json.dump(eq_data, outfile, indent = 4)


list_of_eqs = eq_data["features"]

mags, lons, lats, hover_texts = [], [], [], []

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    title = eq["properties"]["title"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

print(mags[:10])
print(lons[:10])
print(lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#List comprehension
#new_mags = [mag * 5 for mag in mags if mag > 3]

data = [{'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_texts,
    'marker' : {
        'size' : [5 * mags for mag in mags if mag > 3],
        'color' : mags,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title' : 'Magnitude'}}
    },]
    #Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title='Global Earthquakes')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='global_earthquakes.html')


#print(len(list_of_eqs))