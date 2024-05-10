import math

def normal_approximation_to_binomial(n, p):
    mu = p * n
    sigma = math.sqrt(p * (1-p) * n)
    return mu, sigma

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf ((x-mu) / math.sqrt(2) / sigma)) / 2

normal_probability_below = normal_cdf

def normal_probability_above (lo, mu=0, sigma=1):
    return 1-normal_cdf(lo, mu, sigma)

def normal_probability_between (lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma)-normal_cdf(lo, mu, sigma)
def normal_probability_outside (lo, hi, mu=0, sigma=1):
    return 1-normal_probability_between (lo, hi, mu, sigma)

mu, sigma = normal_approximation_to_binomial (100, 0.6)
print(normal_probability_above (60, mu, sigma))
print(normal_probability_between (50, 70, mu, sigma))
