"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your program should be case-insensitive.
If the user input -1 for class name, your program would output
the maximum, minimum, and average among all the inputs.
"""

# class for class (named Lesson instead)
class Lesson():
    def __init__(self, name):
        self.name = name
        self.n = 0
        self.sum_score = 0
        self.max_score = 0
        self.min_score = 1000
        
    def find_max_min(self, new_score):
        if new_score > self.max_score:
            self.max_score = new_score            
        if new_score < self.min_score:
            self.min_score = new_score

    def print_info(self):
        if self.n >0:
            str_num = self.name[2:]
            print('=============',self.name,'=============')
            print('Max ('+str_num+'): ', self.max_score)
            print('Min ('+str_num+'): ', self.min_score)
            print('Avg ('+str_num+'): ', float(self.sum_score/self.n))
        elif self.n == 0:
            print('=============',self.name,'=============')
            print('No score for ', self.name)

def print_res(lesson1, lesson2):
    if lesson1.n + lesson2.n == 0:
        print('No class scores were entered')
    else:
        lesson1.print_info()
        lesson2.print_info()
    
def main():
    # only these 2 classes
    sc0 = Lesson('SC001')
    sc1 = Lesson('SC101')
    
    # keep until input '-1' 
    while True:
        print("Which class?")
        c = str(input()).upper()
        if c == '-1':
            # print result
            print_res(sc0, sc1)
            break
        else:
            print('Score:')
            score = int(input())
            
            if c == 'SC001':
                sc0.n +=1
                sc0.sum_score += score
                sc0.find_max_min(score)
                
            elif c == 'SC101':
                sc1.n +=1
                sc1.sum_score += score
                sc1.find_max_min(score)
            else:
                pass
        
#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
