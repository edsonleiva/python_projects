
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(message,shift_amt,option):

    new_text = ''

    #if the option is decode the shift goes backwards
    if option == 'decode':
        shift_amt *= -1

    #finds the position of each letter and moves it according to shift - if char is not a letter it just appends without changing the value
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            new_text += alphabet[position+shift_amt]
        else:
            new_text += char
    print(f'Your {option}d text is:\n{new_text}')

end_program = False

while not end_program:

    choice = input('Type "encode" to encrypt or "decode" to decrypt\n').lower()
    text = input('Enter your message:\n')
    shift = int(input('Enter the shift amount: ')) % 26

    caesar(text,shift,choice)

    again = input('Type "Yes" if you would like to continue: ').lower()

    if again != 'yes':
        end_program = True
        print('Goodbye')
