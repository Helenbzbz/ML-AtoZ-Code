MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

SPACE_LETTER = '   '
SPACE_WORD_ADDITION = '    '
SPACE_WORD = '       '

def encode():
    sentence = input('Please enter the sentense you want to encode:\n').strip()
    encoded_sentence = []
    word_list  = sentence.split(' ')
    for word in word_list:
        for letter in list(word):
            if letter.upper() not in list(MORSE_CODE_DICT.keys()):
                print(f"\'{letter.upper()}\' is not supported in morse code. Only letters, numbers, and these symbols are supported: {' '.join(list(MORSE_CODE_DICT.keys())[-7:])}\n")
                return 
            encoded_sentence.append(MORSE_CODE_DICT[letter.upper()])
            encoded_sentence.append(SPACE_LETTER)
        encoded_sentence.append(SPACE_WORD_ADDITION)
    return ''.join(encoded_sentence)

def decode():
    sentence = input('Please enter the sentense you want to decode:\n').strip()
    word_list  = sentence.split(SPACE_WORD)
    print(word_list)

    decoded_sentence = []
    key_lists = list(MORSE_CODE_DICT.keys())
    value_lists = list(MORSE_CODE_DICT.values())

    for word in word_list:
        for letter in word.split(SPACE_LETTER):
            print(letter)
            if letter not in value_lists:
                print(f"\'{letter.upper()}\' is not found in morse code. Please double check.")
                return 
            index = value_lists.index(letter)
            decoded_sentence.append(key_lists[index])
        decoded_sentence.append(' ')

    return ''.join(decoded_sentence).strip()

def rules():
    print('1. Each character is composed of \'.\' and \'-\'\n2. The space between letters is three units\n3. The space between words is even units')

def dictionary():
    for char in MORSE_CODE_DICT:
        print(f'{char}: {MORSE_CODE_DICT[char]}')

is_on = True
while is_on:
    mode = input(f"Please choose the mode. Type \'E\' for encode, \'D\' for decode, \'R\' for rules, \'N\' for dictionaries, \'Q\' for quit: ").strip().upper()
    result = None
    if mode == 'Q':
        is_on = False
    elif mode == 'E':
        result = encode()
    elif mode == 'D':
        result = decode()
    elif mode == 'R':
        rules()
    elif mode == 'N':
        dictionary()
    else:
        print('Please choose a valid option')
    
    if result:
        print(result)