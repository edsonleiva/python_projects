#the word list was downloaded from github from the user deekayen
# https://gist.github.com/deekayen/4148741
# full credit goes to deekayen for file word_text.txt
# code below is mine which reads the file and creates a list from it

def create_word_list():

    #ensure that you update the file pate if your word list .txt file is saved on your computer with different file path
    word_file = open('/Users/edsonleiva/Desktop/python_test/100_days_coding/hangman/word_list.txt', 'r')

    data = word_file.read()

    #converts the txt file full of words into a list
    data_list = data.replace('\n', ' ').split()
    word_file.close()

    return data_list

word_list = create_word_list()

