import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))

def fast_MED(S, T, memo=None):
    if memo is None:
        memo = {}
    
    if (S, T) in memo:
        return memo[(S, T)]
    
    if S == "":
        return len(T)
    elif T == "":
        return len(S)
    else:
        if S[0] == T[0]:
            result = fast_MED(S[1:], T[1:], memo)
        else:
            sub_cost = 1  # Cost of substitution
            del_cost = 1  # Cost of deletion
            ins_cost = 1  # Cost of insertion
            result = 1 + min(fast_MED(S, T[1:], memo),      # Insertion
                             fast_MED(S[1:], T, memo),      # Deletion
                             fast_MED(S[1:], T[1:], memo))  # Substitution
        memo[(S, T)] = result
        return result

def fast_align_MED(S, T, memo=None):
    if memo is None:
        memo = {}

    if (S, T) in memo:
        return memo[(S, T)]

    if S == "":
        return len(T), "-" * len(T), T

    elif T == "":
        return len(S), S, "-" * len(S)

    else:
        cost = 0 if S[0] == T[0] else 1

        dist_insert, align_insert_S, align_insert_T = fast_align_MED(S, T[1:], memo)
        dist_delete, align_delete_S, align_delete_T = fast_align_MED(S[1:], T, memo)
        dist_sub, align_sub_S, align_sub_T = fast_align_MED(S[1:], T[1:], memo)

        dist_delete += 1
        dist_insert += 1
        dist_sub += cost

        min_dist = min(dist_insert, dist_delete, dist_sub)

        if min_dist == dist_insert:
            align_S = "-" + align_insert_S
            align_T = T[0] + align_insert_T
        elif min_dist == dist_delete:
            align_S = S[0] + align_delete_S
            align_T = "-" + align_delete_T
        else:  # Substitution
            align_S = S[0] + align_sub_S
            align_T = T[0] + align_sub_T

        # Additional case for when an extra character is inserted at the beginning
        if min_dist == dist_sub and cost == 1:
            align_S = "-" + align_S
            align_T = "-" + align_T
            min_dist += 1

        memo[(S, T)] = (min_dist, align_S, align_T)
        return memo[(S, T)]
