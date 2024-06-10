import sys
import os
import subprocess

def main():
    # Check if at least one argument is provided
    if len(sys.argv) == 1:
        print("No WRF variables provided. Please enter at least one WRF variable.")
        print("usage: reduce.py VAR1 VAR2 VAR3 ...")
        sys.exit(1)
    
    # Get the WRF variables from the command line arguments
    wrf_variables = sys.argv[1:]
    
    # List all files starting with 'wrfout'
    wrf_files = [f for f in os.listdir('.') if f.startswith('wrfout')]
    
    for wrf_file in wrf_files:
        # Prepare the ncks command
        command = ['ncks', '-7', '-L', '1', '-v', 'XLAT,XLONG,P,PH,PHB,Times,' + ','.join(wrf_variables), wrf_file, f'Areduced_{wrf_file}']
        
        # Execute the ncks command
        subprocess.run(command)

if __name__ == "__main__":
    main()
