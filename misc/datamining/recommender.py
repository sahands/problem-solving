from __future__ import print_function
from __future__ import division

from itertools import chain
from collections import defaultdict
import sys
import math


__author__ = 'Sahand Saba'


def get_data():
    ratings = defaultdict(dict)
    for line in sys.stdin:
        rater, movie, rating = line.split('\t')
        rating = float(rating)
        ratings[rater][movie] = rating

    return ratings


def dot(u, v, uc, vc):
    return sum((x - uc) * (y - vc) for x, y in zip(u, v))


def pearson_similiarty(u, v):
    """Assume u and v are vectors of the same length at this point."""
    u_avg = sum(u) / len(u)
    v_avg = sum(v) / len(v)
    u_dot_v = dot(u, v, u_avg, v_avg)
    u_dot_u = dot(u, u, u_avg, u_avg)
    v_dot_v = dot(v, v, v_avg, v_avg)
    return u_dot_v / (math.sqrt(u_dot_u) * math.sqrt(v_dot_v))


def user_user_similarity(u, v, sim_func):
    u_vector = []
    v_vector = []
    for k in u:
        if k in v:
            u_vector.append(u[k])
            v_vector.append(v[k])

    return sim_func(u_vector, v_vector)


def get_rating(u, m, raters, sim, K=5):
    if u in raters[m]:
        return ratings[u][m]
    else:
        raters_to_use = sorted(raters[m], key=lambda v: sim[u, v], reverse=True)[:K]
        numerator = sum(sim[u, v] * ratings[v][m] for v in raters_to_use)
        denom = sum(sim[u, v] for v in raters_to_use)
        return numerator / denom


if __name__ == '__main__':
    ratings = get_data()
    users = ratings.keys()
    raters = defaultdict(set)
    for u, m in ratings.iteritems():
        for movie in m:
            raters[movie].add(u)

    sim_matrix = dict()
    for u in users:
        for v in users:
            sim = user_user_similarity(ratings[u],
                                       ratings[v],
                                       pearson_similiarty)
            sim_matrix[u, v] = sim

    print('Guessed ratings:')
    for u in users:
        for m, r in raters.iteritems():
            if u not in r:
                rating = get_rating(u, m, raters, sim_matrix)
                output = '{0}: {1} - {2:5.3f}'
                output = output.format(u, m, rating)
                print(output)
