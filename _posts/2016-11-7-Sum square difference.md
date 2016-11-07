---
layout: post
title: Sum square difference, Problem 6
---
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

### python 3.0. solved on 2016-7-14

```python
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
```
