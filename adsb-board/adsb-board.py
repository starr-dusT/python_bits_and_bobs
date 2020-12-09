from opensky_api import OpenSkyApi
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# initalize apis
opn_sky = OpenSkyApi()

# constant variables
map = Image.open('map_lrg.png')

# geographical bounding box
#bnd_box=(34.5256, 35.8901, -119.8212, -117.448)
bnd_box=(34.8178, 36.7373, -122.0107, -117.5129)
#-122.0107,34.8178,-117.5129,36.7373
# number of "pixels" for representation
sz_x = 24
sz_y = 8

# cities
cit_x = [10, 21, 22, 25, 17]
cit_y = [11, 2, 1, 5, 8]

fig, ax = plt.subplots()
ax.set_xlim(-1, sz_x+1)
ax.set_ylim(-1, sz_y+1)

xp = []
yp = []
for x in range(sz_x):
    for y in range(sz_y):
        xp.append(x)
        yp.append(y)

while(1):
    pln_df = pd.DataFrame(columns=['calsn','lat', 'long', 'head', 'vel'])
    sts = opn_sky.get_states(bbox=bnd_box)
    if sts is None:
        plt.pause(20)
        print('continue')
        continue
    for st in sts.states:
        st_row = {'calsn':st.callsign, 'lat':st.latitude, 'long':st.longitude, 'head':st.heading, 'vel':st.velocity}
        pln_df = pln_df.append(st_row, ignore_index=True) 
    pln_df = pln_df[pln_df.calsn != ''].reset_index(drop=True)
    pln_df.reindex()
    grid_x = ((pln_df['long']-bnd_box[2])/(bnd_box[3]-bnd_box[2]))*sz_x
    grid_y = ((pln_df['lat']-bnd_box[0])/(bnd_box[1]-bnd_box[0]))*sz_y
    grid_x = grid_x.astype(int)
    grid_y = grid_y.astype(int)

    ax.clear()
    #ax.imshow(map, extent=(0,sz_x,0,sz_y), aspect='equal')
    ax.scatter(grid_x, grid_y, zorder=1, color='blue')
    ax.scatter(xp, yp, zorder=1, color='black', alpha=0.25)
    #ax.scatter(cit_x, cit_y, zorder=1, color='red')
    #for i, ann in enumerate(pln_df['calsn']):
        #ax.annotate(ann, (grid_x[i]+0.15, grid_y[i]+0.15))
    ax.set_aspect(abs((bnd_box[1]-bnd_box[0])/(bnd_box[3]-bnd_box[2])))
    ax.set_title('grid of plane locations')
    plt.pause(20)
