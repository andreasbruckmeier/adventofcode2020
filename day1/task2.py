#!/usr/bin/env python3

def find(numbers, sum): 
    number_of_numbers = len(numbers)
    for i in range(0, number_of_numbers-1): 
        hashset = set() 
        current_sum = sum - numbers[i] 
        for j in range(i + 1, number_of_numbers): 
            if (current_sum - numbers[j]) in hashset: 
                print("Found: {} * {} * {} = {}".format(numbers[i], numbers[j], current_sum-numbers[j], numbers[i] * numbers[j] * (current_sum-numbers[j]))) 
                return
            hashset.add(numbers[j])

with open('input.txt') as f:
  find(list(map(int, f)), 2020)

