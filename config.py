# -*- coding: utf-8 -*-
"""
Created on Mon May 15 00:46:30 2023

@author: HP
"""
import numpy as np
import pandas as pd


nifty_world={'Capital Goods': ['APLAPOLLO',
  'ADANIENT',
  'HINDALCO',
  'HINDCOPPER',
  'HINDZINC',
  'JSWSTEEL',
  'JSL',
  'JINDALSTEL',
  'MOIL',
  'NATIONALUM',
  'RATNAMANI',
  'SAIL',
  'TATASTEEL',
  'VEDL',
  'WELCORP'],
 'Financial Services': ['AXISBANK',
  'BANDHANBNK',
  'CUB',
  'FEDERALBNK',
  'HDFCBANK',
  'ICICIBANK',
  'IDFCFIRSTB',
  'INDUSINDBK',
  'KOTAKBANK',
  'RBLBANK'],
 'Fast Moving Consumer Goods': ['BRITANNIA',
  'COLPAL',
  'DABUR',
  'EMAMILTD',
  'GODREJCP',
  'HINDUNILVR',
  'ITC',
  'MARICO',
  'NESTLEIND',
  'PGHH',
  'RADICO',
  'TATACONSUM',
  'UBL',
  'MCDOWELL-N',
  'VBL'],
 'Healthcare': ['ABBOTINDIA',
  'ALKEM',
  'AUROPHARMA',
  'BIOCON',
  'CIPLA',
  'DIVISLAB',
  'DRREDDY',
  'GLAND',
  'GLAXO',
  'GLENMARK',
  'GRANULES',
  'IPCALAB',
  'LAURUSLABS',
  'LUPIN',
  'NATCOPHARM',
  'PFIZER',
  'SANOFI',
  'SUNPHARMA',
  'TORNTPHARM',
  'ZYDUSLIFE'],
 'Information Technology': ['COFORGE',
  'HCLTECH',
  'INFY',
  'LTTS',
  'LTIM',
  'MPHASIS',
  'PERSISTENT',
  'TCS',
  'TECHM',
  'WIPRO'],
 'Media Entertainment & Publication': ['DISHTV',
  'HATHWAY',
  'NDTV',
  'NAVNETEDUL',
  'NAZARA',
  'NETWORK18',
  'PVR',
  'SUNTV',
  'TV18BRDCST',
  'ZEEL'],
 'Oil Gas & Consumable Fuels': ['ATGL',
  'AEGISCHEM',
  'BPCL',
  'CASTROLIND',
  'GAIL',
  'GUJGASLTD',
  'GSPL',
  'HINDPETRO',
  'IOC',
  'IGL',
  'MGL',
  'ONGC',
  'OIL',
  'PETRONET',
  'RELIANCE']}

sector=['Capital Goods', 'Financial Services', 'Fast Moving Consumer Goods', 
        'Healthcare', 'Information Technology', 'Media Entertainment & Publication', 
        'Oil Gas & Consumable Fuels']


