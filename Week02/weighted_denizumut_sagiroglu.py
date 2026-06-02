import random
def weighted_srs(data, n, weights, with_replacement=True):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    pool_d, pool_w, sample = list(data), list(weights) if weights else [1]*len(data), []
    for _ in range(n):
        i = random.choices(range(len(pool_d)), weights=pool_w, k=1)[0]
        sample.append(pool_d.pop(i)); pool_w.pop(i)
    return sample
