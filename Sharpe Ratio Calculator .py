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
dict = {'time steps' : 13}

                     #****** MODIFICATION SECTION ******#
# TICKER
ticker = 'aapl'                                             # not case sensitive

# CALL VS PUT
dict['callput'] = 1

# AMERICAN VS EUROPEAN
dict['AmerEu'] = 1

# EXPIRATION LIST
expiration = op.get_expiration_dates(ticker)
print('expiration dates are', expiration)

# EXPIRY DATE
date_of_exp = 'June 9, 2023'                               # keep in mind to format this properly, especially the months
expiry_date = date(2023, 6, 9)                             # formattted as (year, int(month), day)

if dict['callput'] == 1:                                    # call = 1, put = -1; in callput
    option_type = 'calls'
    optionsname = 'call'
elif dict['callput'] == -1:
    option_type = 'puts'
    optionsname = 'put'
if dict['AmerEu'] == 1:                                     # American = 1, European = -1; in AmerEu
    exercise = 'American'
elif dict['AmerEu'] == -1:
    exercise = 'European'
            # NOTE: all US market options on securities seen on Yahoo Finance are American exercise, only indexes are European

# CHAIN DATA
chaindata = op.get_options_chain(ticker)[option_type]
option_info = {}
opinfo = option_info
for daate in expiration:
    opinfo[daate] = chaindata

# OPTION EXPIRY EXTRACTION
todays = date.today()
time_between = expiry_date - todays
dict['years'] = time_between.days/365

# RISK FREE RATE EXTRACTION
ratefloat = (si.get_live_price('^TNX'))
dict['risk-free rate'] = ratefloat * dict['years'] / 100

# DIVIDEND YIELD EXTRACTION
def div_yield():
    stockdiv = yaf.Ticker(ticker)
    try:
        divrate = stockdiv.info['dividendRate']
    except KeyError:
        divrate = 0
    return divrate
dict['dividend'] = div_yield() * dict['years']/100

# STRIKES EXTRACTION
old_strike = opinfo[date_of_exp][['Strike']].values.tolist()
strikes= []
for x in old_strike:
    for item in x:
        strikes.append(int(item))

# VOLATILITY EXTRACTION
old_vol = opinfo[date_of_exp][['Implied Volatility']].values.tolist()
vol = []
for x in old_vol:
    for item in x:
        items = item.replace("%","").replace(",","")
        vol.append(float(items))

# PRICE EXTRACTION
dict['price'] = si.get_live_price(ticker)

# PARAMETER SETTING
calculated_price = []
strikes.append(0)
vol.append(0)
print(strikes)
for i,j in zip(strikes,vol):
    dict['strike'] = i
    dict['sigma'] = j/100
    if j == 0:
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
        for n in range(Tstep+1):
            payoffs.append(max(0, dict['callput']*(dict['price']*(u**((Tstep)-n))*(d**n) - dict['strike'])))
        while Tstep >= 1:
            discounting1 = []
            for i in range(0,Tstep):
                if dict['AmerEu'] == 1:
                    American_payoff = (dict['callput']*(dict['price']*(u**(Tstep-i-1)*(d**i)) - dict['strike']))
                    European_payoff = (((probup)*payoffs[i]) + ((1-probup)*payoffs[i+1])) / (math.exp(discount_factor))
                    discounting1.append(max(American_payoff, European_payoff))
                elif dict['AmerEu'] == -1:
                    discounting1.append((((probup)*payoffs[i]) + ((1-probup)*payoffs[i+1]))
                                        / (math.exp(discount_factor)))
                else:
                    pass 
                
            payoffs.clear()
            payoffs.extend(discounting1)
            Tstep -= 1
        return discounting1
    if binomial()[0] < 0:
        calculated_price.append(0)
    else:
        calculated_price.append(binomial()[0])
#####################################################################################################################################################################################
# BID PRICES LIST
old_bid = opinfo[date_of_exp][['Bid']].values.tolist()                      
bids = []                            
for x in old_bid:
    for item in x:
        if item == '-':
            bids.append(0)
        else:
            bids.append(float(item))
        
# ASK PRICES LIST
old_ask = opinfo[date_of_exp][['Ask']].values.tolist()                       
asks = []
for x in old_ask:
    for item in x:
        if item == '-':
            asks.append(0)
        else:
            asks.append(float(item))

# OPEN INTEREST LIST
old_open_int = opinfo[date_of_exp][['Open Interest']].values.tolist()       
open_int = []
for x in old_open_int:
    for item in x:
        open_int.append(float(item))

# EXCESS RETURN
option_return = []
for i, j, k in zip(calculated_price, bids, asks):
    if i <= j or j == 0 or ((i/j) - 1 - dict['risk-free rate']) < 0:
        option_return.append(0)
    elif i > j and j != 0:
        option_return.append(((i/j) - 1 - dict['risk-free rate'])*100)
    elif i >= k or k == 0 or ((k/i) - 1 - dict['risk-free rate']) < 0:
        option_return.append(0)
    elif i < k and k != 0:
        option_return.append(((k/i) - 1 - dict['risk-free rate'])*100)

# PROBABILITIES OF OUTCOMES
prob_denom = 0
for i, j in zip(open_int, option_return):
    if j != 0:
        prob_denom += i
    else:
        None
probabilities = []
for x,y in zip(open_int, option_return):
    if y != 0:
        probabilities.append(x/prob_denom)
    else:
        None
option_return = [i for i in option_return if i != 0]

# CALCULATING EXPECTED VALUE
expected_value = []
for i, j in zip(probabilities, option_return):
    expected_value.append(i*j) 

# VARIANCE CALCULATION (E(V^2))
def expected_square_value():
    expected_square_value = []
    for i,j in zip(option_return,probabilities):
        expected_square_value.append(((i)**2)*j)
    return expected_square_value

# STANDARD DEVIATION
standard_dev = mpmath.sqrt(sum(expected_square_value()) - (sum(expected_value))**2)

# SHARPE RATIO CALCULATION
sharpe_ratio = float(sum(expected_value)) / float(standard_dev)
company = yaf.Ticker(ticker)
name = company.info['longName']
print(name, 'current', optionsname,'option Sharpe ratio for', date_of_exp,'is', sharpe_ratio)

