---
layout: post
title: Largest prime factor, Problem 3
---

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

### Python 3.0. solved on 2016-7-11

``` python
def Factorizationer(value):
  subMultiples = []
  tValue = value
  i = 1
  print('i: %s' % i)
  while i < tValue:
    i += 1
    print('i: %s \t tValue: %s' % (i, tValue))
    if tValue % i == 0:
      tValue = int(tValue / i)
      print('gottcha! %s' % i)
      subMultiples.append(i)
      i = 1
      continue
    else:
      continue
  return subMultiples

target = 600851475143
print(Factorizationer(target))
```
