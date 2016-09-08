'''
The sum of the squares of the first ten natural numbers is,
	12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
	(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_of_the_squares_of_the_natural_numbers(rng):
	squrs = []
	for i in range(rng + 1):
		a = i ** 2
		squrs.append(a)
	return(sum(squrs))

def squre_of_the_sum_of_natural_numbers(rng):
	ints = []
	ints.extend(range(rng+1))
	squrs = sum(ints) ** 2
	return(squrs)

def sum_squre_difference(sum_of_the_squares, squares_of_the_sum):
	return(squares_of_the_sum - sum_of_the_squares)

inputNumb = 100
a = sum_of_the_squares_of_the_natural_numbers(inputNumb)
b = squre_of_the_sum_of_natural_numbers(inputNumb)
print(sum_squre_difference(a, b))


'''
# Problem 6: What is the difference between the sum of the squares and the square of the sums?

First of all, one could use a brute force implementation, because 100 is not a really high limit. This could be done as follows:

	limit = 100
	sum_sq = 0
	sum = 0
	for i = 1 to limit do
		sum = sum + i
		sum sq = sum sq + i ** 2
	end for
	print sum ** 2 − sum_sq

However, such an approach would definitely get in trouble when limit becomes very large.

A closer look at the program shows that the sum variable, at the end, contains the sum of the integers from 1 to limit. As is widely known, this sum can be directly calculated using the formula sum(n) = n(n + 1)/2. As you might have expected, such a formula also exists for the sum of squares. Let us derive this formula.

Thus, we are looking for a function f(n), that for any n gives the sum of 1**2 up to n**2. Assume it is of the form f(n) = an**3 + bn**2 + cn + d, with a, b, c, d constants that we have to determine. This we can do because we can verify that f(0) = 0, f(1) = 1, f(2) = 5, f(3) = 14. This yields four equations in four variables, namely

								d	=	0
		a	+	b	+	c	+	d	=	1
		8a	+	4b	+	2c	+	d	=	5
		27a	+	9b	+	3c	+	d	=	14

Solving this system of equations, we obtain a = 1/3, b = 1/2, c = 1/6, d = 0. This gives f(n) = 1/6(2n**3 + 3n**2 + n) = n/6(2n + 1)(n + 1).

What remains is to show this f actually is what we want. This we prove by induction: Assuming f is the correct formula for n, we show it is also for n + 1. Then, because we know it is correct for n = 0, 1, 2, 3, we know that it’s correct for all n. Thus, we have to show f(n + 1) = f(n) + (n + 1)**2. By expanding both sides we get

Since both sides are equal, we have proven that f is the correct formula. This means that we can now write a very simple program to calculate the difference between the sum of the squares and the square of the sum:

	limit = 100
	sum = limit(limit + 1)/2
	sum_sq = (2limit + 1)(limit + 1)limit/6
	print sum**2 − sum_sq

This algorithm is limited only by the size of the integer types your programming language (and computer memory) support.

'''
