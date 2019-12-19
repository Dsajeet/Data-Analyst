# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 08:25:06 2019

@author: z003u3cr
"""

from scipy import stats
import scipy

### Binomial
## Example 1
stats.binom.pmf(0, 10, 0.5)
stats.binom.cdf(2, 10, 0.5)
P(X = 6) = pmf

stats.binom.pmf(#successess, #trials, prob of success)
stats.binom.pmf(8, 10, 0.5)

exact 

### Prob of getting at most 5 heads 
P(X <= 5) = P(X = 0) + P(X = 1) + ...... + P(X = 5)
stats.binom.cdf(5, 10, 0.5)

### Prob of getting at least 6 heads
1 - cdf(6)

P(X = 0) = pmf = 

stats.poisson.pmf(0, 1.5)
stats.poisson.pmf(2, 1.5)
## Prob of getting 1 error in 200 pages
stats.poisson.pmf(1, 3)

## 
P(X>=5) = 1 - P(X<5) = 1 - P(X <= 4)
stats.po


lamda = 1200
## prob 8000
stats.poisson.pmf(8000, 1200)
        
### Poisson Distribution
stats.poisson.pmf(0, 1.5)
stats.poisson.cdf(2, 1.5)

### Normal DIstribution
stats.norm.cdf(1.52)
x = scipy.linspace(-10, 10, 21)
mean, var, skew, kurt = stats.norm.stats(moments = "mvsk")


### independent events vs mut exclusive
### Bayes Theorem

### 

A = Ai,j

B = Bi,j 

import numpy as np
A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])



