# WhatGenerationOfPrimes
Suppose we generate x random numbers, filter our random numbers and extract prime numbers. Given the length of our prime numbers, we generate new numbers and filter out for primes. We repeat this process until we find which stage/ generation has only two primes present. 

#### what curiosity doth,

1. What is the distribution of prime numbers in each generation of the process, and how does it evolve over successive generations?
2. How does the length of the prime numbers in each generation correlate with the likelihood of encountering a generation with only two prime numbers present?
3. What is the average number of generations required to reach a state where only two prime numbers remain, and how does this vary with different initial parameters (e.g., range of random numbers, length of generated numbers)?
4. Are there any patterns or trends observed in the occurrence of generations with only two prime numbers, and if so, what factors influence these patterns?
5. How does the efficiency of the filtering process for prime numbers impact the rate of convergence towards a generation with only two primes?
6. What is the impact of increasing the sample size (number of iterations) on the stability and consistency of the results obtained regarding the presence of only two prime numbers in a generation?
7. Can statistical models or machine learning algorithms be employed to predict the likelihood of encountering a generation with only two prime numbers based on the initial parameters and the evolution of prime numbers across generations?
8. Are there any practical applications or implications of the observed phenomena in terms of cryptography, random number generation, or optimization algorithms?
9. is there a relationship between the generational progression—shown by the "x" growing—and the probability of achieving the goal of coming across a generation in which there are only two prime numbers?
   

#### Hypothesis:

***We conjecture that as the generations go on, there will be a greater chance of coming across a generation in which there are only two prime numbers. This is because the process involves generating random numbers, filtering for prime numbers, and then generating new numbers based on the length of the prime numbers until only two prime numbers remain. According to this theory, the primality-based filtering mechanism and the intrinsic randomness of number formation cause a convergence towards a situation in which there are only two prime numbers remaining. Moreover, we predict that as the number of repetitions or generations rises, the likelihood of coming across a generation with just two primes will rise.***

## Conclusion:
 
To run:  
~~~
python3 yeah.txt
~~~
