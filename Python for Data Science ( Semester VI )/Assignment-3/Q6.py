import math

def normal_approximation_to_binomial(n, p):
    mu = p*n
    sigma = math.sqrt(p * (1-p) * n)
    return mu, sigma

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x-mu) / math.sqrt(2) / sigma)) / 2

def normal_probability_below(x, mu=0, sigma=1):
    return normal_cdf(x, mu, sigma)

def normal_probability_above (x, mu=0, sigma=1):
    return 1-normal_cdf(x, mu, sigma)

def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        return 2 * normal_probability_below(x, mu, sigma)

x=110
mu=100
sigma=5

print(two_sided_p_value(x,mu,sigma))
print(two_sided_p_value(x-0.5,mu,sigma))
