import pandas as pd
nato_data = pd.read_csv(r"NATO-alphabet-start\nato_phonetic_alphabet.csv")

mapped_dict={row['letter']:row['code'] for idx,row in nato_data.iterrows()}

word = input("Enter a word: ").upper()
coded_list = [mapped_dict[letter] for letter in word]
print(coded_list)