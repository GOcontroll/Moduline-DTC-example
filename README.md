# Moduline DTC

This script translates fault codes from /usr/mem-diag into readable information for the Moduline-WebUI application.  
It expects a linux environment, if using Windows look into WSL to develop this.  
It should be workable on a MacOS system

## Building

Install the necessary python dependencies, python itself, python pip and python venv

navigate to this folder in the shell, then run:  
`python3 -m venv .venv` #Create the venv  
`source .venv/bin/activate` #Enter the venv  

then run:  
`pip install --editable .`

at this point you can run:  
`go-print-dtcs`  
to get the output of the get_errors() function  
you can put some dummy dtcs in /usr/mem-diag like `16844753` and `17893329`

to build the distributable:  
`python3 setup.py sdist`