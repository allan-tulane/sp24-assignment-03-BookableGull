from main import *

def test_MED():
    assert fast_MED("kitten", "sitting") == 3

def test_alignment():
    dist, align_S, align_T = fast_align_MED("relevant", "elephant")
    print("Distance:", dist)
    print("Alignment S:", align_S)
    print("Alignment T:", align_T)
    assert dist == 4