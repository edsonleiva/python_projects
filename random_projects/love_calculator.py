###### LOVE CALCULATOR ######

active = True

while active:
    #intro
    print('Welcome to the Love Calculator!\n')

    #ask for the two names that you would like to calculate
    name1 = input('What is your name? ').lower()
    name2 = input('What is their name? ').lower()
    true_counter = 0
    love_counter = 0

    #created a list with the letter of true love for the calculation
    true_list = ['t','r','u','e']
    love_list = ['l','o','v','e']

    #check for the number of times that the letters true appear in both names
    for letter in true_list:
        if name1.count(letter) > 0 or name2.count(letter) > 0:
            true_counter += name1.count(letter)
            true_counter += name2.count(letter)

    #check for the number of times that the letters love appear in both names
    for letter in love_list:
        if name1.count(letter) > 0 or name2.count(letter) > 0:
            love_counter += name1.count(letter)
            love_counter += name2.count(letter)

    #combines both true_counter and love_counter to get the percentage
    percentage = int(str(true_counter) + str(love_counter))

    #adjust for a score over 100
    if percentage > 100:
        percentage = 100

    #check for the different percentages and gives back the results
    if percentage < 25:
        print(f'Your score is {percentage}%, sorry but we suggest you think twice about this one!')
    elif percentage >= 25 and percentage < 50:
        print(f'Your score is {percentage}%, tough call! We recommend not getting your hopes up, but you can still give it a try.')
    elif percentage >= 50 and percentage < 75:
        print(f'Your score is {percentage}%, we think you would go great with each other!')
    else:
        print(f'Your score is {percentage}%, you two were meant for each other!')


    #check to see if they would like to continue
    try_next = input('Would you like to continue? Y or N ')[0].upper()

    if try_next == 'N':
        active = False
    else:
        print('\n'*20)