---
layout: post
title: Largest palindrome product, Problem 4
---

> A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

> Find the largest palindrome made from the product of two 3-digit numbers.

### python 3.0. solved on 2016-7-12

```python
def palindromeGenerator(digit):
  digitFix = int(digit / 2)
  a = 10 ** (digitFix - 1)
  aSqur = a * 10
  palindromeList = []

  # print('%s, %s' % (a, aSqur))

  if digit < 2:
    print("there is no palindrome in the range")
    return None

  elif digit >=2:
    while a < aSqur:
      strA = str(a)
      palindrome = strA + ''.join(reversed(strA))
      palindromeList.append(int(palindrome))
      a += 1
    return(palindromeList)

def nDigitMultiplicator(digit, target):
  d = 10 ** (digit - 1)
  dReset = d - 1
  t = target
  dSqur = 10 ** (digit)
  nDigitMultiply = []
  # print('d: %s, t: %s, dSqur: %s' % (d, t, dSqur))

  while d < dSqur:
    # print(d)
    c = dReset + 1
    while c < dSqur:
      # print(d, c)
      if c * d == target:
        nDigitMultiply.append([c,d])
        # print(c, d, target)
        break
      c += 1
    d += 1

  if len(nDigitMultiply) < 1:
    # print("there is no %s-digit numbers to product %s" % (digit, target))
    return(False)
  else:
    print('we found them: %s results in %s' % (len(nDigitMultiply), target))
    return(nDigitMultiply)

targetNumbers = palindromeGenerator(6)
accepted = []

for i in targetNumbers:
  if nDigitMultiplicator(3, i) == False:
    continue
  else:
    accepted.append(nDigitMultiplicator(3, i))
    continue

print(max(accepted))
```
