config = {
    'latitude': 'latitude',
    'longitude': 'longitude',
    'sensingtime': 'sensingtime',
    'do_retrieval': 'do_retrieval',
    'sensingtime_msec': 'sensingtime_msec',
    'sensingtime_day': 'sensingtime_day',
    'sensingtime': 'sensingtime',
    'npres': 'npres',
    'npi': 'npi',
}
 
import cf

# Any old global model data - doesn't have to be this one! E.g. from Model_Input/
m = cf.read('tas_day_HadGEM3-GC31-MM_highresSST-future_r1i3p1f1_gn_20150101-20151230.nc')[0]

# /gws/pw/j07/rsg_share/public/projects/ims/data/lv2/output_ghg_cv9_v123_lam2_nat_nfo33_fgsnwp_nobc_newbc_rbc_ram4_rem20-ncam_rcl5_raer6st_rmg_oap_cnv2_ixam7-8_o3f110_swir2/metopa/2017/07/03/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_350_399-v1000.nc

l2 = cf.read('ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20170703201158z_20170703215054z_350_399-v1000.nc')


s0 = l2.select('air_temperature')[0]

# Remove the vertical axis
index = []
for i, key in enumerate(s.get_data_axes()):
    if s.domain_axis(key).nc_get_dimension() == config['npres']:
        index.append(slice(None))
        npres_position = i
    else:
        index.append(0)

if len(index) != s.ndim:
    raise ValueError()
        
s = s0[tuple(index)].squeeze()

# Satelite time
time_of_day =  l2.select_field(f"ncvar%{config['sensingtime_msec']}")
time_of_day.override_units('ms', inplace=True)
time_of_day.dtype = float

day = l2.select_field(f"ncvar%{config['sensingtime_day']}")
day.override_units('day since 2000-01-01', inplace=True)
day.dtype = float

time = day.copy()
time.data += time_of_day.data

time.clear_properties()
time.set_property('standard_name', 'time')

# Satelite latitude and longitude
lat = l2.select_field(f"ncvar%{config['latitude']}")
lon = l2.select_field(f"ncvar%{config['longitude']}")

# Check for spatial subsetting
if lat.size == s.size:
    do_retrival = l2.select_field('ncvar%do_retrieval')
    mask = do_retrival.data.where(1, None, cf.masked).mask.persist()

    for f in (time, lat, lon):    
        f.where(mask, cf.masked, inplace=True)
        data = f.del_data()
        data.compressed(inplace=True)
        if data.size != s.size:
            raise ValueError()
        
        f.domain_axis().set_size(s.size)
        f.set_data(data.compressed())

    del mask

# Create satelite "trajectory"
s.set_construct(cf.AuxiliaryCoordinate(source=lat))
s.set_construct(cf.AuxiliaryCoordinate(source=lon))
s.set_construct(cf.AuxiliaryCoordinate(source=time))
s.set_property('featureType', 'trajectory')

regridded = m.regrids(s, method='linear')

print(m)
print(s)
print(regridded)
