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

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

infile = open('univ.json', 'r')
outfile = open('readable_univ_data.json', 'w')

univ_data = json.load(infile)

json.dump(univ_data, outfile, indent = 4)

women_grad_rate, aa_enroll, instate_price, hover_texts = [],[],[],[]

lons, lats, sizes = [],[],[]

for school in univ_data:
    if school["NCAA"]["NAIA conference number football (IC2020)"] in [102, 107,108, 127, 130]:
        lon = school["Longitude location of institution (HD2020)"]
        lat = school["Latitude location of institution (HD2020)"]
        size = school["Total  enrollment (DRVEF2020)"]
        grad_rate = school["Graduation rate  women (DRVGR2020)"]
        if grad_rate > 50:
            women_grad_rate.append(grad_rate)
        title = [school["instnm"], grad_rate]
        #enroll = school["Percent of total enrollment that are Black or African American (DRVEF2020)"]
        #price = school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]
        lons.append(lon)
        lats.append(lat)
        sizes.append(size)
        hover_texts.append(title)
        #if enroll > 10:    
           # aa_enroll.append(enroll)
        #if price > 50000:
            #instate_price.append(price)
        
        
print(women_grad_rate[:10])
#print(aa_enroll[:10])
#print(instate_price[:10])
print(hover_texts[:10])


#Map 1
data = [{'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : [hover_texts,grad_rate],
    'marker' : {
        'size' : [.0002 * size for size in sizes],
        'color' : sizes,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title' :'Graduation Rate'}},
    },]

my_layout = Layout(title='Power 5 Conference Graduation rate for Women')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='women_grad_rate.html')

women_grad_rate, aa_enroll, instate_price, hover_texts = [],[],[],[]

lons, lats, sizes = [],[],[]

for school in univ_data:
    if school["NCAA"]["NAIA conference number football (IC2020)"] in [102, 107,108, 127, 130]:
        lon = school["Longitude location of institution (HD2020)"]
        lat = school["Latitude location of institution (HD2020)"]
        size = school["Total  enrollment (DRVEF2020)"]
        enroll = school["Percent of total enrollment that are Black or African American (DRVEF2020)"]
        if enroll > 10:    
            aa_enroll.append(enroll)
        title = [school["instnm"], enroll]
        lons.append(lon)
        lats.append(lat)
        sizes.append(size)
        hover_texts.append(title)

print(aa_enroll[:10])
print(hover_texts[:10])

#Map 2
data = [{'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_texts,
    'marker' : {
        'size' : [.0002 * size for size in sizes],
        'color' : sizes,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title' : 'Enrollment Rate'}}
    },]
    

my_layout = Layout(title='Power 5 Conference Enrollment Rate for African Americans')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='enrollment_rate.html')

'''
women_grad_rate, aa_enroll, instate_price, hover_texts = [],[],[],[]

lons, lats, sizes = [],[],[]

for school in univ_data:
    if school["NCAA"]["NAIA conference number football (IC2020)"] in [102, 107,108, 127, 130]:
        lon = school["Longitude location of institution (HD2020)"]
        lat = school["Latitude location of institution (HD2020)"]
        size = school["Total  enrollment (DRVEF2020)"]
        price = school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]
        title = school["instnm"] & price
        lons.append(lon)
        lats.append(lat)
        sizes.append(size)
        hover_texts.append(title)
        if price > 50000:
            instate_price.append(price)

print(price[:10])
print(hover_texts[:10])



#Map 3
data = [{'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_texts,
    'marker' : {
        'size' : [.0002 * size for size in sizes],
        'color' : sizes,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title' : 'Total In-state Price'}}
    },]
    

my_layout = Layout(title='Power 5 Conference In-state Price For Students Living Off Campus')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='total_price.html')
'''