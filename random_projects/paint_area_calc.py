from math import ceil

def cans_calc(height,width,cover=400):

    return ceil(((height * width)*4) / cover)

test_h = int(input('What is the height of the wall? '))
test_w = int(input('what is the width of the wall? '))

calculation = cans_calc(test_h,test_w)

print(f'You will need {calculation} can(s) of paint for your project.')