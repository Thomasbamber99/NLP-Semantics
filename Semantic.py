import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("Spaceship")
word2 = nlp("Extraterrestrial")

print(word1.similarity(word2))

# I did not expect so many decimal places!

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# I found it interesting that it is able to link patterns between words and output information which makes sense to the viewer

tokens2 = nlp("sword knight cheese mouse trap")

for token1 in tokens2:
    for token2 in tokens2:
        print(token1.text, token2.text, token1.similarity(token2))

# after running the example.py file with en_core_web_sm the output is much harder to read and understand