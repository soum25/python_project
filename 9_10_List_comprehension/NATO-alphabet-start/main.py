import pandas

# TODO 1. Create a dictionary

data = pandas.read_csv("nato_phonetic_alphabet.csv")
my_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(my_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("enter your name: ").upper()
code_words = [f"{letter} = {my_dict[letter]}" for letter in name if letter in my_dict]
print(code_words)
