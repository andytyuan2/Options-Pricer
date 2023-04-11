import math
# dictionary contains all the parameters, u = up movement, d = down movement, probup = probability of an up movement, discount factor is used in the function below
dict = {'strike' : 90, 'price' : 100, 'time steps' : 20, 'sigma': 0.2, 'risk-free rate': 0.04, 'years': 1, 'dividend': 0.02, 'nexercise': 20}
u = math.exp(dict['sigma']*math.sqrt(dict['years']/dict['time steps']))
print('up', u)
d = 1/u
print('down', d)
probup = (((math.exp((dict['risk-free rate']-dict['dividend'])*dict['years']/dict['time steps'])) - d) / (u - d))
discount_factor = dict['risk-free rate']/dict['time steps']
timesteps = dict['time steps']

# function to calculate option price, contains the entire binomial tree
def binomial():
    payoffs = []
    n = 0
    while n < dict['time steps'] + 1: 
        payoffs.append(max(0, (dict['price']*(u**((dict['time steps'])-n))*(d**n) - dict['strike'])))
        n += 1
    print('payoffs are', payoffs)   
    dict['time steps']
    while dict['time steps'] >= 1:
        def combos(n, i):
            return math.factorial(n) / (math.factorial(n-i)*math.factorial(i))
        pascal = []
        for i in range(dict['time steps']+1):
            pascal.append(combos(dict['time steps'], i))
        probabilities = []
        i = 0
        for i in range(dict['time steps']+1):
            probabilities.append(pascal[i]*(probup**((dict['time steps'])-i))*((1-probup)**i))
            i += 1
        discounting1 = []
        i = 0
        while i < (dict['time steps']):
            if i == 0 and dict['nexercise'] > 1:
                discounting1.append(max(((dict['price']*(u**((dict['time steps']-1)-i))*(d**i) - dict['strike'])),            
                    ((((probup)*payoffs[i]) + ((1-probup)*payoffs[i+1]))
                                / (math.exp(discount_factor))))
                                )
            elif i > 0 and dict['nexercise'] > 1:
                discounting1.append(max(((dict['price']*(u**((dict['time steps']-1)-i))*(d**(i-1)) - dict['strike'])),            
                    ((((probup)*payoffs[i]) + ((1-probup)*payoffs[i+1]))
                                / (math.exp(discount_factor))))
                                )
            elif dict['nexercise'] == 1: 
                discounting1.append(((((probup)*payoffs[i]) + ((1-probup)*payoffs[i+1]))
                                / (math.exp(discount_factor))))
            i += 1   
        payoffs.clear()
        payoffs.extend(discounting1)
        dict['time steps'] -= 1
    return discounting1

print('option price at t=0 is', binomial())
