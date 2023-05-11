import pandas as pd

data = pd.read_csv("phonetic_alphabet.csv")
phonetic_data_frame = pd.DataFrame(data)
phonetic_alphabets = {row.letter: row.code for (index, row) in phonetic_data_frame.iterrows()}


def get_phonetics():
    word = input("Enter a word: ").upper()

    try:
        word_phonetics = [phonetic_alphabets[letter] for letter in word]

    except KeyError:
        print("Only Alphabets are allowed please.")
        get_phonetics()

    else:
        print(word_phonetics)


get_phonetics()


