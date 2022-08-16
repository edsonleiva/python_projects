###### TREASURE HUNT ######

#art by ASCII ART
print('''
#############################################################################
#(@@@@)                    (#########)                   (@@@@@@@@(@@@@@@@@@#
#@@@@@@)___                 (####)~~~   /\                ~~(@@@@@@@(@@@@@@@#
#@@@@@@@@@@)                 ~~~~      /::~-__               ~~~(@@@@@@@@)~~#
#@@@)~~~~~~                           /::::::/\                  ~~(@@@@)   #
#~~~                              O  /::::::/::~--,                 ~~~~    #
#                                 | /:::::/::::::/{                         #
#                 |\              |/::::/::::::/:::|                        #
#                |:/~\           ||:::/:::::/::::::|                        #
#               |,/:::\          ||/'::: /::::::::::|                       #
#              |#__--~~\        |'#::,,/::::::::: __|   ,,'`,               #
#             |__# :::::\       |-#"":::::::__--~~::| ,'     ',     ,,      #
#,    ,,     |____#~~~--\,'',.  |_#____---~~:::::::::|         ',','  ',    #
# '.,'  '.,,'|::::##~~~--\    `,||#|::::::_____----~~~|         ,,,     '.''#
#____________'----###__:::\_____||#|--~~~~::::: ____--~______,,''___________#
#^^^  ^^^^^   |#######\~~~^^O, | ### __-----~~~~_____########'  ^^^^  ^^^   #
#,^^^^^','^^^^,|#########\_||\__O###~_######___###########;' ^^^^  ^^^   ^^ #
#^^/\/^^^^/\/\^^|#######################################;'/\/\/^^^/\/^^^/\/^#
#   /\/\/\/\/\  /\|####################################'      /\/\/\/\/\    #
#\/\/\     /\/\/\  /\/\/\/\    /\/\/\/\/\   /\/\/\    /\/\/\/\      /\/\/\/\#
#spb\/\/\    /\/\/\/\    /\/\/\/\    /\/\/\/\   /\/\/\/\    /\/\/\/\/\      #
#############################################################################
''')

#intro the the pirate journey
print('\n\nWelcome aboard to the Reaper!')
print('We are setting sail to the Island of Despair seeking the hidden treasure.')
print('Legend has it even the bravest have never returned from the journey.')

#first scenario
print('\nThere is a huge mountain up ahead with a dark ravine down the middle! We are unsure where it leads to and if our ship will fit. Going around might be the safest option, but it might take us hours.\n')

#ask user for input on the first scenario
scene1 = input('Which path do you want to take? "Ravine" or "Around" ')[0].upper()

#based on user input determine the outcome of the first scenario
if scene1 == 'R':
    print('\nGet ready we are heading into the ravine!')
    print('Our ship barely fits!')
    print('We see the exit! Great job crew!\n\n')

    #intro into the second scenario
    print('Do you guys see that?!')
    print('A pirate ship ahead on our left side!')

    #ask the user for input on the second scenario
    scene2 = input('Should we fight them or speed past them going to the right? "Fight" or "Run" ')[0].upper()

    #determine outcome based on user input
    if scene2 == 'F':
        print('\nPrepare for attack!')
        print('We have destroyed their ship! It\'s sinking!')
        print('Onward we go. We are close to the Island of Despair.\n\n')

        #Intro to the final scenario
        print('We see the shore of the Island of Despair!')
        scene3 = input('Should we drop the anchor by the beach side or on the dock? "Beach" or "Dock" ')[0].upper()

        #determine outcome of the final scenario
        if scene3 == 'B':
            print('\nWe landed on the Island of Despair safely!')
            print('Congratulations! We are the first pirates to make it to the Island of Despair!')
            print('Now to find the Island\'s treasure! ')
        
        else:
            print('\nOn the way to the dock there was a mysterious creature that looked half octopus and half shark!')
            print('The Reaper couldn\'t handle the attack. The ship sank with all of its crew!')
            print('Game Over!')

    else:
        print('\nAll speed Northeast! We plan on out speeding them!')
        print('Nooooo! They are gaining on us! Incoming cannonballs!')
        print('Crew was not prepared to fight. The Reaper was sunk by the pirates!')
        print('Game Over!')

else:
    print('\nHoist the sails! We are heading around the mountain!')
    print('After two hours of sailing around the mountain. A large thunderstorm erupted whiping out the entire crew!')
    print('Game Over!')