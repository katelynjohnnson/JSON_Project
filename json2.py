from plotly import offline
from plotly.graph_objs import Scattergeo, Layout
import json

infile = open('eq_data_30_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

list_of_eqs = eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    title = eq['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

print(mags[:5])
print(lons[:5])
print(lats[:5])


#data = [Scattergeo(lon=lons, lat=lats)]

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*m for m in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title': 'Magnitude'}
    }
}]

my_layout = Layout(title='Global Earthquake 1 Day')

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='globalearthquake1day.html')
