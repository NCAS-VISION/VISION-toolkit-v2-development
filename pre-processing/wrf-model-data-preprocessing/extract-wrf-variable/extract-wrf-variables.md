# Extract WRF variables. 
This script will take a standard WRF output file and extract the user defined variables. 
It will then write create a new netcdf 4 file with level 1 compression. 

The script makes use of ncks, which is part of the [NetCDF operators (NCOs)](https://nco.sourceforge.net/) software for file manipulation and simple calculations. This software can be installed with conda. 

## Setting up the environment
Included in the folder is an environment file which contains all the dependencies for both NCO and CF-python these tools are 

```python
conda env create --name envname --file=environments.yml
```
## Running the code
To run the code you can simply specify which [WRF variable](http://rccdp.unl.edu/portal/WRF_Variable_Table.pdf) you require in your    sub-setted file.
The script will find any wrf out files in the current working directory and subset them with the selected variables and create new netcdf files in the form Areduced_wrfout_d01_2024-06-06_19:00:00

```python
python extract-wrf-variables.py VAR1 VAR2


