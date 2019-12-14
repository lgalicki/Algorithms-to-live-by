'''
The secretary problem

Given a set of applicants, we have to select the best one. There's limited time
for the task, though, and we must balance a good choice and the time invested
in the search. Instead of analysing each applicant, we should check around 37%
of them and then get the following one that exceed the best one out of the 37%
analised.

Here I'll compare the result of such technique against analysing each single
applicant.
'''

from random import sample

def optimal_percentage(qt_cand):
    '''
    Returns the optimal percentage of the sample that should be used for the 37% rule
    INPUT: quantity of candidates
    OUTPUT: percentage of  the sample
    '''
    table = {1:100,2:50,3:33.33,4:25,5:40,6:33.33,7:28.57,8:37.5,9:33.33,
             10:30,20:35,30:36.67,40:37.5,50:36,100:37,1000:36.9}
    
    #Higher than 1000? Fixed value.
    if int(qt_cand) > 1000:
        return 36.9
    
    #Between 1 and 1000? Looks for where it matches in between the defined values.
    keys = list(table.keys())
    for key in keys:
        if key == qt_cand:
            return table[key]
        elif key < qt_cand:
            prev_key = key
            continue
        else:
            return table[prev_key]

    
def opt_stop_37(candidates):
    '''
    Uses the 37% rule to select a possible best candidate.
    INPUT: list of candidates
    OUTPUT: selected candidate
    '''
    qt_cand = len(candidates)
    
    #Deciding the optimal sampling percentage.
    sample_perc = optimal_percentage(int(qt_cand))
    
    #Now let's read the whole sample and get the best candidate out of it
    perc_read = float()
    qt_read = int()
    best_sample = int()
    
    while(perc_read < sample_perc):
        if candidates[qt_read] > best_sample:
            best_sample = candidates[qt_read]
        
        qt_read += 1
        perc_read = (qt_read / int(qt_cand)) * 100
        
    #Let's test the rest of the candidates and get the first one that is better the best sampled one.
    #NOTE: in case the best of all candidates was in the sample, we'll end up with the last in the population.
    for pos,cand in enumerate(candidates):
        #Skipping the sampled ones
        if qt_read > pos: #it's not >= because pos starts in 0
            continue
        
        #Found a better than the best sampled.
        if cand > best_sample:
            return cand
            
    #Couldn't find someone better that the best sampled. Return the last one.
    return cand


if __name__ == '__main__':

    qt_cand = input('How many candidates do you want to generate? ')
    if int(qt_cand) > 1:
        #Generating a list of random elements. Let's pick qt_cand numbers in an universe of 1 to (qtc_cand*2).
        candidates = sample(list(range(1,int(qt_cand)*2)),int(qt_cand))

        #Select the best one using the 37% rule
        best_37 = opt_stop_37(candidates)
        print(f'The best one selected by the 37% rule is {best_37}')