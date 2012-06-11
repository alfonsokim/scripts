
big_str_num = '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''.strip().replace('\n', '')

def fibo_lineal(n):
	i = 1
	j = 0
	for k in range(1, n):
		t = i+j
		i = j
		j = t
	return j
	


def fibo(n):
	if n <= 1:
		return n
	if n in cache:
		return cache[n]
	else:
		cache[n] = fibo(n-1) + fibo(n-2)
		return cache[n]


def isprime(n):
	'''check if integer n is a prime'''
	# make sure n is a positive integer
	n = long(n)
	n = abs(n)
	# 0 and 1 are not primes
	if n < 2:
		return False
	# 2 is the only even prime number
	if n == 2: 
		return True    
	# all other even numbers are not primes
	if not n & 1: 
		return False
	# range starts with 3 and only needs to go up the squareroot of n
	# for all odd numbers
	for x in range(3, int(n**0.5)+1, 2):
		if x == 0:
			return False
	return True
	

def primeFactors(n, factor):
	factors = []
	while (n % factor != 0):
		factor = factor + 1
	
	factors.append(factor)
	
	if n > factor:
		factors.extend(primeFactors(n / factor, factor))
	print factors
	return factors

#print max(primeFactors(600851475143, 2))

def primes(count):
	prime_nums = [2]
	#for i in xrange(limit):
	i = 3
	while True:
		if isprime(i):
			prime_nums.append(i)
		if len(prime_nums) == count:
			break
		i += 2
	return prime_nums

	
def primes_below(limit):
	prime_nums = [2]
	#for i in xrange(limit):
	for i in range(3, limit+1, 2):
		if isprime(i):
			#print i
			prime_nums.append(i)
	return prime_nums
	
def big_num():
	offset = 5
	max = 0
	for i in range(len(big_str_num)-offset):
		#print big_str_num[i:i+offset]
		num = reduce(lambda x,y: x*y, [int(num) for num in big_str_num[i:i+offset]])
		if num > max:
			max = num
	return max
	
	
def get_c(a, b):
	return 1000 - a - b
	
def validate_c(a, b, c):
	return (a*a) + (b*b) == (c*c)

def pitagoras():
	for a in range(1001):
		for b in range(a+1):
			c = get_c(a, b)
			if validate_c(a, b, c):
				return a*b*c
	
if __name__ == '__main__':
	#import sys
	#print ','.join([str(fibo_lineal(n)) for n in range(int(sys.argv[1]))])
	#print sum([fibo_lineal(n) for n in range(int(sys.argv[1])) if fibo_lineal(n) % 2 == 1])
	#anum = long(600851475143)
	#print '\n'.join([str(long(a)) for a in xrange(anum) if isprime(long(a)) and long(anum) % long(a) == 0])
	#print max([str(a) for a in xrange(anum) if isprime(a) and anum % a == 0])
	#print max(primeFactors(600851475143, 2))
	print sum(primes_below(2000000))
	
	
	
	
	