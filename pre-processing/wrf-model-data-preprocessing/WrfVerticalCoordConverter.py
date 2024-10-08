from wrf import getvar, extract_vars
import cf
import xarray as xr
from netCDF4 import Dataset



class WrfVerticalCoordConverter:

    def __init__(self, wrfouts):
        # single or list of wrfouts (netcdf4 self.wrfouts)
        self.wrfouts = wrfouts 
        self._get_blank_field()

    def _get_blank_field(self):
        """
            Generates a blank cf field that has the atmospheric hybrid
            sigma pressure coordinate and all required constructs
        """

        # Load all necessary WRF data for coordinates including a 3d field
        # that we will use as the template of the blank field

        # Surface pressure p_s
        PSFC = extract_vars(self.wrfouts, varnames='PSFC', timeidx=None)['PSFC'][:]/100
        # Pressure at top of model domain p_t
        PT = extract_vars(self.wrfouts, varnames='P_TOP', timeidx=None)['P_TOP']/100
        # B, function of eta coord (znu) from WRF coords,
        # substitutes directly for B function in 'atmosphere hybrid sigma 
        # pressure coordinate'
        B = extract_vars(self.wrfouts, varnames='C3H', timeidx=None)['C3H'][:]
        # Eta, vertical coord
        ZNU = extract_vars(self.wrfouts, varnames='ZNU', timeidx=None)['ZNU'][:]
        # Horizontal coords
        XLAT= extract_vars(self.wrfouts, varnames='XLAT', timeidx=None)['XLAT']
        XLONG = extract_vars(self.wrfouts, varnames='XLONG', timeidx=None)['XLONG']
        # Reference sea level pressure p_0
        P0 = 1013.25
        # A, function of eta (znu), derived for AHSP coords
        A = (ZNU - B + (1 - ZNU) * (PT/P0))
        # T, 3d temp to derive dims
        T = extract_vars(datasets, varnames='T', timeidx=None)['T']

        ds = xr.Dataset()
        ds['A'] = A[0]
        ds['B'] = B[0]
        ds['B'].attrs = {}
        ds['ps'] = PSFC
        ds['p0'] = P0
        ds['ZNU'] = ZNU
        ds['ZNU'].attrs = {}
        ds['XLAT'] = XLAT
        ds['XLAT'].attrs = {}
        ds['XLONG'] = XLONG
        ds['XLONG'].attrs = {}
        ds['T'] = T
        ds['T'].attrs = {}
        # Add random string for name
        ds.to_netcdf('wrf-sigma-temp.nc')

        

        # Carry out cf methods to produce the field with coordinates

        file = cf.read('wrf-sigma-temp.nc')
        
        # Take out the fields of relevance
        a = file[0]
        b = file[1]
        f = file[2]
        z = file[3]
        p0 = file[4]
        ps = file[5]
        f.del_data()
        
        # 1. Set up the domain ancils
        a_da = cf.DomainAncillary(source=a)
        b_da = cf.DomainAncillary(source=b)
        p0_da = cf.DomainAncillary(source=p0)
        ps_da = cf.DomainAncillary(source=ps)
        
        # 2. Add these as constructs to t, our main field
        key_f_a = f.set_construct(a_da)
        key_f_b = f.set_construct(b_da)
        key_f_p0 = f.set_construct(p0_da)
        key_f_ps = f.set_construct(ps_da)
        #print("\n\nAfter domain ancil setting, f is:", f)
        
        # 3. Create the coordinate reference
        c = cf.CoordinateReference()
        # Set the standard name which we get from App. D of the CF Conventions doc
        c.coordinate_conversion.set_parameter(
               "standard_name", "atmosphere_hybrid_sigma_pressure_coordinate")
        # Get the computed standard name from App D. section 'formula terms'
        c.coordinate_conversion.set_parameter(
               "computed_standard_name", "air_pressure")
        # Get the variables from the 'formula terms' equation and match them to
        # the keys from the set_construct() call above.
        dom_ancils = {
               "a": key_f_a,
               "b": key_f_b,
               "p0": key_f_p0,
               "ps": key_f_ps,
               }
        c.coordinate_conversion.set_domain_ancillaries(dom_ancils)
        #print("\n\nCoordinate reference about to add is:")
        #c.dump()
        # All ready to add!
        
        # 4. Add the coordinate reference to the field t
        c_key = f.set_construct(c)
        #print("\n\nField f after coordinate reference setting is:", f)
        
        # 5. There is some unit processing to do, since we can't yet do the computation
        # of t.compute_vertical_coordinates() which ultimately needs to work
        # Do the unit addition required:
        # No units on the domain ancils - pulled in from wrf-python - should
        # find a way to get those in via the script
        p0 = f.construct("ncvar%p0")
        ps = f.construct("ncvar%ps")
        p0.override_units("hPa", inplace=True)
        ps.override_units("hPa", inplace=True)
        #print("\n\nField after unit processing is:", f)
        # Units now added as desired
        
        # 6. Now the call to compute_vertical_coordinates should work!
        f1 = f.compute_vertical_coordinates()
        #print("\n\nComputing of vertical coordinates worked, giving:", f1)
        # Note there is now an 'air_pressure' aux coord! We have done it!
        
        # Note we should only write out the field without the computed vert coord
        # since that will double the size of the data. Calculate when need, don't save
        # e.g. we will calculate it at the start of the VISION script.
        
        # 7. Finally, we need to deal with the z coordinate which is presently
        #    just a separate field
        #print("\n\nVertical coordinates from original field z are:", z)
        #print("\n\nWith array of:", z.array)
        
        # Note these are all the same across the times, so take just the first
        z0 = z[0].squeeze()
        # Create a dimension coordinate of this
        d = cf.DimensionCoordinate(source=z0)
        d.set_property("standard_name", "atmosphere_hybrid_sigma_pressure_coordinate")
        d.set_property("computed_standard_name", "air_pressure")
        #print("\n\nAdding a dimension coordinate of the squeezed first z element:")
        #d.dump()
        
        # Now set this on f, to incorporate the z into f as a dim. coord.
        d_key = f.set_construct(d)
        # Now added!
        #print("\n\nAdded dimension coord. to f:", f)
        
        # 8. Also need to add it to the coordinate reference as its coordinate
        c = f.construct(c_key)
        c.set_coordinate(d_key)
        g = cf.aggregate(f)
        blank_field = g[0]
        blank_field.nc_set_variable('BLANK')
        self.blank_field = blank_field

    def get_blank_field(self):
        return self.blank_field

    def getvar(self, varname):
        """
        Wrapper for wrf-python getvar and extract_vars routines
        returns variable in cf field with atmospheric hybrid
        sigma pressure coordinate
        """
        try:
            data = getvar(self.wrfouts, varname, timeidx=None)
        except ValueError:
            print('val error')
            data = extract_vars(self.wrfouts, varnames=varname, timeidx=None)[varname]
        except:
            exit()
        field = self.blank_field.copy()
        field.nc_set_variable(varname)
        field.set_data(data[:])
        return field 
        
if __name__ == "__main__":
    import glob
    paths = glob.glob('../wrfout_d03_2023-07-12_0*')
    datasets = [Dataset(file) for file in paths]
    converter = WrfVerticalCoordConverter(datasets)
    var = converter.getvar('QVAPOR')
    var.dump()
