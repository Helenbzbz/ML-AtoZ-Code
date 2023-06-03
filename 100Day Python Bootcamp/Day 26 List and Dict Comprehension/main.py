import pandas as pd

alphabet_pd = pd.read_csv("100Day Python Bootcamp/Day 26 List and Dict Comprehension/nato_phonetic_alphabet.csv")
alphabet_dict = {}
for (index, row) in alphabet_pd.iterrows():
    alphabet_dict[row.letter] = row.code

user_input = input("Please enter the word: ")
output = [alphabet_dict[letter.upper()] for letter in user_input]

print(output)


