# fits-emulator
Emulate observations of seeing-limited point sources recorded in FITS files


# Resources
https://homepage.physics.uiowa.edu/~pkaaret/2018s_a4850/Lab02_noise.html

# Environment Setup
python3 -m virtualenv venv  
created virtual environment CPython3.9.6.final.0-64 in 386ms
  creator CPython3macOsFramework(dest=/Users/proutyr1/Documents/git/fits-emulator/venv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/proutyr1/Library/Application Support/virtualenv)
    added seed packages: pip==24.0, setuptools==69.1.0, wheel==0.42.0
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
[proutyr1@/Users/proutyr1/Documents/git/fits-emulator]
source ./venv/bin/activate
(venv) [proutyr1@/Users/proutyr1/Documents/git/fits-emulator]
pip list
Package    Version
---------- -------
pip        24.0
setuptools 69.1.0
wheel      0.42.0
(venv) [proutyr1@/Users/proutyr1/Documents/git/fits-emulator]

pip3 install numpy matplotlib astropy scipy argparse
pip list          
Package             Version
------------------- -------------------
astropy             6.0.0
astropy-iers-data   0.2024.2.26.0.28.55
contourpy           1.2.0
cycler              0.12.1
fonttools           4.49.0
importlib_resources 6.1.2
kiwisolver          1.4.5
matplotlib          3.8.3
numpy               1.26.4
packaging           23.2
pillow              10.2.0
pip                 24.0
pyerfa              2.0.1.1
pyparsing           3.1.1
python-dateutil     2.9.0.post0
PyYAML              6.0.1
scipy               1.12.0
setuptools          69.1.0
six                 1.16.0
wheel               0.42.0
zipp                3.17.0