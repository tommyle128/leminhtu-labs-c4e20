from random import *
from eval import calc

def generate_quiz():
    # Hint: Return [x, y, op, result]
    from random import randint, choice
    
    x = randint(1, 10)
    y = randint(1, 10)
    op = choice(['+', '-', '*', '/'])
    res = calc(x, y, op)

    err = randint(-1,1)
    display_res = res + err
       
    return [x, y, op, display_res]
   
def check_answer(x, y, op, display_res, user_choice):
    # user_choice: True/False nhiem vu la return ra True or False
    true_res = calc(x, y, op)
    if true_res == display_res:
        return user_choice
    else:
        return not user_choice
    
     
    
    
