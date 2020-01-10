import itertools

'''
@function ways
@description finds all the possible ways a certain sum could be achieved from a set of numbers
@param x {list<float>} set of numbers 
@param n {int} number of terms to be summed
@param s {float} expected sum 
'''
def ways(x, n, s):
	combs = [p for p in itertools.product(x, repeat=n)]
	sums = list(map(sum,combs))
	final = []
	for i,summ in enumerate(sums):
		if summ == s:
            final.append(combs[i])
    return final
    
