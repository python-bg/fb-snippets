# permutations without itertools.permutations 

def permutations(arr: list):
	# count of permutations is 2^n 
	for i in range(2**len(arr)):
		perm = list()
		# match binary number with the array 
		for k, v in zip(bin(i)[2:].zfill(len(arr)), arr):
			if int(k):
				perm.append(v)
		yield perm

arr = ["apple", "orange", "banana"]

for p in permutations(arr):
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