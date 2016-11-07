---
layout: post
title: Smallest multiple, Problem 5
---
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

### python 3.0. solved on 2016-7-14

```python
def evenDevider(value, tango):
  if value % tango == 0:
    return(True)

def Factorizationer(value):
  subMultiples = []
  tValue = value
  i = 1
  # print('i: %s' % i)
  while i < tValue:
    i += 1
    # print('i: %s \t tValue: %s' % (i, tValue))
    if tValue % i == 0:
      tValue = int(tValue / i)
      # print('gottcha! %s' % i)
      subMultiples.append(i)
      i = 1
      continue
    else:
      continue
  return subMultiples

def evenlyDivisibleFinder(vFrom, vTo):
  divisibleNumbs = []
  rawRange = range(vFrom, vTo + 1)
  for item in rawRange:
    result = Factorizationer(item)
    if len(result) == 0:
      continue
    if len(result) == 1:
      print('%s is prime number' % result)
      divisibleNumbs = divisibleNumbs + result
      continue
    print('%s is factorilized to\t%s' % (item, result))
  print(divisibleNumbs)

  setD = set(divisibleNumbs)
  setR = set(rawRange)
  setA = setR - setD
  cleanedRange = list(setA)

  print(cleanedRange)
  for item in cleanedRange:
    result = Factorizationer(item)
    print('%s is factorilized to\t%s' % (item, result))
    # if len(result) == 1:
    #   print('%s is prime number' % result)
    #   divisibleNumbs = divisibleNumbs + result

evenlyDivisibleFinder(1, 20)
```
