# -*- coding: utf-8 -*-
"""
Created on Mon May 15 00:30:46 2023

@author: arghya.ghosh
"""


'''
import subprocess
# Define the command to run the script
command = ['python', 'package_installer.py']
# Run the command to execute the script
subprocess.run(command, check=True)
'''



import yfinance as yf
import numpy as np
import pandas as pd
import config as cf



class nifty_data_loader():
    def __init__(self,**kwargs):
        self.start_date=kwargs['start_date']
        self.end_date=kwargs['end_date']
        self.stock_name=kwargs['stock_name']
        self._date_check()
        self._stock_match_check()
        
        
    
        
    def _date_check(self):
        if self.start_date > self.end_date:
            raise ValueError(f"Start Date cannot be greater than Enddate")
        
    def _stock_match_check(self):
        all_stock=cf.nifty_world
        sectors=cf.sector
        exist_flag=[(self.stock_name in all_stock[sector]) for sector in sectors]
        if sum(exist_flag)==0:
            raise KeyError(f"There is no such stock available. Please enter a proper ticker.")
            
    def getData(self):
        yahooticker=self.stock_name+'.NS'
        data = yf.download(yahooticker, start=self.start_date, end=self.end_date)
        return data

        

            
            
        
        
        
        
