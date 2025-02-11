import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

# Sample text
text = "ChatGPT is an advanced AI model for text processing."

# Tokenize the text
words = nltk.word_tokenize(text)

# Perform POS tagging
pos_tags = nltk.pos_tag(words)

print("POS Tags:", pos_tags)
