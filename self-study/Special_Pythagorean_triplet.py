'''

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

https://en.wikipedia.org/wiki/Pythagorean_triple
'''
s = 2

a = 2 * s
b = (s ** 2) - 1
c = (s ** 2) + 1

print(a, b, c)

for i in range(1, 1000):
	s = i
	a = 2 * s
	b = (s ** 2) - 1
	c = (s ** 2) + 1
	d = a + b + c
	print('%s + %s + %s = %s' % (a, b, c, d))
	if d == 1000:
		print('we found it!! a: %s, b: %s, c: %s' % (a, b, c))
