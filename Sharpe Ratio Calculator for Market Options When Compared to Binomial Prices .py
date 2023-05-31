import pandas as pd
import math
import mpmath
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime as dt
from datetime import date as date
from yahoo_fin import options as op
from yahoo_fin import stock_info as si
import yahoo_fin as yf
import yfinance as yaf


#####################################################################################################################################################################################
dict = {'time steps' : 13, 'risk-free rate': 0.05261, 'callput': -1, 'AmerEu': 1}

if dict['callput'] == 1:                                     # call = 1, put = -1; in callput
    option_type = 'calls'
elif dict['callput'] == -1:
    option_type = 'puts'
if dict['AmerEu'] > 0:                                      # American = 1, European = -1; in AmerEu
    exercise = 'American'
else:
    exercise = 'European'

#####################################################################################################################################################################################

# TICKER
ticker = 'nflx'                                             # not case sensitive

# EXPIRATION LIST
expiration = op.get_expiration_dates(ticker)
print('expiration dates are', expiration)

# EXPIRY DATE
date_of_exp = 'June 21, 2024'                               # keep in mind to format this properly, especially the months

todays = date.today()
expiry_date = date(2024, 6, 21)                             # formattted as (year, int(month), day)
time_between = expiry_date - todays

# CHAIN DATA
chaindata = op.get_options_chain(ticker)[option_type]

option_info = {}
opinfo = option_info
for daate in expiration:
    opinfo[daate] = chaindata

#####################################################################################################################################################################################
# RISK FREE RATE EXTRACTION
dict['risk-free rate'] = (si.get_live_price('TNX')) / 100

# DIVIDEND YIELD EXTRACTION
def div_yield():
    stockdiv = yaf.Ticker(ticker)
    try:
        divrate = stockdiv.info['dividendRate']
    except KeyError:
        divrate = 0
    return divrate

# STRIKES EXTRACTION
old_strike = opinfo[date_of_exp][['Strike']].values.tolist()
new_strikes= []
for x in old_strike:
    for item in x:
        new_strikes.append(int(item))

# VOLATILITY EXTRACTION
old_vol = opinfo[date_of_exp][['Implied Volatility']].values.tolist()
new_vol = []
for x in old_vol:
    for item in x:
        items = item.replace("%","").replace(",","")
        new_vol.append(float(items))

#####################################################################################################################################################################################
# PARAMETER SETTING
calculated_price = []
j = 0
while j < len(opinfo[date_of_exp][['Strike']]):
    dict['strike'] = new_strikes[j]
    dict['sigma'] = new_vol[j]/100
    dict['price'] = si.get_live_price(ticker)
    dict['years'] = time_between.days/365
    dict['dividend'] = div_yield()/100

    if new_vol[j] == 0:
        u = 1.0000001
    else:
        u = math.exp(dict['sigma']*math.sqrt(dict['years']/dict['time steps']))
    d = 1/u
    probup = (((math.exp((dict['risk-free rate']-dict['dividend'])*dict['years']/dict['time steps'])) - d) / (u - d))
    discount_factor = dict['risk-free rate']/dict['time steps']
    duration_of_time_step = (dict['years']/dict['time steps'])
##################################################################################################################################################################################### 
# BINOMIAL FUNCTION    
    def binomial():
        Tstep = dict['time steps']
        payoffs = []
        n = 0
        while n < (Tstep + 1): 
            payoffs.append(max(0, dict['callput']*(dict['price']*(u**((Tstep)-n))*(d**n) - dict['strike'])))
            n += 1
        
        while Tstep >= 1:
            discounting1 = []
            i = 0
            while i < (Tstep):
                if dict['AmerEu'] == 1:
                    American_payoff = (dict['callput']*(dict['price']*(u**(Tstep-i-1)*(d**i)) - dict['strike']))
                    European_payoff = (((probup)*payoffs[i]) + ((1-probup)*payoffs[i+1])) / (math.exp(discount_factor))
                    discounting1.append(max(American_payoff, European_payoff))
                elif dict['AmerEu'] == -1:
                    discounting1.append((((probup)*payoffs[i]) + ((1-probup)*payoffs[i+1]))
                                        / (math.exp(discount_factor)))
                else:
                    pass
                i += 1  
                
            payoffs.clear()
            payoffs.extend(discounting1)
            Tstep -= 1
        return discounting1
    if binomial()[0] < 0:
        calculated_price.append(0)
    else:
        calculated_price.append(binomial()[0])
    j += 1
#####################################################################################################################################################################################
# BID PRICES LIST
old_bid = opinfo[date_of_exp][['Bid']].values.tolist()                      
new_bid = []                            
for x in old_bid:
    for item in x:
        if item == '-':
            item = 0
        else:
            None
        new_bid.append(float(item))

# ASK PRICES LIST
old_ask = opinfo[date_of_exp][['Ask']].values.tolist()                       
new_ask= []
for x in old_ask:
    for item in x:
        if item == '-':
            item = 0
        else:
            None
        new_ask.append(float(item))

# OPEN INTEREST LIST
old_open_int = opinfo[date_of_exp][['Open Interest']].values.tolist()       
new_open_int = []
for x in old_open_int:
    for item in x:
        new_open_int.append(float(item))

#####################################################################################################################################################################################
# EXCESS RETURN
option_return = []
i = 0
while i < len(calculated_price):
    if calculated_price[i] < new_bid[i] or new_bid[i] == 0 or ((calculated_price[i]/new_bid[i]) - 1 - dict['risk-free rate']) < 0:
        option_return.append(0)
    elif calculated_price[i] > new_bid[i] and new_bid[i] != 0:
        option_return.append(((calculated_price[i]/new_bid[i]) - 1 - dict['risk-free rate'])*100)
    elif calculated_price[i] > new_ask[i] or new_ask[i] == 0 or ((new_ask[i]/calculated_price[i]) - 1 - dict['risk-free rate']) < 0:
        option_return.append(0)
    elif calculated_price[i] < new_ask[i] and new_ask[i] != 0:
        option_return.append(((new_ask[i]/calculated_price[i]) - 1 - dict['risk-free rate'])*100)
    i += 1

#####################################################################################################################################################################################

# ADJUSTING PROBABILITY
i = 0
while i < len(new_open_int):
    if option_return[i] == 0:
        new_sum_int = sum(new_open_int) - new_open_int[i]
    else:
        None
    i += 1

# CALCULATING OPEN INTEREST PROBABILITY
open_int_prob = []
for x in new_open_int:
    open_int_prob.append(x/new_sum_int)

# CALCULATING EXPECTED VALUE
expected_value = []
i = 0
while i < len(option_return):
    expected_value.append(option_return[i]*open_int_prob[i])
    i += 1
expected_val = sum(expected_value)

# VARIANCE CALCULATION (E(V^2))
ex_2_val = []
i = 0
while i < len(option_return):
    ex_2_val.append(((option_return[i])**2)*open_int_prob[i])
    i += 1

# STANDARD DEVIATION
standard_dev = mpmath.sqrt(sum(ex_2_val) - expected_val**2)

# SHARPE RATIO CALCULATION
sharpe_ratio = float(expected_val) / float(standard_dev)
print(ticker, option_type,'option Sharpe ratio is', sharpe_ratio)
