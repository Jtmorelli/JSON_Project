"""
Process the JSON file named univ.json. Create 3 maps per instructions below.
The size of the point on the map should be based on the size of total enrollment. Display only those schools 
that are part of the 
ACC, Big 12, Big Ten, Pac-12 and SEC divisons 
(refer to valueLabels.csv file)
The school name and the specific map criteria should be displayed when you hover over it.
(For example for Map 1, when you hover over Baylor, it should display "Baylor University, 81%")
Choose appropriate tiles for each map.


Map 1) Graduation rate for Women is over 50%
Map 2) Percent of total enrollment that are Black or African American over 10%
Map 3) Total price for in-state students living off campus over $50,000

"""

import json


infile = open("univ.json", "r")
outfile = open("readable_univ.json", "w")


univ_data = json.load(infile)

json.dump(univ_data, outfile, indent=4)

list_of_univ = univ_data

div = [102, 108, 107, 127, 130]
m1schools = []
m2schools = []
m3schools = []


lons, lats, tot_e, hover_texts, m1, m2, m3 = [], [], [], [], [], [], []

########################### MAP 1 ##############################################

for school in list_of_univ:
    percent = int(
        0
        if school["Graduation rate  women (DRVGR2020)"] is None
        else school["Graduation rate  women (DRVGR2020)"]
    )
    if (school["NCAA"]["NAIA conference number football (IC2020)"] in div) and (
        percent >= 50
    ):
        m1schools.append(school)


for univ in m1schools:
    tote = univ["Total  enrollment (DRVEF2020)"]
    wom = univ["Graduation rate  women (DRVGR2020)"]
    lon = univ["Longitude location of institution (HD2020)"]
    lat = univ["Latitude location of institution (HD2020)"]
    title = univ["instnm"]
    lons.append(lon)
    lats.append(lat)
    tot_e.append(tote)
    m1.append(wom)
    hover_texts.append(title)


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_texts,
        "marker": {
            "size": [tote / 2500 for tote in tot_e],
            "color": tot_e,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]

my_layout = Layout(title="Schools where Graduation rate for Women is over 50%")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="map1.html")

#####################################################################################

########################### MAP 2 ##############################################

for school in list_of_univ:
    percent = int(
        0
        if school[
            "Percent of total enrollment that are Black or African American (DRVEF2020)"
        ]
        is None
        else school[
            "Percent of total enrollment that are Black or African American (DRVEF2020)"
        ]
    )
    if (school["NCAA"]["NAIA conference number football (IC2020)"] in div) and (
        percent > 10
    ):
        m2schools.append(school)


for univ in m2schools:
    tote = univ["Total  enrollment (DRVEF2020)"]
    m_2 = univ[
        "Percent of total enrollment that are Black or African American (DRVEF2020)"
    ]
    lon = univ["Longitude location of institution (HD2020)"]
    lat = univ["Latitude location of institution (HD2020)"]
    title = univ["instnm"]
    lons.append(lon)
    lats.append(lat)
    tot_e.append(tote)
    m2.append(m_2)
    hover_texts.append(title)


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_texts,
        "marker": {
            "size": [tote / 2500 for tote in tot_e],
            "color": tot_e,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]

my_layout = Layout(
    title="Schools where Percent of total enrollment that are Black or African American is over 10%"
)

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="map2.html")

#####################################################################################

########################### MAP 3 ##############################################

for school in list_of_univ:
    amount = int(
        0
        if school[
            "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"
        ]
        is None
        else school[
            "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"
        ]
    )
    if (school["NCAA"]["NAIA conference number football (IC2020)"] in div) and (
        amount >= 50000
    ):
        m3schools.append(school)


for univ in m3schools:
    tote = univ["Total  enrollment (DRVEF2020)"]
    m_3 = univ[
        "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"
    ]
    lon = univ["Longitude location of institution (HD2020)"]
    lat = univ["Latitude location of institution (HD2020)"]
    title = univ["instnm"]
    lons.append(lon)
    lats.append(lat)
    tot_e.append(tote)
    m3.append(m_3)
    hover_texts.append(title)


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_texts,
        "marker": {
            "size": [tote / 2500 for tote in tot_e],
            "color": tot_e,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]

my_layout = Layout(
    title="Schools where Total price for in-state students living off campus over $50,000"
)

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="map3.html")

#####################################################################################
