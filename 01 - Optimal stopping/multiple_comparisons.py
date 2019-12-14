'''
The secretary problem

Given a set of applicants, we have to select the best one. There's limited
time for the task, though, and we must balance a good choice and the time
invested in the search. Instead of analysing each applicant, we should check
around 37% of them and then get the following one that exceed the best one
out of the 37% analised.

here we run a batch of comparisions between the selections made by the 37%
rule and a selection of the best candidate that runs through the whole list
of candidates. This can be used to validate the table presented in the book.
'''

from random import sample
from single_comparison import opt_stop_37

def full_scan(candidates):
    return max(candidates)


qt_cand = input('How many candidates do you want to generate? ')
qt_comp = input('How many times do you want to compare the 37% selection with a full scan selection? ')

qt_right = int()
qt_wrong = int()
for comp in range(0,int(qt_comp)):
    #Generating a list of random elements. Let's pick qt_cand numbers in an universe of 1 to (qtc_cand*2).
    candidates = sample(list(range(1,int(qt_cand)*2)),int(qt_cand))
    
    #Select the best one using the 37% rule and then the really best using the full scan
    best_37 = opt_stop_37(candidates)  
    best_full = full_scan(candidates)
    
    if best_37 == best_full:
        qt_right += 1
    else:
        qt_wrong += 1
    
success_rate = qt_right / int(qt_comp) * 100
print(f'Out of {qt_comp} selections the 37% rule got {qt_right} right, missing {qt_wrong}. Success rate: {success_rate}')


