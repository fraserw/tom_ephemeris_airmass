import numpy as np
import json

def get_eph_scheme_data(target, data):
    
    eph_json = json.loads(target.eph_json)
    site = list(eph_json.keys())[0]
    eph_json_single = eph_json[site]
    mjd, ra, dec = [], [] , []

    for i in range(0, len(eph_json_single)):
        mjd.append(eph_json_single[i]['t'])
        ra.append(eph_json_single[i]['R'])
        dec.append(eph_json_single[i]['D'])
    mjd, ra, dec = np.array(mjd, dtype='float64'), np.array(ra, dtype='float64'), np.array(dec, dtype='float64')
    step = max(1, int(10.0/(mjd[1]-mjd[0])))
    l = len(ra[::step])
    data.append(
        dict(
            lon=ra[::step] if l>1 else ra,
            lat=dec[::step] if l>1 else dec,
            text=target.name,
            hoverinfo='text',
            mode='lines',
            type='scattergeo'
        ))

    return data
