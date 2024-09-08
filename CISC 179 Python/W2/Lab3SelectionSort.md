# Lab 3 Selection Sort

```python
import random
# Generate prime numbers (Sieve of Eratosthenes)
def generatePrimes(n):
    prime = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if sieve[p]:
            prime.append(p)
            for i in range(p*p, n+1, p):
                sieve[i] = False
    return prime

# Generate prime numbers from 1 to 100
prime = generatePrimes(100)
print("Prime numbers from 1 to 100:", prime)

# Randomize the prime numbers
rnd_prime = prime.copy()
random.shuffle(rnd_prime)
print("Randomized prime numbers:", rnd_prime)

# Selection Sort algorithm
def selectionSort(arr):
    for i in range(len(arr)):
        minIdx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIdx]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

# Sort the randomized primes
selectionSort(rnd_prime)
print("Sorted prime numbers:", rnd_prime)
```
## Explain in your own words why did you select the particular algorithm?
I selected the Sieve of Eratosthenes algorithm because, from my research, this seems to be the most efficient algorithm to generate prime numbers that doesn't require extensive memory. 

## Why array data structure is a better choice over a list data structure? 
Due to the type of dataset we are working with, array data structures are superior to list data structures. Since all the data we are using is the same (all prime numbers) arrays offer memory efficiency and performance. If we needed to store different data types a list data structure can be more beneficial.
