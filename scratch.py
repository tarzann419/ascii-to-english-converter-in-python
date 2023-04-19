class Translator:
    def __init__(self):
        pass

    @staticmethod
    def ascii_to_english(word):
        return ''.join([chr(int(char)) for char in word.split()])

    @staticmethod
    def english_to_ascii(word):
        return ' '.join([str(ord(char)) for char in word])


translator = Translator()


# start ciode
word = input('what would you like to convert?\n')
print("Original word: ", word)

# ascii converter
ascii_word = translator.english_to_ascii(word)
print("ASCII code: ", ascii_word)

# back to english
english_word = translator.ascii_to_english(ascii_word)
print("English word: ", english_word)
