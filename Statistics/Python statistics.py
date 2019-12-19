# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:44:49 2019

@author: Mohit Kumar
"""

Random Variables - Discrete(Number or errors) / Continuous(Height, Temp, Current)
Probability Distribution - equation/table


Discrete PD - PMF = f(x) = P(X = x)
CDF = F(x) = P(X <= x)

1. B

# statistics
#Distribution
################# Discrete Distribution ##############################
#PMF - For discrete variates the probability mass function (PMF) 
# gives the probability of the variate having a value x.
#Binomial Distribution
import scipy.stats
import matplotlib.pyplot as plt

n,p = 12,0.5

## Mean, Var, Skewness
#method of moments
mean, var, sk = scipy.stats.binom.stats(n,p,moments ='mvs')

## PMF and CDF
pmf = scipy.stats.binom.pmf(6, n, p)
cdf = scipy.stats.binom.cdf(4, n, p)

## Draw PMF
x = scipy.linspace(0,10,11)
pmf = scipy.stats.binom.pmf(x, n, p)
plt.bar(x, pmf)

# cdf
scipy.stats.binom.cdf(5,n,p)

P(X <= x) = 0.22

## ppf - Inverse of CDF - 
scipy.stats.binom.ppf(0.7,12,0.2)

scipy.stats.binom.pmf(4, 12, 0.2)
1 - scipy.stats.binom.cdf(3, 12, 0.2)

## Value of RV that probability taking that value or less than that is 0.7
P(X >= 4 ) = 1 - P(X <= 3)


## Example:
#1. 
scipy.stats.binom.pmf(4, 12, 0.2)
#2. 
scipy.stats.binom.cdf(4, 12, 0.2)

####################### Poisson Distribution
mean,var,ske,kurtw = scipy.stats.poisson.stats(3,moments ='mvsk')

### PMF and CDF
scipy.stats.poisson.pmf(5,10)
scipy.stats.poisson.cdf(12,10)

x = scipy.linspace(0,10,11)
pmf = scipy.stats.poisson.pmf(x,2.3)
plt.bar(x, pmf)

# Example:
#1.
scipy.stats.poisson.pmf(2, 2.3)
1 - scipy.stats.poisson.pmf(0, 4.6)







#2. 
1 - scipy.stats.poisson.cdf(0, 4.6)












#################### Continous Probability Distributions ###########################
[150 - 170]
P(X = 151) = 1 / infinite = 0 - PMF 
PDF - Probability 

[a , b]
151-152
PDF = f(x) = P(a<=X<=b)
CDF = F(x) = P(X <= x)

# normal distribution
# PDF - For continuous variates the probability density function (PDF) is 
#proportional to the probability 
#of the variate being in a small interval about the given value.

from scipy import stats
import matplotlib.pyplot as plt

npdf = stats.norm(50,10)
x = range(0,100)
plt.plot(x, npdf.pdf(x), 'k-', lw=2)
npdf.pdf(0)

#probability density function
scipy.stats.norm(50,10).pdf(45)

# cumulative density function
# CDF gives the probability that the variate has a value less than or equal to the given value.
scipy.stats.norm(50,10).cdf(45) #= P(X <= 45) ~N(50, 10)
scipy.stats.norm(50,10).cdf(60) - scipy.stats.norm(50,10).cdf(45)

# PPF - percent point function - PPF is the inverse of the CDF. 
# That is, PPF gives the value of the variate for 
# which the cumulative probability has the given value
stats.norm.ppf(0.5, 0, 1.0) # 0

#### Example:
#1.
1 - scipy.stats.norm.cdf(500, 527, 112)
#2. 
scipy.stats.norm.ppf(0.95, 527, 112)

# explicity finding the pobability density function for nd
from math import pi
from math import exp
from scipy import stats

def normal_pdf(x, mu, sigma):
    return 1.0 / (sigma * (2.0 * pi)**(1/2)) * exp(-1.0 * (x - mu)**2 / (2.0 * (sigma**2)))

################ CLT ############################
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#%matplotlib notebook
import scipy.stats as st

# 1000 simulations of die roll
n = 1000

# In each simulation, there is one trial more than the previous simulation
avg = []
for i in range(1,n):
    a = np.random.randint(1,7,10)
    avg.append(np.average(a))
    
# sample 10 expected value of die rolls
avg[1:10]
plt.hist(avg[0:100])



#################### Confidence Interval ########################



#Mean Interval Estimation using t dist
import numpy as np
import scipy.stats
import statsmodels.stats.api as sms
x = range(10,50)
scipy.stats.t.interval(0.95, len(x) - 1, loc = np.mean(x), scale = scipy.stats.sem(x))
lower, upper = sms.DescrStatsW(x).tconfint_mean(alpha = 0.05)

#Mean Interval Estimation using Normal Distribution
import statsmodels.stats.api as sms
x = range(10,50)
scipy.stats.norm.interval(0.95, loc = np.mean(x), scale = scipy.stats.sem(x))
lower, upper = sms.DescrStatsW(x).zconfint_mean(alpha = 0.05)

#### Import diamonds
import pandas as pd
df = pd.read_csv("D:/diamonds.csv")

## Price Mean CI - 95% (90%) (99%)
scipy.stats.t.interval(0.95, len(df["price"])-1, loc = np.mean(df["price"]), scale = scipy.stats.sem(df["price"]))


zalpha/2 = 
scipy.stats.norm.ppf(0.995)


scipy.stats.norm.ppf(0.995)

#################### Hypothesis Testing ######################### 
Ho: mu = 3 ounces
Ha: mu != 3 - 

Two sided 


Ho: mu = 50 cm/s
Ha: mu != 50 cm/s

Two sided 

3. 
Ho: mu >= 50 cm/s
Ha: mu < 50 cm/s - One Sided 


Ha: mu != 50

Ho: mu = 50000
Ha: mu < 50000

P(Type I error) = alpha = significance level
P(Type II Error) = beta

Ho: mu = 10.5 Lac
Ha: mu != 10.5 Lac

at most 6 success
X <= 6 

at least 6 success
1 - P(X <= 5)


### There are 2 approaches to perform the Hyp testing procedre

## 1st Procedure
### Significance Level - aplha = P(Type I error)
### Critical Values - aplha = 0.05, Critical values - +-1.96
                      alpha = 0.01, Critical Value - +-2.575
### Test Statistics (calculating from sample)
# Procedure 1                      
1. State Ho and Ha - 
2. CHoose alpha
3. Calculate Test STatistic                      
4. Calculate Critical Values
                      
                      
# Preocedure                      
1. State Ho and Ha
2. CHoose alpha
3. Calculate Test STatistic
4. P-Value 
2*scipy.stats.norm.cdf(-2)                  
    
scipy.stats.norm.cdf(0.88)

################################################                 
Ho: mu = 52
Ha: mu > 52

std = 4.5
n = 100
xbar = 52.8
alpha = 0.05


### Approach 1 - Critical Values
Test - STatistic = (52.8 - 52) / (4.5/10)
# z = 1.78
# Critical Values - 
scipy.stats.norm.ppf(0.95)
## Rejecting Null Hypothesis

### Approach 2 - pvalue     
P[1.78,inf] = 1 - P(X < 1.78) =
1 - scipy.stats.norm.cdf(1.78)
## Rejecting the Null Hypothesis
                       
            

### T - test 
Ho: mu = 168
Ha: mu != 168

alpha = 0.05

Test statistic (T statistic) = 1.46

# Approach 1: 
Critical Values - 1.96
Critical Value - 
scipy.stats.t.ppf(0.975, 24)
scipy.stats.t.ppf(0.025, 24)
 
# Approach 2: P-Value
2*(1 - scipy.stats.t.cdf(1.46, 24))

###########
scipy.stats.chi2.ppf(0.95, 19)



## One Population 
## 3 cases:
1. HT on Mean, Population Variance Known

## 1. Critical Value
## 2. P-Value
## Use z (Standard Normal DIstribution)

2. HT on Mean, Pop Variance Unknown - T Statistic (T distribution)

3. HT on Variance - Chi-Square Distribution ()          


Ho: muF >= muM <=> muF - muM = 0 
Ha: muF < muM  <=> muF - muM < 0

scipy.stats.norm.ppf(0)

Ho: you are not pregnant - Accepting  - Type II error
Ha: Pregnant - 

## Type I error - Rejecting the H0 when it was True = alpha = p(Type I error)
## Type II error - Accepting the H0 When it was wrong = Beta = P(Type II error)

scipy.stats.norm.ppf(0.9)


Case1: Pop variance Known - z test statistic
z = Xbar - mu / (sigma/sqrt(n))

Case 2: Pop Variance Unknown
t = Xbar - mu / (sample std (s) / sqrt(n))
                      
                      
         



             

### p-value approach to test the Hypothesis
scipy.stats.t.ppf(0.025, 24)
2*scipy.stats.t.cdf(-1.46, 24)




mu = 2
xbar = 2.1
sd = 0.25
n = 35
se = sd/np.sqrt(n)
z = (xbar-mu)/se
#2.366
#single tail
alpha = 0.05
z_alpha = st.norm.ppf(0.95)

#Two tail
st.norm.ppf(.975)
1.959963984540054
st.norm.ppf(.025)
-1.960063984540054



# F stats
F_critical = st.f.ppf(0.95,2,12)
#3.8852938346523933

# Chi Square Distribution 
scipy.stats.chi.pdf(3,2)







################### anova #######################
import pandas as pd
import scipy.stats as stats
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt

# Loading data
df = pd.read_csv("https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/difficile.csv")
df.drop('person', axis= 1, inplace= True)

# Recoding value from numeric to string
df['dose'].replace({1: 'placebo', 2: 'low', 3: 'high'}, inplace= True)
    
# Gettin summary statistics
rp.summary_cont(df['libido'])
rp.summary_cont(df['libido'].groupby(df['dose']))

stats.f_oneway(df['libido'][df['dose'] == 'high'], 
             df['libido'][df['dose'] == 'low'],
             df['libido'][df['dose'] == 'placebo'])


results = ols('libido ~ C(dose)', data=df).fit()
results.summary()

aov_table = sm.stats.anova_lm(results, typ=3)
aov_table


import pandas as pd
data = pd.read_csv("C:\\Users\\gunjan.thareja\\Downloads\\ToothGrowth.csv")
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.graphics.factorplots import interaction_plot
import matplotlib.pyplot as plt
from scipy import stats
%matplotlib inline
fig = interaction_plot(data.dose, data.supp, data.len,
             colors=['red','blue'], markers=['D','^'], ms=10)


N = len(data.len)
df_a = len(data.supp.unique()) - 1
df_b = len(data.dose.unique()) - 1
df_axb = df_a*df_b 
df_w = N - (len(data.supp.unique())*len(data.dose.unique()))

grand_mean = data['len'].mean()
ssq_a = sum([(data[data.supp ==l].len.mean()-grand_mean)**2 for l in data.supp])
ssq_b = sum([(data[data.dose ==l].len.mean()-grand_mean)**2 for l in data.dose])
ssq_t = sum((data.len - grand_mean)**2)

#with variance
vc = data[data.supp == 'VC']
oj = data[data.supp == 'OJ']
vc_dose_means = [vc[vc.dose == d].len.mean() for d in vc.dose]
oj_dose_means = [oj[oj.dose == d].len.mean() for d in oj.dose]
ssq_w = sum((oj.len - oj_dose_means)**2) +sum((vc.len - vc_dose_means)**2)
     dose
supp 2     1      0.5
vc   7     16.77  26.139 
oj 13.23   22.7   26.06

#interaction
ssq_axb = ssq_t-ssq_a-ssq_b-ssq_w
#msa_a
ms_a = ssq_a/df_a
#msb
ms_b = ssq_b/df_b
#Mean Square AxB
ms_axb = ssq_axb/df_axb

ms_w = ssq_w/df_w

f_a = ms_a/ms_w
f_b = ms_b/ms_w
f_axb = ms_axb/ms_w

p_a = stats.f.sf(f_a, df_a, df_w)
p_b = stats.f.sf(f_b, df_b, df_w)
p_axb = stats.f.sf(f_axb, df_axb, df_w)

results = {'sum_sq':[ssq_a, ssq_b, ssq_axb, ssq_w],
           'df':[df_a, df_b, df_axb, df_w],
           'F':[f_a, f_b, f_axb, 'NaN'],
            'PR(>F)':[p_a, p_b, p_axb, 'NaN']}
columns=['sum_sq', 'df', 'F', 'PR(>F)']
 
aov_table1 = pd.DataFrame(results, columns=columns,
                          index=['supp', 'dose', 
                          'supp:dose', 'Residual'])
    
    
    
formula = 'len ~ C(supp) + C(dose)+C(var3) + C(supp):C(dose)+C(Supp):C(var3)+C(dose):C(Supp):C(var3)'
model = ols(formula, data).fit()
aov_table = anova_lm(model, typ=2)