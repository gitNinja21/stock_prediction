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
        pip install numpy==1.8.0
    else:
        subprocess.run(['pip', 'install', '--upgrade', package], check=True)
