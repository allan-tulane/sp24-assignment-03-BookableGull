# CMPS 2200 Assignment 3
## Answers

**Name:**Ivo Tomasovich
**Name:**Frankie Soltero



Place all written answers from `assignment-03.md` here for easier grading.


1a. 

function makeChange(N):

    coin_count = 0
    coins = []
    for k in descending order from floor(log2(N)) to 0:
        while N >= 2^k:
            N = N - 2^k
            coin_count = coin_count + 1
            coins.append(2^k)
    return coin_count, coins



1b. Given an amount N, lets say the greedy algorithm chooses a coin of denomination 2^k, which is the largest denomination less than or equal to N. Since the denomination is a power of 2, teh remainder N - 2^k is also an amount for which we need to find change. No larger denomination could have been chosen, since that would exceed the amount N, and any smaller denomination would not be as efficient.



1c. The work and Span are O(logN)




2a. Consider a currency system where the denominations are 1,3,4 if we need make change for 6 using the greedy algorith,, it would choose one 4 and 2 1's giving us 3 coins in total. However the optimal solution would be 2 3's which is 2 coinds. This shows it doesn't always produce the fewest coins




2b. The optimal way to go about this would be to make change for some amount N and subtract D or a denomination of one of the coins used in the optimal solution.
Proof: Lets assume that removing a coin of denomination D from the optimal solution for N does not leave an optimal solution for N - D. that would mean there is a better solution when D is added back it would give a better solution for N than the assumed optimal one. This is a contradiction therefore it is proved by contradiction.






2c.
function dynamicChangeMaking(denominations, N):
    minCoins = array of size N+1 with all values set to infinity
    minCoins[0] = 0
 
    for i from 1 to N:
        for each denomination D in denominations:
            if i >= D:
                minCoins[i] = min(minCoins[i], minCoins[i - D] + 1)
 
    return minCoins[N] if minCoins[N] != infinity else "No solution"
The span for the pseudo code I have provided would be O(N) and the work would be O(kN) where k is the number of denominations