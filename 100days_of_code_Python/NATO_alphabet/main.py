import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dic = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word:").upper()
output = [nato_dic[alphabet] for alphabet in word]
print(output)



