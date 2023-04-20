This is the CRR binomial pricing model for both American and European options; using python. Written by Andy in 2023 at Western University with the mathematical support of professor Lars Stentoft. At this time I was in my third year of a 4-year bachelor's degree in accounting and applied statistics.
It served as a pilot project so I could learn Python and quantitative finance concepts outside of my curriculum.

The main file that includes Greeks and Probabilities has a variety of functions. It calculates all the Greeks, some by using the tree and some by using finite differences (derivatives). Additionally, there are probabilities of the individual nodes at payoff according to the binomial distribution. Though you will have to print these probabilties yourself.

The option price effect folder examines the option price sensitivity to changes in those parameters. My findings are described below. The default amounts are strike = $100, underlying price = $100, volatility = 20%, Time to expiry (years) = 1 year, risk-free rate = 4%, dividend yield = 2%, time steps = 10. The sensitivity analysis takes the lowest of the specific parameter and increases it to a specific hard limit. These are the graphs resulting from the data I extracted from the models.

The full data sheet I used is the Excel file in the repo. To note, most of the parameter sensitivities calculated do not have an imposed decimal limit, but the risk-free rate sensitivity analysis does. For the file without the risk-neutral adjustment, the limit is 2 decimal places on the European call; the limit is 3 decimal places on the European put as well as the American put and call. For the file with the risk-neutral adjustment, the decimal limit is 5. 

The reason why those limits exist is because I wanted to model the prices up to 400% risk-free rate. The graph for that would be essentially useless however, so I only captured the graph from 0% to 160%. 

Risk-Free Rate without Risk-Neutral Drift Adjustment:
![image](https://user-images.githubusercontent.com/125106540/231875230-f2ddda38-612e-4ca4-85e9-ec3cb476141a.png)


Risk-Free Rate with Risk-Neutral Drift Adjustment:
![image](https://user-images.githubusercontent.com/125106540/231875608-c4b39b7b-c168-4538-9c80-59d77b51a6d4.png)

Risk-Free Rate with Risk-Neutral Drift Adjustment, up to 75% risk-free rate:
![image](https://user-images.githubusercontent.com/125106540/233242638-5295569d-f0d6-4c65-85f7-0e833e1af761.png)

Risk-Free Rate with Risk-Neutral Drift Adjustment, up to 5% risk-free rate:
![image](https://user-images.githubusercontent.com/125106540/233242870-f3f23069-184b-4d87-bf6c-a8ed890048d1.png)

Dividend Yield:
![image](https://user-images.githubusercontent.com/125106540/231875795-c2f0400f-18a0-423f-977b-d3e5aa03cff3.png)

Volatility:
![image](https://user-images.githubusercontent.com/125106540/231027488-6fbbca4e-db94-4918-9d8c-5d1ec22c9065.png)

Years / Time to Expiry:
![image](https://user-images.githubusercontent.com/125106540/231875908-f597c952-0912-4f1a-968f-2ef51aa1a8b7.png)

Time Steps:
![image](https://user-images.githubusercontent.com/125106540/231875992-9d56cb0a-ef20-41d4-861b-3bd7c5e3dd12.png)

Option Strike:
![image](https://user-images.githubusercontent.com/125106540/231876066-e1cf0338-a5d3-4ba7-a7c7-444ba494379c.png)

Underlying Price:
![image](https://user-images.githubusercontent.com/125106540/231876195-f7a7d929-d7d1-43b6-82f2-e5e654c5be03.png)
