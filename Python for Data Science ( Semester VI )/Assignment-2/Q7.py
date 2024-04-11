import math

def normal_cdf(x):
    return (1 + math.erf(x / math.sqrt(2))) / 2

def inverse_normal_cdf(
    p: float,
    mu: float = 0,
    sigma: float = 1,
    tolerance: float = 0.00001) -> float:
    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1: return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    low_z = -10.0 # normal_cdf(-10) is (very close to) 0
    hi_z = 10.0 # normal_cdf(10) is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2 
        mid_p = normal_cdf(mid_z)
        if mid_p < p:low_z = mid_z 
        else:
            hi_z = mid_z 
    return mid_z

