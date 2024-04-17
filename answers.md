# CMPS 2200 Assignment 3
## Answers

**Name:**Ivo Tomasovich


Place all written answers from `assignment-03.md` here for easier grading.

1a)

-Start with the largest denomination coin available, which is 2^k, where k is the largest integer such that 2^k  is less than or equal to N.
-Subtract 2^k from N as many times as possible without making the result negative.
-Move to the next smaller denomination coin and repeat step 2 until N becomes zero.
1b)

Greedy Choice Property:

Assume there exists an optimal solution that does not follow the greedy choice, meaning at some step, it selects a coin denomination that is not the largest possible denomination less than or equal to the remaining amount.

Let's say the algorithm selects a coin denomination c_1 , but there exists a larger denomination c_2  such that c_2 > c_1 and c_2
​ is the largest denomination less than or equal to the remaining amount.

Now, if we replace c_1  with c_2 in the solution, the total number of coins will decrease or remain the same, as c_2  is larger than 
c_1. Thus, the new solution will be at least as good as the previous one, contradicting the assumption that the original solution was optimal. Therefore, the greedy choice property holds.

Optimal Substructure Property:

To prove the optimal substructure property, let's consider any optimal solution for a given amount N

Suppose the optimal solution uses a certain number of coins of denomination c_1,c_2, ...,c_k. If we take any subset of these coins, we get an optimal solution for the remaining amount 
N′, where N′is the amount obtained by subtracting the total value of the selected coins from N


This is because, if there existed a better solution for N′that doesn't include some of the coins in our optimal solution, we could add those coins back to obtain a better solution for N, contradicting the optimality of our original solution.

Therefore, the problem exhibits the optimal substructure property.

Since the greedy algorithm satisfies both the greedy choice property and the optimal substructure property, it produces an optimal solution for the problem. Thus, the greedy algorithm is optimal for producing the fewest number of coins to sum up to 
 dollars with denominations of powers of 2.

1c) Work = O(logn), Span = O(logn); N is the amount to be converted into coins

2a) Let's assume we have the following set of denominations available at a bank in Fortuito: {1,3,4}

Now, consider the case where we need to make change for N=6.

If we apply the greedy algorithm, it will choose the largest denomination less than or equal to the remaining amount at each step. So, in this case, the greedy algorithm would proceed as follows:

-Start with N=6.
-Choose D_2=4. Subtract 4 from 6, leaving 2.
-Choose D_1=3 Subtract 3 from 2. Now we're left with -1, which is not a valid amount.
The greedy algorithm fails in this case because it chooses the largest denomination available at each step without considering the possibility that a combination of smaller denominations might result in fewer total coins.

2b) 
To prove the optimal substructure property for this problem, let's define OPT(N) as the minimum number of coins needed to make change for N dollars. We aim to show that OPT(N) can be recursively constructed from optimal solutions to its subproblems.

The optimal substructure property can be stated as follows:

Optimal Substructure Property: For any amount N, the minimum number of coins needed to make change for N dollars can be obtained by considering all possible choices of the last coin used in the optimal solution.

Let's prove this property:

Consider any optimal solution for making change for N dollars. Let 
c_k be the last coin used in this optimal solution, where c_k has a denomination D_k.

Now, there are two cases:

1. c_k is not used in the optimal solution: In this case, the optimal solution for N dollars is the same as the optimal solution for N dollars without using c_k. Since 
c_k is not used, the minimum number of coins needed for N dollars remains the same.
2. c_k is used in the optimal solution: If c_k is used, then the remaining amount after using c_k is N − D_k dollars. Therefore, the optimal solution for making change for N dollars can be obtained by finding the optimal solution for N − D_k dollars and adding 1 to account for the coin c_k used.

Since we can obtain the optimal solution for N dollars by considering all possible choices of the last coin used, the problem exhibits optimal substructure.

Thus, we have shown that the problem has the optimal substructure property, which suggests that dynamic programming or another algorithm that exploits this property can be used to find the optimal solution efficiently.

2c)

-Initialize an array dp of size N+1, where dp[i] represents the minimum number of coins needed to make change for i dollars. Initialize all elements of dp to infinity, except for dp[0]=0.
-Iterate from 1 to N and for each i, compute dp[i] as follows:
For each denomination D_j, where D_j is less than or equal to i, compute dp[i]=min(dp[i],dp[i−D_j]+1).
Return dp[N], which represents the minimum number of coins needed to make change for N dollars. 

Using memoization (either top-down or bottom-up), we avoid recomputing solutions to subproblems, resulting in a more efficient algorithm.

Work = O(N*K)
Span = O(N)

N is the amount to be converted into coins and K is the number of denominations available.