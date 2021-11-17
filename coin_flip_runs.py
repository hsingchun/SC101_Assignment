"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r

def main():
    print("Let's filp a coin!")
    # target run
    targ_run = int(input())
    
    # setting
    res_str = ''
    first = 'first'
    n_in_row = 1
    n_run = 0
    
    while n_run < targ_run:
        new = r.choice(('H', 'T'))
        res_str += new
        
        # count n in row
        if new == first:
            n_in_row +=1
        # when ends in a row, add one run, and reset counter
        if (n_in_row >1)&(new!=first):
            n_run +=1
            n_in_row = 1
            
        # last run should end when n_in_row == 2
        if (n_run == targ_run-1)&(n_in_row==2):
            break
        first = new
            
    print('Number of runs:', targ_run)
    print(res_str)
        

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
