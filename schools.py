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

power_five_schools = []

for school in univ_data:
    if univ_data["NAIA conference number football (IC2020)"] == 102 or 107 or 108 or 127 or 130:
        power_five_schools.append(school)
        


women_grad_rate, aa_enroll, instate_price = [],[],[]


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


