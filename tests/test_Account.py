# -*- coding: utf-8 -*-
"""
@author: Uwe Ziegenhagen
"""

import pytest
from Account import Account

def test_set_currency():
    a = Account()
    a.currency = 'EUR'
    assert a.currency == 'EUR'