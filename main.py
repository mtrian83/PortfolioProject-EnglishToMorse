original_sentence = input("Hi there! What would you like to translate to Morse Code?").upper()

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': ' '
}


def english_to_morse():
    morse = []
    for letter in original_sentence:
        morse_letter = str(morse_code.get(letter))
        morse.append(morse_letter)
    print("".join(morse))


english_to_morse()