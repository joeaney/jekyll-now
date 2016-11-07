---
layout: post
title: Multiples of 3 and 5
---
# Multiples of 3 and 5

## Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

```javascript
var step;
var till = 1000;
var watertank = [];
var v = 0;
for (step = 0; step < till; step++) {
    if (step % 3 === 0 || step % 5 === 0) {
        v = v + step;
    }
}

console.log("answer is " + v);
```

Answer is 233168.
