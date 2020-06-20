# get all combinations without itertools.combinations 

def all_combinations(arr: list):
	# count of all_combinations is 2^n 
	for i in range(2**len(arr)):
		comb = list()
		# match binary number with the array 
		for k, v in zip(bin(i)[2:].zfill(len(arr)), arr):
			if int(k):
				comb.append(v)
		yield comb

arr = ["apple", "orange", "banana"]

for p in all_combinations(arr):
	print(p)

"""
after running we get:
[]
['banana']
['orange']
['orange', 'banana']
['apple']
['apple', 'banana']
['apple', 'orange']
['apple', 'orange', 'banana']
"""
