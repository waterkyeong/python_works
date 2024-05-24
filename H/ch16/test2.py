from pathlib import Path
import json

import plotly.express as px

# path = Path('H/ch16/earthquake_data/significant_month.geojson')
path = Path('H/ch16/earthquake_data/all_month.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# path = Path('H/ch16/earthquake_data/readable_eq_data.geojson')
path = Path('H/ch16/earthquake_data/all_month.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats =[], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])
print(lons[:5])
print(lats[:5])

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, title=title, size=mags)
fig.show()
