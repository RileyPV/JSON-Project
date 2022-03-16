"""
Process the JSON file named univ.json. Create 3 maps per instructions below.
The size of the point on the map should be based on the size of total enrollment. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons (refer to valueLabels.csv file)
The school name and the specific map criteria should be displayed when you hover over it.
(For example for Map 1, when you hover over Baylor, it should display "Baylor University, 81%")
Choose appropriate tiles for each map.


Map 1) Graduation rate for Women is over 50%
Map 2) Percent of total enrollment that are Black or African American over 10%
Map 3) Total price for in-state students living off campus over $50,000

"""

import json

infile = open('univ.json', 'r')
outfile = open('readable_univ_data.json', 'w')


univ_data = json.load(infile)

json.dump(univ_data, outfile, indent = 4)

power_five_schools = {}

#inst_name = []

women_grad_rate, aa_enroll, instate_price, hover_texts = [],[],[],[]

for school in univ_data:
    if school["NCAA"]["NAIA conference number football (IC2020)"] == 102 or 107 or 108 or 127 or 130:
        title = school["instnm"]
        grad_rate = school["Graduation rate  women (DRVGR2020)"]
        enroll = school["Percent of total enrollment that are Black or African American (DRVEF2020)"]
        price = school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]
        women_grad_rate.append(grad_rate)
        aa_enroll.append(enroll)
        instate_price.append(price)
        hover_texts.append(title)
        
print(women_grad_rate[:10])
print(aa_enroll[:10])
print(instate_price[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Map 1
#data = [{'type' : 'Scattergeo',
 #   'lon' : lons,
  #  'lat' : lats,
   # 'text' : hover_texts,
    #'marker' : {
     #   'size' : [5 * mags for mag in mags if mag > 3],
      #  'color' : mags,
       # 'colorscale' : 'Viridis',
        #'reversescale' : True,
        #'colorbar' : {'title' : 'Magnitude'}}
    #},]
    

#my_layout = Layout(title='Global Earthquakes')

#fig = {'data':data, 'layout':my_layout}

#offline.plot(fig,filename='global_earthquakes.html')

#Map 2
#data = [{'type' : 'Scattergeo',
 #   'lon' : lons,
  #  'lat' : lats,
   # 'text' : hover_texts,
   # 'marker' : {
   #     'size' : [5 * mags for mag in mags if mag > 3],
    #    'color' : mags,
     #   'colorscale' : 'Viridis',
      #  'reversescale' : True,
       # 'colorbar' : {'title' : 'Magnitude'}}
    #},]
    

#my_layout = Layout(title='Global Earthquakes')

#fig = {'data':data, 'layout':my_layout}

#offline.plot(fig,filename='global_earthquakes.html')

#Map 3
#data = [{'type' : 'Scattergeo',
 #   'lon' : lons,
  #  'lat' : lats,
   # 'text' : hover_texts,
   # 'marker' : {
    #    'size' : [5 * mags for mag in mags if mag > 3],
     #   'color' : mags,
      #  'colorscale' : 'Viridis',
       # 'reversescale' : True,
       # 'colorbar' : {'title' : 'Magnitude'}}
   # },]
    

#my_layout = Layout(title='Global Earthquakes')

#fig = {'data':data, 'layout':my_layout}

#offline.plot(fig,filename='global_earthquakes.html')
