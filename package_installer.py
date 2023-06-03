# -*- coding: utf-8 -*-
"""
Created on Sat May 27 17:54:41 2023

@author: HP
"""
import subprocess

# List of packages to install or upgrade
required_packages = ['numpy', 'pandas', 'statsmodels','yfinance']

# Iterate over the packages and install or upgrade them
for package in required_packages:
    if package=='numpy':
        package_name=package
        package_version=1.18
        command = ['pip', 'install', f'{package_name}=={package_version}']
        subprocess.run(command, check=True)
    else:
        subprocess.run(['pip', 'install', '--upgrade', package], check=True)

        
 

