def create_word_list():

    word_file = open('/Users/edsonleiva/Desktop/python_test/100_days_coding/hangman/word_list.txt', 'r')

    data = word_file.read()

    #converts the txt file full of words into a list
    data_list = data.replace('\n', ' ').split()
    word_file.close()

    return data_list

word_list = create_word_list()

