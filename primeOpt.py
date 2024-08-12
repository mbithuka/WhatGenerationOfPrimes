import time
import math
import platform
from multiprocessing import Pool, freeze_support

def sieve_of_eratosthenes(limit):
    """Return a list of primes up to the limit using the Sieve of Eratosthenes."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(math.sqrt(limit)) + 1):
        if sieve[start]:
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

def segmented_sieve_worker(args):
    low, high, primes = args
    sieve = [True] * (high - low + 1)

    for p in primes:
        start = max(p * p, (low + p - 1) // p * p)
        for multiple in range(start, high + 1, p):
            sieve[multiple - low] = False

    if low == 0:
        sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    return [low + i for i, is_prime in enumerate(sieve) if is_prime]

def segmented_sieve(n):
    """Return a list of primes up to n using the segmented sieve algorithm."""
    try:
        limit = int(math.sqrt(n)) + 1
        primes = sieve_of_eratosthenes(limit)
        segment_size = max(limit, 32768)

        ranges = [(low, min(low + segment_size - 1, n), primes) 
                  for low in range(0, n + 1, segment_size)]

        with Pool() as pool:
            segments = pool.map(segmented_sieve_worker, ranges)

        primes_list = []
        for segment in segments:
            primes_list.extend(segment)

        return primes_list

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def measure_time(func, *args):
    """Measure the execution time of a function."""
    try:
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return result, elapsed_time
    except Exception as e:
        print(f"An error occurred while measuring time: {e}")
        return [], 0

if __name__ == "__main__":
    if platform.system() == "Windows":
        freeze_support()  # Needed only for Windows

    # Measure the time taken to generate all primes up to 2^30
    n = 2**30 - 1
    primes, time_taken = measure_time(segmented_sieve, n)

    print(f"Number of primes found: {len(primes)}")
    print(f"Time taken: {time_taken:.2f} seconds")
