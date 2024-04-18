import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))
        
print(MED("elephant", "relevant"))


def fast_MED(S, T, MED={}):
    if (S, T) in MED:
        return MED[(S, T)]
  
    elif S == "":
        return len(T)
  
    elif T == "":
        return len(S)
  
    elif S[0] == T[0]:
        return fast_MED(S[1:], T[1:], MED)
  
    else:
        return 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED))

def fast_align_MED(S, T, MED={}):
  if (S, T) in MED:
      return MED[(S, T)]

    #Base Case
  if S == "":
      return ("-" * len(T), T)
  if T == "":
      return (S, "-" * len(S))

  #Recursive Case
  if S[0] == T[0]:
      edited_S, edited_T = fast_align_MED(S[1:], T[1:], MED)
      change = (S[0] + edited_S, T[0] + edited_T)
  else:
      insert_S, insert_T = fast_align_MED(S, T[1:], MED)
      delete_S, delete_T = fast_align_MED(S[1:], T, MED)
    
      insert_cost = 1 + len(insert_S)
      delete_cost = 1 + len(delete_S)

      if insert_cost <= delete_cost:
        change = ("-" + insert_S, T[0] + insert_T)
      else:
         change = (S[0] + delete_S, "-" + delete_T)
  #Store for future
  MED[(S, T)] = change
  return change