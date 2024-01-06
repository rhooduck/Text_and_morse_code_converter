MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '\'': '. _ _ _ .',
    '!': '_ . _ . _ _',
    '/': '_ . . _ .',
    '(': '_ . _ _ .',
    ')': '_ . _ _ . _',
    '&': '. _ . . .',
    ':': '_ _ _ . . .',
    ';': '_ . _ . _ .',
    '=': '_ . . . _',
    '+': '. _ . _ .',
    '-': '_ . . . . _',
    '_': '. . _ _ . _',
    '"': '. _ . . _ .',
    '$': '. . . _ . . _',
    '@': '. _ _ . _ .',
}

def text_to_morse(text):
    morse_decoded = ""

    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_decoded += MORSE_CODE_DICT[char] + ' '

        else:
            morse_decoded += '/ '

    return print(morse_decoded)

def morse_to_text(morse):
    morse_char_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    text_decoded = ""

    for code in morse.split():
        if code == '/':
            text_decoded += ' '
        elif code in morse_char_dict:
            text_decoded += morse_char_dict[code]
        else:
            text_decoded += " "

    return print(text_decoded)


def is_text(user_input):

    character_list = list(MORSE_CODE_DICT.keys())
    morse_char_list = ['-', '.', '/']
    first_char = user_input[0].upper()

    if first_char in character_list and first_char in morse_char_list:
        user_interaction = input("Seems to me it's not a text. Do you want to decode morse to text?"
                                 "\nPlease write T for text to morse or M for morse to text.\n").upper()

        if user_interaction == 'T':
            return True

        elif user_interaction == 'Y':
            return False

        else:
            print('Wrong answer, please try again.')

    elif first_char in character_list:
        return True

    else:
        return False

keep_going = True

def main():
    user_message = input('Hello please enter text or morse code to decode:\n')
    if is_text(user_message):
        text_to_morse(user_message)
    else:
        morse_to_text(user_message)


def check_for_continue():
    global keep_going
    user_choice = input("Do you want to decode another text or morse?\n"
                        "Type Y / YES / or N / NO /.\n")
    if user_choice.upper() == 'N':
        keep_going = False
        print('Program closed. Bye')



while keep_going:
    main()
    check_for_continue()


