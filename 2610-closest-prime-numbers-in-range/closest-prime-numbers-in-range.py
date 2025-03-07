class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        '''
        - 2 ptr???
        ->Sieve of Eratosthenes to mark numbers that are primes.
        -> check if prime number
        ->> find 2 prime numbers s.t. difference is minimized
        ->>> for num2-num1  
        '''
        def sieve(start,end):
            primes = [True for _ in range(end+1)]
            primes[0] = primes[1] = False
            for i in range(2,int(sqrt(end))+1):
                if not primes[i]: 
                    continue
                for j in range(i+i, right+1,i):
                    primes[j] = False
            ret = []
            for i in range(len(primes)):
                if primes[i] and i>= start:
                    ret.append(i)
            return ret
        primes = sieve(left,right)
        ret = [-1,-1]
        mini = float('inf')
        for i in range(1,len(primes)):
            if primes[i] - primes[i-1] < mini:
                mini = primes[i] -primes[i-1]
                ret = [primes[i-1],primes[i]]
        return ret