# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:57:27 2020

@author: Uwe
"""


from PyQifParser import PyQifParser

P = PyQifParser(r'C:\Users\Uwe\Nextcloud\QIF-Parser\Quicken_h.QIF')
P.parse()
P.to_excel('r:/export.xlsx')