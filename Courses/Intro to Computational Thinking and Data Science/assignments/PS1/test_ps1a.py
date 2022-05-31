# -*- coding: utf-8 -*-

from ps1a import load_cows, greedy_cow_transport, brute_force_cow_transport

filename = 'ps1_cow_data.txt'

cows = load_cows(filename)

#trips = greedy_cow_transport(cows)

trips = brute_force_cow_transport(cows, 12)

print(trips)