import math
import mpmath
from datetime import date
from datetime import datetime as dt
from yahoo_fin import stock_info as si
import yfinance as yf
import numpy as np
dict = {'time steps' : 13}
##################################################################################################################################################################################### 
                     #****** MODIFICATION SECTION ******#
# TICKER
ticker = 'msft'                                             # not case sensitive
stock = yf.Ticker(ticker)

# CALL VS PUT
callput = 1                                                 # call = 1, put = -1; in callput

# AMERICAN VS EUROPEAN
AmerEu = 1

# EXPIRATION LIST
expiration = list(stock.options)
print('expiration dates are', expiration)

# EXPIRY DATE
date_of_exp = expiration[0]
expiry_date = dt.strptime(date_of_exp, '%Y-%m-%d').date()
##################################################################################################################################################################################### 
                    #****** PLEASE DO NOT MODIFY THE FOLLOWING CODE FOR THE CALCULATOR ******#
if callput == 1:                                    
    optionsname = 'call'
elif callput == -1:
    optionsname = 'put'
if AmerEu == 1:                                     # American = 1, European = -1; in AmerEu
    exercise = 'American'
elif AmerEu == -1:
    exercise = 'European'
            # NOTE: all US market options on securities seen on Yahoo Finance are American exercise, only indexes are European
# CHAIN DATA
option_info = {}
for x in expiration:
    if callput == 1:
        chaindata = stock.option_chain(x).calls
    elif callput == -1:
        chaindata = stock.option_chain(x).puts
    option_info[x] = chaindata

# OPTION EXPIRY
todays = date.today()
years = (expiry_date - todays).days/365

# RISK FREE RATE
ratefloat = (si.get_live_price('^TNX'))
risk_free_rate = ratefloat * years / 100

# DIVIDEND YIELD
def div_yield():
    try:
        divrate = stock.info['dividendRate']
    except KeyError:
        divrate = 0
    return divrate
dividend = div_yield() * years/100

# STRIKES
strikes = list(option_info[date_of_exp]['strike'])

# VOLATILITY
vol = list(option_info[date_of_exp]['impliedVolatility'])

# PRICE EXTRACTION
price = stock.info['currentPrice']

# PARAMETER SETTING
calculated_price = []
for i,j in zip(strikes,vol):
    strike = i
    sigma = j/100
    if j == 0:
        u = 1.0000001
    else:
        u = math.exp(sigma*math.sqrt(years/dict['time steps']))
    d = 1/u
    probup = (((math.exp((risk_free_rate-dividend)*years/dict['time steps'])) - d) / (u - d))
    discount_factor = risk_free_rate/dict['time steps']
    duration_of_time_step = (years/dict['time steps'])
##################################################################################################################################################################################### 
# BINOMIAL FUNCTION    
    def binomial():
        Tstep = dict['time steps']
        payoffs = []
        for n in range(Tstep+1):
            payoffs.append(max(0, callput*(price*(u**((Tstep)-n))*(d**n) - strike)))
        while Tstep >= 1:
            discounting1 = []
            for i in range(0,Tstep):
                if AmerEu == 1:
                    American_payoff = (callput*(price*(u**(Tstep-i-1)*(d**i)) - strike))
                    European_payoff = (((probup)*payoffs[i]) + ((1-probup)*payoffs[i+1])) / (math.exp(discount_factor))
                    discounting1.append(max(American_payoff, European_payoff))
                elif AmerEu == -1:
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
bids = list(option_info[date_of_exp]['bid'])
        
# ASK PRICES LIST
asks = list(option_info[date_of_exp]['ask'])

# OPEN INTEREST LIST
open_int = list(option_info[date_of_exp]['openInterest'])

# EXCESS RETURN
option_return = []
for i, j, k in zip(calculated_price, bids, asks):
    if i <= j or j == 0 or ((i/j) - 1 - risk_free_rate) < 0:
        option_return.append(0)
    elif i > j and j != 0:
        returns = ((i/j) - 1 - risk_free_rate)*100
        option_return.append(returns)
    elif i >= k or k == 0 or ((k/i) - 1 - risk_free_rate) < 0:
        option_return.append(0)
    elif i < k and k != 0:
        returns = ((k/i) - 1 - risk_free_rate)*100
        option_return.append(returns)

# PROBABILITIES OF OUTCOMES
prob_denom = 0
probabilities = []
for i, j in zip(open_int, option_return):
    if j != 0:
        prob_denom += i
    else:
        None
for x,y in zip(open_int, option_return):
    if y != 0:
        probabilities.append(x/prob_denom)
    else:
        None
option_return = [i for i in option_return if i != 0]  # removes all the zeroes in the list 

# CALCULATING EXPECTED VALUE
def expected_value():
    weighted_avg = np.average(option_return, weights=probabilities)
    return weighted_avg

# STANDARD DEVIATION
def standard_dev():
    variance = np.average((option_return - expected_value())**2, weights=probabilities)
    return math.sqrt(variance)
print(f'Standard deviation is {standard_dev()} and expected value is {expected_value()}.')

# SHARPE RATIO CALCULATION
def sharpe():
    try:
        sharpe_ratio = float(expected_value()) / float(standard_dev())
    except ZeroDivisionError:
        sharpe_ratio = 0
    return sharpe_ratio
name = stock.info['longName']
print(name, 'current', optionsname,'option Sharpe ratio for', date_of_exp,'is', sharpe())
