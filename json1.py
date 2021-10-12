from plotly import offline
from plotly.graph_objs import Scattergeo, Layout
import json

infile = open('eq_data_30_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

list_of_eqs = eq_data['features']

mags = []
lons = []
lats = []

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:5])
print(lons[:5])
print(lats[:5])


data = [Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title='Global Earthquake 1 Day')

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='globalearthquake1day.html')
