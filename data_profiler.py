# -*- coding: utf-8 -*-
"""
Created on Mon May 15 02:30:00 2023

@author: arghya.ghosh
"""

import numpy as np
from stock_data_loader import nifty_data_loader
from statsmodels.tsa.ar_model import ar_select_order




class data_profiling(nifty_data_loader):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.data=self.getData()
        self.lag=kwargs['lag']
       
        
        
        
    def _valuation_flag(self):
        '''
        
        Check whether the stock is overvalued or undervalued
        Returns
        -------
        string

        '''
        
        raise NotImplementedError("Not Implemented Yet")
        
    def _buy_sell_indicator(self):
        '''
        Checks whether we should buy the stock or sell the stock

        Returns
        -------
        dictionary

        '''
        raise NotImplementedError("Not Implemented Yet")
        
        
        
    def _statement_ratios(self):
        '''
        Fetches statement ratios

        Returns
        -------
        dict

        '''
        
        raise NotImplementedError("Not Implemented Yet")
        
    def _lag_correlation_variables(self):
        '''
        Finds which lag orders are significant

        Returns
        -------
        dict

        '''
        log_return= np.log(self.data['Close'] /self.data['Close'].shift(1))
        search = ar_select_order(endog=log_return, maxlag=self.lag)
        print(search)
        return search.ar_lags


        
        
        
    
