This is the binomial pricing model for both American and European options; using python. Written by Andy in 2023 at Western University with the mathematical support of professor Lars Stentoft. At this time I was in my third year of a 4-year bachelor's degree in accounting and applied statistics.
It served as a pilot project so I could learn Python and quantitative finance concepts outside of my curriculum.

The main file that includes Greeks and Probabilities has a variety of functions. It calculates all the Greeks, some by using the tree and some by using finite differences (derivatives). Additionally, there are probabilities of the individual nodes at payoff according to the binomial distribution. 

The option price effect folder examines the option price sensitivity to changes in those parameters. My findings are described below. The default amounts are strike = 100, underlying price = 100, volatility = 20%, years = 1, risk-free rate = 4%, dividend yield = 2%, time steps = 10. The sensitivity analysis takes the lowest of the specific parameter and increases it to a specific hard limit. These are the graphs resulting from the data I extracted from the models.

Risk-Free Rate
![image](https://user-images.githubusercontent.com/125106540/231027367-b9a89bf8-55dc-4d22-a1de-1496d1eb0d05.png)

Dividend Yield 
![image](https://user-images.githubusercontent.com/125106540/231027439-228ba0e5-e221-4d81-b568-c3dcccfc08a8.png)

Volatility
![image](https://user-images.githubusercontent.com/125106540/231027488-6fbbca4e-db94-4918-9d8c-5d1ec22c9065.png)

Years
![image](https://user-images.githubusercontent.com/125106540/231027582-1cfffbb8-7994-477b-a57f-8d74356ec35b.png)

Time Steps
![image](https://user-images.githubusercontent.com/125106540/231027709-ad47dc13-c76a-47ac-a21e-4314a543d9d9.png)

Option Strike
![image](https://user-images.githubusercontent.com/125106540/231027810-2174adb4-5a87-4ebe-a1ff-3d4c3bafa779.png)

Underlying Price
![image](https://user-images.githubusercontent.com/125106540/231027918-e047999e-6dd7-4c78-8b0e-1004474611b0.png)
